
"""
DO NOT EDIT THIS FILE!
It is automatically generated from opcfoundation.org schemas.
"""

from opcua import uaprotocol as ua

false = False #FIXME
true = True #FIXME

def create_standard_address_space_Part13(server):
  
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11187")
    node.BrowseName = ua.QualifiedName.from_string("AggregateConfigurationType")
    node.NodeClass = ua.NodeClass.ObjectType
    node.ParentNodeId = ua.NodeId.from_string("i=58")
    node.ReferenceTypeId = ua.NodeId.from_string("i=45")
    attrs = ua.ObjectTypeAttributes()
    attrs.DisplayName = ua.LocalizedText("AggregateConfigurationType")
    attrs.IsAbstract = false
    node.Attributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=46")
    ref.SourceNodeId = ua.NodeId.from_string("i=11187")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=11188")
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=46")
    ref.SourceNodeId = ua.NodeId.from_string("i=11187")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=11189")
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=46")
    ref.SourceNodeId = ua.NodeId.from_string("i=11187")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=11190")
    refs.append(ref)
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=46")
    ref.SourceNodeId = ua.NodeId.from_string("i=11187")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=11191")
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11188")
    node.BrowseName = ua.QualifiedName.from_string("TreatUncertainAsBad")
    node.NodeClass = ua.NodeClass.Variable
    node.ParentNodeId = ua.NodeId.from_string("i=11187")
    node.ReferenceTypeId = ua.NodeId.from_string("i=46")
    node.TypeDefinition = ua.NodeId.from_string("i=68")
    attrs = ua.VariableAttributes()
    attrs.DisplayName = ua.LocalizedText("TreatUncertainAsBad")
    attrs.Type = ua.ObjectIds.Boolean
    attrs.Rank = -1
    node.Attributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=37")
    ref.SourceNodeId = ua.NodeId.from_string("i=11188")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=78")
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11189")
    node.BrowseName = ua.QualifiedName.from_string("PercentDataBad")
    node.NodeClass = ua.NodeClass.Variable
    node.ParentNodeId = ua.NodeId.from_string("i=11187")
    node.ReferenceTypeId = ua.NodeId.from_string("i=46")
    node.TypeDefinition = ua.NodeId.from_string("i=68")
    attrs = ua.VariableAttributes()
    attrs.DisplayName = ua.LocalizedText("PercentDataBad")
    attrs.Type = ua.ObjectIds.Byte
    attrs.Rank = -1
    node.Attributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=37")
    ref.SourceNodeId = ua.NodeId.from_string("i=11189")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=78")
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11190")
    node.BrowseName = ua.QualifiedName.from_string("PercentDataGood")
    node.NodeClass = ua.NodeClass.Variable
    node.ParentNodeId = ua.NodeId.from_string("i=11187")
    node.ReferenceTypeId = ua.NodeId.from_string("i=46")
    node.TypeDefinition = ua.NodeId.from_string("i=68")
    attrs = ua.VariableAttributes()
    attrs.DisplayName = ua.LocalizedText("PercentDataGood")
    attrs.Type = ua.ObjectIds.Byte
    attrs.Rank = -1
    node.Attributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=37")
    ref.SourceNodeId = ua.NodeId.from_string("i=11190")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=78")
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11191")
    node.BrowseName = ua.QualifiedName.from_string("UseSlopedExtrapolation")
    node.NodeClass = ua.NodeClass.Variable
    node.ParentNodeId = ua.NodeId.from_string("i=11187")
    node.ReferenceTypeId = ua.NodeId.from_string("i=46")
    node.TypeDefinition = ua.NodeId.from_string("i=68")
    attrs = ua.VariableAttributes()
    attrs.DisplayName = ua.LocalizedText("UseSlopedExtrapolation")
    attrs.Type = ua.ObjectIds.Boolean
    attrs.Rank = -1
    node.Attributes = attrs
    server.add_nodes([node])
    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = true
    ref.ReferenceTypeId = ua.NodeId.from_string("i=37")
    ref.SourceNodeId = ua.NodeId.from_string("i=11191")
    ref.NodeClass = ua.NodeClass.DataType
    ref.TargetNodeId = ua.NodeId.from_string("i=78")
    refs.append(ref)
    server.add_references(refs)
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2341")
    node.BrowseName = ua.QualifiedName.from_string("Interpolative")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("At the beginning of each interval, retrieve the calculated value from the data points on either side of the requested timestamp.")
    attrs.DisplayName = ua.LocalizedText("Interpolative")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2342")
    node.BrowseName = ua.QualifiedName.from_string("Average")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the average value of the data over the interval.")
    attrs.DisplayName = ua.LocalizedText("Average")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2343")
    node.BrowseName = ua.QualifiedName.from_string("TimeAverage")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the time weighted average data over the interval using Interpolated Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("TimeAverage")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11285")
    node.BrowseName = ua.QualifiedName.from_string("TimeAverage2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the time weighted average data over the interval using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("TimeAverage2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2344")
    node.BrowseName = ua.QualifiedName.from_string("Total")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the total (time integral) of the data over the interval using Interpolated Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("Total")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11304")
    node.BrowseName = ua.QualifiedName.from_string("Total2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the total (time integral) of the data over the interval using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("Total2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2346")
    node.BrowseName = ua.QualifiedName.from_string("Minimum")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the minimum raw value in the interval with the timestamp of the start of the interval.")
    attrs.DisplayName = ua.LocalizedText("Minimum")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2347")
    node.BrowseName = ua.QualifiedName.from_string("Maximum")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the maximum raw value in the interval with the timestamp of the start of the interval.")
    attrs.DisplayName = ua.LocalizedText("Maximum")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2348")
    node.BrowseName = ua.QualifiedName.from_string("MinimumActualTime")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the minimum value in the interval and the Timestamp of the minimum value.")
    attrs.DisplayName = ua.LocalizedText("MinimumActualTime")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2349")
    node.BrowseName = ua.QualifiedName.from_string("MaximumActualTime")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the maximum value in the interval and the Timestamp of the maximum value.")
    attrs.DisplayName = ua.LocalizedText("MaximumActualTime")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2350")
    node.BrowseName = ua.QualifiedName.from_string("Range")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the difference between the minimum and maximum Value over the interval.")
    attrs.DisplayName = ua.LocalizedText("Range")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11286")
    node.BrowseName = ua.QualifiedName.from_string("Minimum2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the minimum value in the interval including the Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("Minimum2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11287")
    node.BrowseName = ua.QualifiedName.from_string("Maximum2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the maximum value in the interval including the Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("Maximum2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11305")
    node.BrowseName = ua.QualifiedName.from_string("MinimumActualTime2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the minimum value with the actual timestamp including the Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("MinimumActualTime2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11306")
    node.BrowseName = ua.QualifiedName.from_string("MaximumActualTime2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the maximum value with the actual timestamp including the Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("MaximumActualTime2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11288")
    node.BrowseName = ua.QualifiedName.from_string("Range2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the difference between the Minimum2 and Maximum2 value over the interval.")
    attrs.DisplayName = ua.LocalizedText("Range2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2351")
    node.BrowseName = ua.QualifiedName.from_string("AnnotationCount")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the number of Annotations in the interval.")
    attrs.DisplayName = ua.LocalizedText("AnnotationCount")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2352")
    node.BrowseName = ua.QualifiedName.from_string("Count")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the number of raw values over the interval.")
    attrs.DisplayName = ua.LocalizedText("Count")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11307")
    node.BrowseName = ua.QualifiedName.from_string("DurationInStateZero")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the time a Boolean or numeric was in a zero state using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("DurationInStateZero")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11308")
    node.BrowseName = ua.QualifiedName.from_string("DurationInStateNonZero")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the time a Boolean or numeric was in a non-zero state using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("DurationInStateNonZero")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2355")
    node.BrowseName = ua.QualifiedName.from_string("NumberOfTransitions")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the number of changes between zero and non-zero that a Boolean or Numeric value experienced in the interval.")
    attrs.DisplayName = ua.LocalizedText("NumberOfTransitions")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2357")
    node.BrowseName = ua.QualifiedName.from_string("Start")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the value at the beginning of the interval using Interpolated Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("Start")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2358")
    node.BrowseName = ua.QualifiedName.from_string("End")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the value at the end of the interval using Interpolated Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("End")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2359")
    node.BrowseName = ua.QualifiedName.from_string("Delta")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the difference between the Start and End value in the interval.")
    attrs.DisplayName = ua.LocalizedText("Delta")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11505")
    node.BrowseName = ua.QualifiedName.from_string("StartBound")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the value at the beginning of the interval using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("StartBound")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11506")
    node.BrowseName = ua.QualifiedName.from_string("EndBound")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the value at the end of the interval using Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("EndBound")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11507")
    node.BrowseName = ua.QualifiedName.from_string("DeltaBounds")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the difference between the StartBound and EndBound value in the interval.")
    attrs.DisplayName = ua.LocalizedText("DeltaBounds")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2360")
    node.BrowseName = ua.QualifiedName.from_string("DurationGood")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the total duration of time in the interval during which the data is good.")
    attrs.DisplayName = ua.LocalizedText("DurationGood")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2361")
    node.BrowseName = ua.QualifiedName.from_string("DurationBad")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the total duration of time in the interval during which the data is bad.")
    attrs.DisplayName = ua.LocalizedText("DurationBad")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2362")
    node.BrowseName = ua.QualifiedName.from_string("PercentGood")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the percent of data (0 to 100) in the interval which has a good StatusCode.")
    attrs.DisplayName = ua.LocalizedText("PercentGood")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2363")
    node.BrowseName = ua.QualifiedName.from_string("PercentBad")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the percent of data (0 to 100) in the interval which has a bad StatusCode.")
    attrs.DisplayName = ua.LocalizedText("PercentBad")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=2364")
    node.BrowseName = ua.QualifiedName.from_string("WorstQuality")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the worst StatusCode of data in the interval.")
    attrs.DisplayName = ua.LocalizedText("WorstQuality")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11292")
    node.BrowseName = ua.QualifiedName.from_string("WorstQuality2")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the worst StatusCode of data in the interval including the Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("WorstQuality2")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11426")
    node.BrowseName = ua.QualifiedName.from_string("StandardDeviationSample")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the standard deviation for the interval for a sample of the population (n-1).")
    attrs.DisplayName = ua.LocalizedText("StandardDeviationSample")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11427")
    node.BrowseName = ua.QualifiedName.from_string("StandardDeviationPopulation")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the standard deviation for the interval for a complete population (n) which includes Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("StandardDeviationPopulation")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11428")
    node.BrowseName = ua.QualifiedName.from_string("VarianceSample")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the variance for the interval as calculated by the StandardDeviationSample.")
    attrs.DisplayName = ua.LocalizedText("VarianceSample")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
   
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = ua.NodeId.from_string("i=11429")
    node.BrowseName = ua.QualifiedName.from_string("VariancePopulation")
    node.NodeClass = ua.NodeClass.Object
    node.TypeDefinition = ua.NodeId.from_string("i=2340")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText("Retrieve the variance for the interval as calculated by the StandardDeviationPopulation which includes Simple Bounding Values.")
    attrs.DisplayName = ua.LocalizedText("VariancePopulation")
    attrs.EventNotifier = 0
    node.Attributes = attrs
    server.add_nodes([node])
