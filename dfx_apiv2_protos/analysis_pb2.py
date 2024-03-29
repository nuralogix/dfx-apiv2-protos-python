# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='analysis.proto',
  package='dfx.proto.analysis',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x61nalysis.proto\x12\x12\x64\x66x.proto.analysis\"\x14\n\x12ListSignalsRequest\"+\n\x13ListSignalsResponse\x12\x14\n\x0csignal_names\x18\x01 \x03(\t\".\n\x16\x44\x65scribeSignalsRequest\x12\x14\n\x0csignal_names\x18\x01 \x03(\t\"\xaf\x03\n\x17\x44\x65scribeSignalsResponse\x12P\n\x0esignal_details\x18\x01 \x03(\x0b\x32\x38.dfx.proto.analysis.DescribeSignalsResponse.SignalDetail\x1a\xc1\x02\n\x0cSignalDetail\x12\x13\n\x0bsignal_name\x18\x01 \x01(\t\x12\x19\n\x11initial_delay_sec\x18\x02 \x01(\r\x12\x15\n\rmodel_min_sec\x18\x03 \x01(\r\x12\x0f\n\x07min_fps\x18\x04 \x01(\r\x12\x12\n\ntarget_fps\x18\x05 \x01(\r\x12\x15\n\rdefault_model\x18\x06 \x01(\t\x12\x18\n\x10\x61vailable_models\x18\x07 \x03(\t\x12_\n\x0fsignal_channels\x18\x08 \x03(\x0b\x32\x46.dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.SignalChannel\x1a\x33\n\rSignalChannel\x12\x0b\n\x03roi\x18\x01 \x01(\t\x12\x15\n\rchannel_names\x18\x02 \x03(\t\"\xc1\x03\n\x12\x41nalyzeDataRequest\x12\x0b\n\x03\x66ps\x18\x01 \x01(\r\x12\x12\n\ntimestamps\x18\x02 \x03(\x02\x12>\n\x07signals\x18\x03 \x03(\x0b\x32-.dfx.proto.analysis.AnalyzeDataRequest.Signal\x12@\n\x08\x63hannels\x18\x04 \x03(\x0b\x32..dfx.proto.analysis.AnalyzeDataRequest.Channel\x1a\x62\n\x06Signal\x12\x13\n\x0bsignal_name\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x12\n\nresolution\x18\x03 \x01(\r\x12\x1b\n\x13\x65stimate_confidence\x18\x04 \x01(\x08\x1a\xa3\x01\n\x07\x43hannel\x12\x0b\n\x03roi\x18\x01 \x01(\t\x12\x12\n\nnum_frames\x18\x02 \x01(\r\x12H\n\x08\x64\x61tasets\x18\x03 \x03(\x0b\x32\x36.dfx.proto.analysis.AnalyzeDataRequest.Channel.Dataset\x1a-\n\x07\x44\x61taset\x12\x14\n\x0c\x63hannel_name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x02\"\xba\x01\n\x13\x41nalyzeDataResponse\x12?\n\x07results\x18\x01 \x03(\x0b\x32..dfx.proto.analysis.AnalyzeDataResponse.Result\x1a\x62\n\x06Result\x12\x13\n\x0bsignal_name\x18\x01 \x01(\t\x12\x0b\n\x03roi\x18\x02 \x01(\t\x12\x14\n\x0c\x63hannel_name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x02\x12\x12\n\nconfidence\x18\x05 \x03(\x02\x32\xbc\x02\n\x08\x41nalysis\x12`\n\x0bListSignals\x12&.dfx.proto.analysis.ListSignalsRequest\x1a\'.dfx.proto.analysis.ListSignalsResponse\"\x00\x12l\n\x0f\x44\x65scribeSignals\x12*.dfx.proto.analysis.DescribeSignalsRequest\x1a+.dfx.proto.analysis.DescribeSignalsResponse\"\x00\x12`\n\x0b\x41nalyzeData\x12&.dfx.proto.analysis.AnalyzeDataRequest\x1a\'.dfx.proto.analysis.AnalyzeDataResponse\"\x00\x62\x06proto3'
)




_LISTSIGNALSREQUEST = _descriptor.Descriptor(
  name='ListSignalsRequest',
  full_name='dfx.proto.analysis.ListSignalsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=58,
)


_LISTSIGNALSRESPONSE = _descriptor.Descriptor(
  name='ListSignalsResponse',
  full_name='dfx.proto.analysis.ListSignalsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_names', full_name='dfx.proto.analysis.ListSignalsResponse.signal_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=103,
)


_DESCRIBESIGNALSREQUEST = _descriptor.Descriptor(
  name='DescribeSignalsRequest',
  full_name='dfx.proto.analysis.DescribeSignalsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_names', full_name='dfx.proto.analysis.DescribeSignalsRequest.signal_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=151,
)


_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL_SIGNALCHANNEL = _descriptor.Descriptor(
  name='SignalChannel',
  full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.SignalChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roi', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.SignalChannel.roi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_names', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.SignalChannel.channel_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=585,
)

