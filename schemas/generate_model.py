"""
Generate address space c++ code from xml file specification
"""
import sys
from copy import copy

import xml.etree.ElementTree as ET

from IPython import embed

NeedOverride = []
NeedConstructor = []#["RelativePathElement", "ReadValueId", "OpenSecureChannelParameters", "UserIdentityToken", "RequestHeader", "ResponseHeader", "ReadParameters", "UserIdentityToken", "BrowseDescription", "ReferenceDescription", "CreateSubscriptionParameters", "PublishResult", "NotificationMessage", "SetPublishingModeParameters"]
IgnoredEnums = []#["IdType", "NodeIdType"]
#we want to implement som struct by hand, to make better interface or simply because they are too complicated 
IgnoredStructs = []#["NodeId", "ExpandedNodeId", "Variant", "QualifiedName", "DataValue", "LocalizedText"]#, "ExtensionObject"]
#by default we split requests and respons in header and parameters, but some are so simple we do not split them
NoSplitStruct = ["GetEndpointsResponse", "CloseSessionRequest", "AddNodesResponse", "BrowseResponse", "HistoryReadResponse", "HistoryUpdateResponse", "RegisterServerResponse", "CloseSecureChannelRequest", "CloseSecureChannelResponse", "CloseSessionRequest", "CloseSessionResponse", "UnregisterNodesResponse", "MonitoredItemModifyRequest", "MonitoredItemsCreateRequest", "ReadResponse", "WriteRequest", "WriteResponse", "TranslateBrowsePathsToNodeIdsRequest", "TranslateBrowsePathsToNodeIdsResponse", "DeleteSubscriptionsRequest", "DeleteSubscriptionsResponse", "PublishRequest", "CreateMonitoredItemsResponse", "ServiceFault", "AddReferencesRequest", "AddReferencesResponse"]
OverrideTypes = {}#AttributeId": "AttributeID",  "ResultMask": "BrowseResultMask", "NodeClassMask": "NodeClass", "AccessLevel": "VariableAccessLevel", "UserAccessLevel": "VariableAccessLevel", "NotificationData": "NotificationData"}
OverrideNames = {}#{"RequestHeader": "Header", "ResponseHeader": "Header", "StatusCode": "Status", "NodesToRead": "AttributesToRead"} # "MonitoringMode": "Mode",, "NotificationMessage": "Notification", "NodeIdType": "Type"}

#some object are defined in extensionobjects in spec but seems not to be in reality
#in addition to this list all request and response and descriptions will not inherit
#NoInherit = ["RequestHeader", "ResponseHeader", "ChannelSecurityToken", "UserTokenPolicy", "SignatureData", "BrowseResult", "ReadValueId", "WriteValue", "BrowsePath", "BrowsePathTarget", "RelativePath", "RelativePathElement", "BrowsePathResult"]#, "ApplicationDescription", "EndpointDescription"
# many objects are defined as inheriting while inheriting ExtensionObjects while they do not so harcode those who really do
InheritExtensionObjects = ["UserIdentityToken", "NodeAttributes"]#"SignatureData"]


class Bit(object):
    def __init__(self):
        self.name = None
        self.idx = None
        self.container = None
        self.length = 1

    def __str__(self):
        return "(Bit: {}, container:{}, idx:{})".format(self.name, self.container, self.idx)
    __repr__ = __str__

class Struct(object):
    def __init__(self):
        self.name = None
        self.basetype = None
        self.doc = ""
        self.fields = []
        self.bits = {}
        self.needconstructor = None
        self.needoverride = False
        self.children = []
        self.parents = []
        self.extensionobject = False #used for struct which are not pure extension objects

    def get_field(self, name):
        for f in self.fields:
            if f.name == name:
                return f
        raise Exception("field not found: " + name)
    
    def __str__(self):
        return "Struct {}:{}".format(self.name, self.basetype)

    __repr__ = __str__