_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL = _descriptor.Descriptor(
  name='SignalDetail',
  full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_name', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.signal_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_delay_sec', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.initial_delay_sec', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_min_sec', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.model_min_sec', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_fps', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.min_fps', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_fps', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.target_fps', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_model', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.default_model', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available_models', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.available_models', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal_channels', full_name='dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.signal_channels', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL_SIGNALCHANNEL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=585,
)

_DESCRIBESIGNALSRESPONSE = _descriptor.Descriptor(
  name='DescribeSignalsResponse',
  full_name='dfx.proto.analysis.DescribeSignalsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_details', full_name='dfx.proto.analysis.DescribeSignalsResponse.signal_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=585,
)


_ANALYZEDATAREQUEST_SIGNAL = _descriptor.Descriptor(
  name='Signal',
  full_name='dfx.proto.analysis.AnalyzeDataRequest.Signal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_name', full_name='dfx.proto.analysis.AnalyzeDataRequest.Signal.signal_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='dfx.proto.analysis.AnalyzeDataRequest.Signal.model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='dfx.proto.analysis.AnalyzeDataRequest.Signal.resolution', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estimate_confidence', full_name='dfx.proto.analysis.AnalyzeDataRequest.Signal.estimate_confidence', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=871,
)

_ANALYZEDATAREQUEST_CHANNEL_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.Dataset.channel_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.Dataset.data', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=992,
  serialized_end=1037,
)

_ANALYZEDATAREQUEST_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roi', full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.roi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_frames', full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.num_frames', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datasets', full_name='dfx.proto.analysis.AnalyzeDataRequest.Channel.datasets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZEDATAREQUEST_CHANNEL_DATASET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=874,
  serialized_end=1037,
)

_ANALYZEDATAREQUEST = _descriptor.Descriptor(
  name='AnalyzeDataRequest',
  full_name='dfx.proto.analysis.AnalyzeDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fps', full_name='dfx.proto.analysis.AnalyzeDataRequest.fps', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamps', full_name='dfx.proto.analysis.AnalyzeDataRequest.timestamps', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signals', full_name='dfx.proto.analysis.AnalyzeDataRequest.signals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='dfx.proto.analysis.AnalyzeDataRequest.channels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZEDATAREQUEST_SIGNAL, _ANALYZEDATAREQUEST_CHANNEL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=1037,
)


_ANALYZEDATARESPONSE_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='dfx.proto.analysis.AnalyzeDataResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signal_name', full_name='dfx.proto.analysis.AnalyzeDataResponse.Result.signal_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roi', full_name='dfx.proto.analysis.AnalyzeDataResponse.Result.roi', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='dfx.proto.analysis.AnalyzeDataResponse.Result.channel_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='dfx.proto.analysis.AnalyzeDataResponse.Result.data', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='dfx.proto.analysis.AnalyzeDataResponse.Result.confidence', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1226,
)

_ANALYZEDATARESPONSE = _descriptor.Descriptor(
  name='AnalyzeDataResponse',
  full_name='dfx.proto.analysis.AnalyzeDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='dfx.proto.analysis.AnalyzeDataResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZEDATARESPONSE_RESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1226,
)

_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL_SIGNALCHANNEL.containing_type = _DESCRIBESIGNALSRESPONSE_SIGNALDETAIL
_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL.fields_by_name['signal_channels'].message_type = _DESCRIBESIGNALSRESPONSE_SIGNALDETAIL_SIGNALCHANNEL
_DESCRIBESIGNALSRESPONSE_SIGNALDETAIL.containing_type = _DESCRIBESIGNALSRESPONSE
_DESCRIBESIGNALSRESPONSE.fields_by_name['signal_details'].message_type = _DESCRIBESIGNALSRESPONSE_SIGNALDETAIL
_ANALYZEDATAREQUEST_SIGNAL.containing_type = _ANALYZEDATAREQUEST
_ANALYZEDATAREQUEST_CHANNEL_DATASET.containing_type = _ANALYZEDATAREQUEST_CHANNEL
_ANALYZEDATAREQUEST_CHANNEL.fields_by_name['datasets'].message_type = _ANALYZEDATAREQUEST_CHANNEL_DATASET
_ANALYZEDATAREQUEST_CHANNEL.containing_type = _ANALYZEDATAREQUEST
_ANALYZEDATAREQUEST.fields_by_name['signals'].message_type = _ANALYZEDATAREQUEST_SIGNAL
_ANALYZEDATAREQUEST.fields_by_name['channels'].message_type = _ANALYZEDATAREQUEST_CHANNEL
_ANALYZEDATARESPONSE_RESULT.containing_type = _ANALYZEDATARESPONSE
_ANALYZEDATARESPONSE.fields_by_name['results'].message_type = _ANALYZEDATARESPONSE_RESULT
DESCRIPTOR.message_types_by_name['ListSignalsRequest'] = _LISTSIGNALSREQUEST
DESCRIPTOR.message_types_by_name['ListSignalsResponse'] = _LISTSIGNALSRESPONSE
DESCRIPTOR.message_types_by_name['DescribeSignalsRequest'] = _DESCRIBESIGNALSREQUEST
DESCRIPTOR.message_types_by_name['DescribeSignalsResponse'] = _DESCRIBESIGNALSRESPONSE
DESCRIPTOR.message_types_by_name['AnalyzeDataRequest'] = _ANALYZEDATAREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeDataResponse'] = _ANALYZEDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSignalsRequest = _reflection.GeneratedProtocolMessageType('ListSignalsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSIGNALSREQUEST,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.ListSignalsRequest)
  })