class Field(object):
    def __init__(self):
        self.name = None
        self.uatype = None
        self.length = None
        self.sourcetype = None
        self.switchfield = None
        self.switchvalue = None
        self.bitlength = 1 

    def __str__(self):
        return "Field {}({})".format(self.name, self.uatype)

    __repr__ = __str__

    def is_native_type(self):
        if self.uatype in ("Char", "SByte", "Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "Boolean", "Double", "Float", "Byte", "String", "CharArray", "ByteString"):
            return True
        return False

    def get_ctype(self):
        if self.uatype == "String":
            ty = "std::string"
        elif self.uatype == "CharArray":
            ty = "std::string"
        elif self.uatype == "Char":
            ty = "char"
        elif self.uatype == "SByte":
            ty = "char"
        elif self.uatype == "Int8":
            ty = "int8_t"
        elif self.uatype == "Int16":
            ty = "int16_t"
        elif self.uatype == "Int32":
            ty = "int32_t"
        elif self.uatype == "Int64":
            ty = "int64_t"
        elif self.uatype == "UInt8":
            ty = "uint8_t"
        elif self.uatype == "UInt16":
            ty = "uint16_t"
        elif self.uatype == "UInt32":
            ty = "uint32_t"
        elif self.uatype == "UInt64":
            ty = "uint64_t"
        elif self.uatype == "DateTime":
            ty = "OpcUa::DateTime"
        elif self.uatype == "Boolean":
            ty = "bool"
        elif self.uatype == "Double":
            ty = "double"
        elif self.uatype == "Float":
            ty = "float"
        elif self.uatype == "ByteString":
            ty = "OpcUa::ByteString"
        elif self.uatype == "Byte":
            ty = "uint8_t"
        else:
            ty = "OpcUa::" + self.uatype
        if self.length:
            ty = "std::vector<{}>".format(ty)
        return ty

class Enum(object):
    def __init__(self):
        self.name = None
        self.uatype = None
        self.values = []
        self.doc = ""

    def get_ctype(self):
        return "uint{}_t".format(self.uatype)

class EnumValue(object):
    def __init__(self):
        self.name = None
        self.value = None

class Model(object):
    def __init__(self):
        self.structs = []
        self.enums = []
        self.struct_list = []
        self.enum_list = []

    def get_struct(self, name):
        for struct in self.structs:
            if name == struct.name:
                return struct
        raise Exception("No struct named: " + str(name))

    def get_enum(self, name):
        for s in self.enums:
            if name == s.name:
                return s
        raise Exception("No enum named: " + str(name))




def reorder_structs(model):
    types = IgnoredStructs + IgnoredEnums + ["Bit", "Char", "CharArray", "Guid", "SByte", "Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "DateTime", "Boolean", "Double", "Float", "ByteString", "Byte", "StatusCode", "DiagnosticInfo", "String", "AttributeID"] + [enum.name for enum in model.enums] + ["VariableAccessLevel"]
    waiting = {}
    newstructs = []
    for s in model.structs:
        types.append(s.name)
        s.waitingfor = []
        ok = True
        for f in s.fields:
            if f.uatype not in types:
                if f.uatype in waiting.keys():
                    waiting[f.uatype].append(s)
                    s.waitingfor.append(f.uatype)
                else:
                    waiting[f.uatype] = [s]
                    s.waitingfor.append(f.uatype)
                ok = False
        if ok:
            newstructs.append(s)
            waitings = waiting.pop(s.name, None)
            if waitings:
                for s2 in waitings:
                    s2.waitingfor.remove(s.name)
                    if not s2.waitingfor:
                        newstructs.append(s2)
    if len(model.structs) != len(newstructs):
        print("Error while reordering structs, some structs could not be reinserted, had {} structs, we now have {} structs".format(len(model.structs), len(newstructs)))
        s1 = set(model.structs)
        s2 = set(newstructs)
        rest = s1 -s2
        print("Variant" in types)
        for s in s1-s2:
            print("{} is waiting for: {}".format(s, s.waitingfor))
        #print(s1 -s2)
        #print(waiting)
    model.structs = newstructs

def override_types(model):
    for struct in model.structs:
        for field in struct.fields:
            if field.name in OverrideTypes.keys():
                field.uatype = OverrideTypes[field.name]

def remove_duplicates(model):
    for struct in model.structs:
        fields = []
        names = []
        for field in struct.fields:
            if field.name not in names:
                names.append(field.name)
                fields.append(field)
        struct.fields = fields
    
def add_encoding_field(model):
    for struct in model.structs:
        newfields = []
        container = None
        idx = 0
        for field in struct.fields:
            if field.uatype in ("UInt6", "NodeIdType"):
                container = field.name
                b = Bit()
                b.name = field.name
                b.idx = 0
                b.container = container
                b.length = 6 
                idx = b.length
                struct.bits[b.name] = b

            if field.uatype == "Bit":
                if not container or idx > 7:
                    container = "Encoding"
                    idx = 0
                    f = Field()
                    f.sourcetype = field.sourcetype
                    f.name = "Encoding"
                    f.uatype = "UInt8"
                    newfields.append(f)

                b = Bit()
                b.name = field.name
                b.idx = idx
                b.container = container
                b.length = field.bitlength
                idx += field.bitlength
                struct.bits[b.name] = b
            else:
                newfields.append(field)
        struct.fields = newfields

def remove_vector_length(model):
    for struct in model.structs:
        new = []
        for field in struct.fields:
            if not field.name.startswith("NoOf"):
                new.append(field)
        struct.fields = new

def remove_body_length(model):
    for struct in model.structs:
        new = []
        for field in struct.fields:
            if not field.name == "BodyLength":
                new.append(field)
        struct.fields = new

#def remove_extensionobject_fields(model):
    #for obj in model.structs:
        #if obj.name.endswith("Request") or obj.name.endswith("Response"):
            #obj.fields = [el for el in obj.fields if el.name not in ("TypeId", "Body", "Encoding")]

def split_requests(model):
    structs = []
    for struct in model.structs:
        structtype = None
        if struct.name.endswith("Request") and not struct.name in ("MonitoredItemCreateRequest"):
            structtype = "Request"
        elif struct.name.endswith("Response") or struct.name == "ServiceFault":
            structtype = "Response"
        if structtype:
            #for field in struct.fields:
                #if field.name == "Encoding":
                    #struct.fields.remove(field)
                    #break
            #for field in struct.fields:
                #if field.name == "BodyLength":
                    #struct.fields.remove(field)
                    #break
            struct.needconstructor = True
            field = Field()
            field.name = "TypeId"
            field.uatype = "NodeId"
            struct.fields.insert(0, field)

        if structtype and not struct.name in NoSplitStruct:
            paramstruct = Struct()
            if structtype == "Request":
                basename = struct.name.replace("Request", "") + "Parameters"
                paramstruct.name = basename 
            else:
                basename = struct.name.replace("Response", "") + "Result"
                paramstruct.name = basename 
            paramstruct.fields = struct.fields[2:]
            paramstruct.bits = struct.bits

            struct.fields = struct.fields[:2]
            #struct.bits = {}
            structs.append(paramstruct)

            typeid = Field()
            typeid.name = "Parameters" 
            typeid.uatype = paramstruct.name 
            struct.fields.append(typeid)
        structs.append(struct)
    model.structs = structs


class Parser(object):
    def __init__(self, path):
        self.path = path
        self.model = None

    def parse(self):
        print("Parsing: ", self.path)
        self.model = Model()
        tree = ET.parse(self.path)
        root = tree.getroot()
        self.add_extension_object()
        for child in root:
            tag = child.tag[40:]
            if tag == "StructuredType":
                struct = self.parse_struct(child)
                if struct.name != "ExtensionObject":
                    self.model.structs.append(struct)
                    self.model.struct_list.append(struct.name)
            elif tag == "EnumeratedType":
                enum = self.parse_enum(child)
                self.model.enums.append(enum)
                self.model.enum_list.append(enum.name)
            #else:
                #print("Not implemented node type: " + tag + "\n")
        return self.model

    def add_extension_object(self):
        obj = Struct()
        obj.name = "ExtensionObject"
        f = Field()
        f.name = "TypeId"
        f.uatype = "NodeId"
        obj.fields.append(f)
        f = Field()
        f.name = "BinaryBody"
        f.uatype = "Bit"
        obj.fields.append(f)
        f = Field()
        f.name = "XmlBody"
        f.uatype = "Bit"
        obj.fields.append(f)
        f = Field()
        f.name = "Body"
        f.uatype = "ByteString"
        f.switchfield = "BinaryBody"
        obj.fields.append(f)
        self.model.struct_list.append(obj.name)

        self.model.structs.append(obj)

    def parse_struct(self, child):
        tag = child.tag[40:]
        struct = Struct()
        for key, val in child.attrib.items():
            if key == "Name":
                struct.name = val
            elif key == "BaseType":
                if ":" in val:
                    prefix, val = val.split(":")
                struct.basetype = val
                tmp = struct
                while tmp.basetype:
                    struct.parents.append(tmp.basetype)
                    tmp = self.model.get_struct(tmp.basetype)
            else:
                print("Error unknown key: ", key)
        for el in child:
            tag = el.tag[40:]
            if tag == "Field":
                field = Field()
                for key, val in el.attrib.items():
                    if key == "Name":
                        field.name = val
                    elif key == "TypeName":
                        field.uatype = val.split(":")[1]
                    elif key == "LengthField":
                        field.length = val
                    elif key == "SourceType":
                        field.sourcetype = val
                    elif key == "SwitchField":
                        field.switchfield = val
                    elif key == "SwitchValue":
                        field.switchvalue = val
                    elif key == "Length":
                        field.bitlength = int(val)
                    else:
                        print("Uknown field item: ", struct.name, key) 

                struct.fields.append(field)
            elif tag == "Documentation":
                struct.doc = el.text
            else:
                print("Uknown tag: ", tag)

        return struct

    def parse_enum(self, child):
        tag = child.tag[40:]
        enum = Enum()
        for k, v in child.items():
            if k == "Name":
                enum.name = v
            elif k == "LengthInBits":
                enum.uatype = "UInt" + v
            else:
                print("Unknown attr for enum: ", k)
        for el in child:
            tag = el.tag[40:]
            if tag == "EnumeratedValue":
                ev = EnumValue()
                for k, v in el.attrib.items():
                    if k == "Name":
                        ev.name = v
                    elif k == "Value":
                        ev.value = v
                    else:
                        print("Uknown field attrib: ", k) 
                enum.values.append(ev)
            elif tag == "Documentation":
                enum.doc = el.text
            else:
                print("Unknown enum tag: ", tag)
        return enum


#"def reorder_extobjects(model):
    #ext = model.get_struct("ExtensionObject")
    #print(ext)
    #typeid = ext.fields[4]
    #ext.fields.remove(typeid)
    #ext.fields.insert(0, typeid)

def add_basetype_members(model):
    for struct in model.structs:
        if not struct.basetype:
            continue
        emptystruct = False
        if len(struct.fields) == 0:
            emptystruct = True
        if not emptystruct and struct.basetype in ("ExtensionObject") and not struct.name in InheritExtensionObjects:
        #if struct.name in NoInherit or struct.name.endswith("Request") or struct.name.endswith("Response") or struct.name.endswith("Description"):
            struct.parents.remove(struct.basetype)
            struct.basetype = None
            continue
        base = model.get_struct(struct.basetype)
        #if struct.basetype == "ExtensionObject" and len(struct.fields) != 0:
        #if struct.basetype == "ExtensionObject" and len(struct.fields) != 0:
            #if struc
            #for f in base.fields:
                #if f.name == "TypeId":
                    #f2 = copy(f)
                    #f2.switchfield = None
                    #struct.fields.insert(0, f2)
                    #break
            #continue
        for name, bit in base.bits.items():
            struct.bits[name] = bit
        for idx, field in enumerate(base.fields):
            field = copy(field)
            if field.name == "Body" and not emptystruct:
                #print("Field is names Body", struct.name, field.name)
                struct.extensionobject = True
                field.name = "BodyLength"
                field.uatype = "Int32"
                field.length = None
                field.switchfield = None
                #print("Field is names Body 2", struct.name, field.name)
            #HACK EXTENSIONOBJECT
            #if base.name == "ExtensionObject":
                #continue
                #if field.uatype == "Bit":
                    #continue
                #if field.name == "Body":
                    #continue
                #if field.name == "TypeId":
                    #field.switchfield = None
            #END HACK
            if not field.sourcetype:
                field.sourcetype = base.name
            struct.fields.insert(idx, field)