_sym_db.RegisterMessage(ListSignalsRequest)

ListSignalsResponse = _reflection.GeneratedProtocolMessageType('ListSignalsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSIGNALSRESPONSE,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.ListSignalsResponse)
  })
_sym_db.RegisterMessage(ListSignalsResponse)

DescribeSignalsRequest = _reflection.GeneratedProtocolMessageType('DescribeSignalsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBESIGNALSREQUEST,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.DescribeSignalsRequest)
  })
_sym_db.RegisterMessage(DescribeSignalsRequest)

DescribeSignalsResponse = _reflection.GeneratedProtocolMessageType('DescribeSignalsResponse', (_message.Message,), {

  'SignalDetail' : _reflection.GeneratedProtocolMessageType('SignalDetail', (_message.Message,), {

    'SignalChannel' : _reflection.GeneratedProtocolMessageType('SignalChannel', (_message.Message,), {
      'DESCRIPTOR' : _DESCRIBESIGNALSRESPONSE_SIGNALDETAIL_SIGNALCHANNEL,
      '__module__' : 'analysis_pb2'
      # @@protoc_insertion_point(class_scope:dfx.proto.analysis.DescribeSignalsResponse.SignalDetail.SignalChannel)
      })
    ,
    'DESCRIPTOR' : _DESCRIBESIGNALSRESPONSE_SIGNALDETAIL,
    '__module__' : 'analysis_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.analysis.DescribeSignalsResponse.SignalDetail)
    })
  ,
  'DESCRIPTOR' : _DESCRIBESIGNALSRESPONSE,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.DescribeSignalsResponse)
  })
_sym_db.RegisterMessage(DescribeSignalsResponse)
_sym_db.RegisterMessage(DescribeSignalsResponse.SignalDetail)
_sym_db.RegisterMessage(DescribeSignalsResponse.SignalDetail.SignalChannel)

AnalyzeDataRequest = _reflection.GeneratedProtocolMessageType('AnalyzeDataRequest', (_message.Message,), {

  'Signal' : _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {
    'DESCRIPTOR' : _ANALYZEDATAREQUEST_SIGNAL,
    '__module__' : 'analysis_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataRequest.Signal)
    })
  ,

  'Channel' : _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {

    'Dataset' : _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
      'DESCRIPTOR' : _ANALYZEDATAREQUEST_CHANNEL_DATASET,
      '__module__' : 'analysis_pb2'
      # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataRequest.Channel.Dataset)
      })
    ,
    'DESCRIPTOR' : _ANALYZEDATAREQUEST_CHANNEL,
    '__module__' : 'analysis_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataRequest.Channel)
    })
  ,
  'DESCRIPTOR' : _ANALYZEDATAREQUEST,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataRequest)
  })
_sym_db.RegisterMessage(AnalyzeDataRequest)
_sym_db.RegisterMessage(AnalyzeDataRequest.Signal)
_sym_db.RegisterMessage(AnalyzeDataRequest.Channel)
_sym_db.RegisterMessage(AnalyzeDataRequest.Channel.Dataset)

AnalyzeDataResponse = _reflection.GeneratedProtocolMessageType('AnalyzeDataResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _ANALYZEDATARESPONSE_RESULT,
    '__module__' : 'analysis_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataResponse.Result)
    })
  ,
  'DESCRIPTOR' : _ANALYZEDATARESPONSE,
  '__module__' : 'analysis_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.analysis.AnalyzeDataResponse)
  })
_sym_db.RegisterMessage(AnalyzeDataResponse)
_sym_db.RegisterMessage(AnalyzeDataResponse.Result)



_ANALYSIS = _descriptor.ServiceDescriptor(
  name='Analysis',
  full_name='dfx.proto.analysis.Analysis',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1229,
  serialized_end=1545,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListSignals',
    full_name='dfx.proto.analysis.Analysis.ListSignals',
    index=0,
    containing_service=None,
    input_type=_LISTSIGNALSREQUEST,
    output_type=_LISTSIGNALSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeSignals',
    full_name='dfx.proto.analysis.Analysis.DescribeSignals',
    index=1,
    containing_service=None,
    input_type=_DESCRIBESIGNALSREQUEST,
    output_type=_DESCRIBESIGNALSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AnalyzeData',
    full_name='dfx.proto.analysis.Analysis.AnalyzeData',
    index=2,
    containing_service=None,
    input_type=_ANALYZEDATAREQUEST,
    output_type=_ANALYZEDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYSIS)

DESCRIPTOR.services_by_name['Analysis'] = _ANALYSIS

# @@protoc_insertion_point(module_scope)
