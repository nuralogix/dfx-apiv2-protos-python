# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meta.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='meta.proto',
  package='dfx.proto.meta',
  syntax='proto3',
  serialized_options=b'\n\020ai.nuralogix.dfxB\004Meta\370\001\001',
  serialized_pb=b'\n\nmeta.proto\x12\x0e\x64\x66x.proto.meta\"\xd6\x01\n\rUpdateRequest\x12\x39\n\x06Params\x18\x01 \x01(\x0b\x32).dfx.proto.meta.UpdateRequest.ParamValues\x12\x39\n\x06Values\x18\x02 \x03(\x0b\x32).dfx.proto.meta.UpdateRequest.ValuesEntry\x1a \n\x0bParamValues\x12\x11\n\tNamespace\x18\x01 \x01(\t\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x10\n\x0eUpdateResponse\"\xcb\x01\n\x0fRetrieveRequest\x12;\n\x06Params\x18\x01 \x01(\x0b\x32+.dfx.proto.meta.RetrieveRequest.ParamValues\x12:\n\x05Query\x18\x02 \x01(\x0b\x32+.dfx.proto.meta.RetrieveRequest.QueryValues\x1a \n\x0bParamValues\x12\x11\n\tNamespace\x18\x01 \x01(\t\x1a\x1d\n\x0bQueryValues\x12\x0e\n\x06\x46ields\x18\x01 \x01(\t\"\x7f\n\x10RetrieveResponse\x12<\n\x06Values\x18\x01 \x03(\x0b\x32,.dfx.proto.meta.RetrieveResponse.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf7\x01\n\x15RetrieveByTypeRequest\x12\x41\n\x06Params\x18\x01 \x01(\x0b\x32\x31.dfx.proto.meta.RetrieveByTypeRequest.ParamValues\x12@\n\x05Query\x18\x02 \x01(\x0b\x32\x31.dfx.proto.meta.RetrieveByTypeRequest.QueryValues\x1a:\n\x0bParamValues\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\n\n\x02ID\x18\x02 \x01(\t\x12\x11\n\tNamespace\x18\x03 \x01(\t\x1a\x1d\n\x0bQueryValues\x12\x0e\n\x06\x46ields\x18\x01 \x01(\t\"\x8b\x01\n\x16RetrieveByTypeResponse\x12\x42\n\x06Values\x18\x01 \x03(\x0b\x32\x32.dfx.proto.meta.RetrieveByTypeResponse.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x02\n\x13UpdateByTypeRequest\x12?\n\x06Params\x18\x01 \x01(\x0b\x32/.dfx.proto.meta.UpdateByTypeRequest.ParamValues\x12?\n\x06Values\x18\x02 \x03(\x0b\x32/.dfx.proto.meta.UpdateByTypeRequest.ValuesEntry\x1a:\n\x0bParamValues\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\n\n\x02ID\x18\x02 \x01(\t\x12\x11\n\tNamespace\x18\x03 \x01(\t\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x16\n\x14UpdateByTypeResponse2\xe6\x02\n\x08Services\x12O\n\x08Retrieve\x12\x1f.dfx.proto.meta.RetrieveRequest\x1a .dfx.proto.meta.RetrieveResponse\"\x00\x12\x61\n\x0eRetrieveByType\x12%.dfx.proto.meta.RetrieveByTypeRequest\x1a&.dfx.proto.meta.RetrieveByTypeResponse\"\x00\x12I\n\x06Update\x12\x1d.dfx.proto.meta.UpdateRequest\x1a\x1e.dfx.proto.meta.UpdateResponse\"\x00\x12[\n\x0cUpdateByType\x12#.dfx.proto.meta.UpdateByTypeRequest\x1a$.dfx.proto.meta.UpdateByTypeResponse\"\x00\x42\x1b\n\x10\x61i.nuralogix.dfxB\x04Meta\xf8\x01\x01\x62\x06proto3'
)




_UPDATEREQUEST_PARAMVALUES = _descriptor.Descriptor(
  name='ParamValues',
  full_name='dfx.proto.meta.UpdateRequest.ParamValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Namespace', full_name='dfx.proto.meta.UpdateRequest.ParamValues.Namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=166,
  serialized_end=198,
)

_UPDATEREQUEST_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='dfx.proto.meta.UpdateRequest.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfx.proto.meta.UpdateRequest.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfx.proto.meta.UpdateRequest.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=245,
)

_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='dfx.proto.meta.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Params', full_name='dfx.proto.meta.UpdateRequest.Params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Values', full_name='dfx.proto.meta.UpdateRequest.Values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEREQUEST_PARAMVALUES, _UPDATEREQUEST_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=245,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='dfx.proto.meta.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=247,
  serialized_end=263,
)


_RETRIEVEREQUEST_PARAMVALUES = _descriptor.Descriptor(
  name='ParamValues',
  full_name='dfx.proto.meta.RetrieveRequest.ParamValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Namespace', full_name='dfx.proto.meta.RetrieveRequest.ParamValues.Namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=166,
  serialized_end=198,
)

_RETRIEVEREQUEST_QUERYVALUES = _descriptor.Descriptor(
  name='QueryValues',
  full_name='dfx.proto.meta.RetrieveRequest.QueryValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Fields', full_name='dfx.proto.meta.RetrieveRequest.QueryValues.Fields', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=440,
  serialized_end=469,
)

_RETRIEVEREQUEST = _descriptor.Descriptor(
  name='RetrieveRequest',
  full_name='dfx.proto.meta.RetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Params', full_name='dfx.proto.meta.RetrieveRequest.Params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Query', full_name='dfx.proto.meta.RetrieveRequest.Query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RETRIEVEREQUEST_PARAMVALUES, _RETRIEVEREQUEST_QUERYVALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=469,
)


_RETRIEVERESPONSE_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='dfx.proto.meta.RetrieveResponse.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfx.proto.meta.RetrieveResponse.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfx.proto.meta.RetrieveResponse.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=245,
)

_RETRIEVERESPONSE = _descriptor.Descriptor(
  name='RetrieveResponse',
  full_name='dfx.proto.meta.RetrieveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Values', full_name='dfx.proto.meta.RetrieveResponse.Values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RETRIEVERESPONSE_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=598,
)


_RETRIEVEBYTYPEREQUEST_PARAMVALUES = _descriptor.Descriptor(
  name='ParamValues',
  full_name='dfx.proto.meta.RetrieveByTypeRequest.ParamValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='dfx.proto.meta.RetrieveByTypeRequest.ParamValues.Type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ID', full_name='dfx.proto.meta.RetrieveByTypeRequest.ParamValues.ID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Namespace', full_name='dfx.proto.meta.RetrieveByTypeRequest.ParamValues.Namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=759,
  serialized_end=817,
)

_RETRIEVEBYTYPEREQUEST_QUERYVALUES = _descriptor.Descriptor(
  name='QueryValues',
  full_name='dfx.proto.meta.RetrieveByTypeRequest.QueryValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Fields', full_name='dfx.proto.meta.RetrieveByTypeRequest.QueryValues.Fields', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=440,
  serialized_end=469,
)

_RETRIEVEBYTYPEREQUEST = _descriptor.Descriptor(
  name='RetrieveByTypeRequest',
  full_name='dfx.proto.meta.RetrieveByTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Params', full_name='dfx.proto.meta.RetrieveByTypeRequest.Params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Query', full_name='dfx.proto.meta.RetrieveByTypeRequest.Query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RETRIEVEBYTYPEREQUEST_PARAMVALUES, _RETRIEVEBYTYPEREQUEST_QUERYVALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=848,
)


_RETRIEVEBYTYPERESPONSE_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='dfx.proto.meta.RetrieveByTypeResponse.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfx.proto.meta.RetrieveByTypeResponse.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfx.proto.meta.RetrieveByTypeResponse.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=245,
)

_RETRIEVEBYTYPERESPONSE = _descriptor.Descriptor(
  name='RetrieveByTypeResponse',
  full_name='dfx.proto.meta.RetrieveByTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Values', full_name='dfx.proto.meta.RetrieveByTypeResponse.Values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RETRIEVEBYTYPERESPONSE_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=990,
)


_UPDATEBYTYPEREQUEST_PARAMVALUES = _descriptor.Descriptor(
  name='ParamValues',
  full_name='dfx.proto.meta.UpdateByTypeRequest.ParamValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='dfx.proto.meta.UpdateByTypeRequest.ParamValues.Type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ID', full_name='dfx.proto.meta.UpdateByTypeRequest.ParamValues.ID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Namespace', full_name='dfx.proto.meta.UpdateByTypeRequest.ParamValues.Namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=759,
  serialized_end=817,
)

_UPDATEBYTYPEREQUEST_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='dfx.proto.meta.UpdateByTypeRequest.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfx.proto.meta.UpdateByTypeRequest.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfx.proto.meta.UpdateByTypeRequest.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=245,
)

_UPDATEBYTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateByTypeRequest',
  full_name='dfx.proto.meta.UpdateByTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Params', full_name='dfx.proto.meta.UpdateByTypeRequest.Params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Values', full_name='dfx.proto.meta.UpdateByTypeRequest.Values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEBYTYPEREQUEST_PARAMVALUES, _UPDATEBYTYPEREQUEST_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1251,
)


_UPDATEBYTYPERESPONSE = _descriptor.Descriptor(
  name='UpdateByTypeResponse',
  full_name='dfx.proto.meta.UpdateByTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=1253,
  serialized_end=1275,
)

_UPDATEREQUEST_PARAMVALUES.containing_type = _UPDATEREQUEST
_UPDATEREQUEST_VALUESENTRY.containing_type = _UPDATEREQUEST
_UPDATEREQUEST.fields_by_name['Params'].message_type = _UPDATEREQUEST_PARAMVALUES
_UPDATEREQUEST.fields_by_name['Values'].message_type = _UPDATEREQUEST_VALUESENTRY
_RETRIEVEREQUEST_PARAMVALUES.containing_type = _RETRIEVEREQUEST
_RETRIEVEREQUEST_QUERYVALUES.containing_type = _RETRIEVEREQUEST
_RETRIEVEREQUEST.fields_by_name['Params'].message_type = _RETRIEVEREQUEST_PARAMVALUES
_RETRIEVEREQUEST.fields_by_name['Query'].message_type = _RETRIEVEREQUEST_QUERYVALUES
_RETRIEVERESPONSE_VALUESENTRY.containing_type = _RETRIEVERESPONSE
_RETRIEVERESPONSE.fields_by_name['Values'].message_type = _RETRIEVERESPONSE_VALUESENTRY
_RETRIEVEBYTYPEREQUEST_PARAMVALUES.containing_type = _RETRIEVEBYTYPEREQUEST
_RETRIEVEBYTYPEREQUEST_QUERYVALUES.containing_type = _RETRIEVEBYTYPEREQUEST
_RETRIEVEBYTYPEREQUEST.fields_by_name['Params'].message_type = _RETRIEVEBYTYPEREQUEST_PARAMVALUES
_RETRIEVEBYTYPEREQUEST.fields_by_name['Query'].message_type = _RETRIEVEBYTYPEREQUEST_QUERYVALUES
_RETRIEVEBYTYPERESPONSE_VALUESENTRY.containing_type = _RETRIEVEBYTYPERESPONSE
_RETRIEVEBYTYPERESPONSE.fields_by_name['Values'].message_type = _RETRIEVEBYTYPERESPONSE_VALUESENTRY
_UPDATEBYTYPEREQUEST_PARAMVALUES.containing_type = _UPDATEBYTYPEREQUEST
_UPDATEBYTYPEREQUEST_VALUESENTRY.containing_type = _UPDATEBYTYPEREQUEST
_UPDATEBYTYPEREQUEST.fields_by_name['Params'].message_type = _UPDATEBYTYPEREQUEST_PARAMVALUES
_UPDATEBYTYPEREQUEST.fields_by_name['Values'].message_type = _UPDATEBYTYPEREQUEST_VALUESENTRY
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['RetrieveRequest'] = _RETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['RetrieveResponse'] = _RETRIEVERESPONSE
DESCRIPTOR.message_types_by_name['RetrieveByTypeRequest'] = _RETRIEVEBYTYPEREQUEST
DESCRIPTOR.message_types_by_name['RetrieveByTypeResponse'] = _RETRIEVEBYTYPERESPONSE
DESCRIPTOR.message_types_by_name['UpdateByTypeRequest'] = _UPDATEBYTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateByTypeResponse'] = _UPDATEBYTYPERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {

  'ParamValues' : _reflection.GeneratedProtocolMessageType('ParamValues', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEREQUEST_PARAMVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateRequest.ParamValues)
    })
  ,

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEREQUEST_VALUESENTRY,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateRequest.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)
_sym_db.RegisterMessage(UpdateRequest.ParamValues)
_sym_db.RegisterMessage(UpdateRequest.ValuesEntry)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

RetrieveRequest = _reflection.GeneratedProtocolMessageType('RetrieveRequest', (_message.Message,), {

  'ParamValues' : _reflection.GeneratedProtocolMessageType('ParamValues', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEREQUEST_PARAMVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveRequest.ParamValues)
    })
  ,

  'QueryValues' : _reflection.GeneratedProtocolMessageType('QueryValues', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEREQUEST_QUERYVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveRequest.QueryValues)
    })
  ,
  'DESCRIPTOR' : _RETRIEVEREQUEST,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveRequest)
  })
_sym_db.RegisterMessage(RetrieveRequest)
_sym_db.RegisterMessage(RetrieveRequest.ParamValues)
_sym_db.RegisterMessage(RetrieveRequest.QueryValues)

RetrieveResponse = _reflection.GeneratedProtocolMessageType('RetrieveResponse', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVERESPONSE_VALUESENTRY,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveResponse.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _RETRIEVERESPONSE,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveResponse)
  })
_sym_db.RegisterMessage(RetrieveResponse)
_sym_db.RegisterMessage(RetrieveResponse.ValuesEntry)

RetrieveByTypeRequest = _reflection.GeneratedProtocolMessageType('RetrieveByTypeRequest', (_message.Message,), {

  'ParamValues' : _reflection.GeneratedProtocolMessageType('ParamValues', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEBYTYPEREQUEST_PARAMVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveByTypeRequest.ParamValues)
    })
  ,

  'QueryValues' : _reflection.GeneratedProtocolMessageType('QueryValues', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEBYTYPEREQUEST_QUERYVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveByTypeRequest.QueryValues)
    })
  ,
  'DESCRIPTOR' : _RETRIEVEBYTYPEREQUEST,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveByTypeRequest)
  })
_sym_db.RegisterMessage(RetrieveByTypeRequest)
_sym_db.RegisterMessage(RetrieveByTypeRequest.ParamValues)
_sym_db.RegisterMessage(RetrieveByTypeRequest.QueryValues)

RetrieveByTypeResponse = _reflection.GeneratedProtocolMessageType('RetrieveByTypeResponse', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEBYTYPERESPONSE_VALUESENTRY,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveByTypeResponse.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _RETRIEVEBYTYPERESPONSE,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.RetrieveByTypeResponse)
  })
_sym_db.RegisterMessage(RetrieveByTypeResponse)
_sym_db.RegisterMessage(RetrieveByTypeResponse.ValuesEntry)

UpdateByTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateByTypeRequest', (_message.Message,), {

  'ParamValues' : _reflection.GeneratedProtocolMessageType('ParamValues', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEBYTYPEREQUEST_PARAMVALUES,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateByTypeRequest.ParamValues)
    })
  ,

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEBYTYPEREQUEST_VALUESENTRY,
    '__module__' : 'meta_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateByTypeRequest.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEBYTYPEREQUEST,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateByTypeRequest)
  })
_sym_db.RegisterMessage(UpdateByTypeRequest)
_sym_db.RegisterMessage(UpdateByTypeRequest.ParamValues)
_sym_db.RegisterMessage(UpdateByTypeRequest.ValuesEntry)

UpdateByTypeResponse = _reflection.GeneratedProtocolMessageType('UpdateByTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBYTYPERESPONSE,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.meta.UpdateByTypeResponse)
  })
_sym_db.RegisterMessage(UpdateByTypeResponse)


DESCRIPTOR._options = None
_UPDATEREQUEST_VALUESENTRY._options = None
_RETRIEVERESPONSE_VALUESENTRY._options = None
_RETRIEVEBYTYPERESPONSE_VALUESENTRY._options = None
_UPDATEBYTYPEREQUEST_VALUESENTRY._options = None

_SERVICES = _descriptor.ServiceDescriptor(
  name='Services',
  full_name='dfx.proto.meta.Services',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1278,
  serialized_end=1636,
  methods=[
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='dfx.proto.meta.Services.Retrieve',
    index=0,
    containing_service=None,
    input_type=_RETRIEVEREQUEST,
    output_type=_RETRIEVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveByType',
    full_name='dfx.proto.meta.Services.RetrieveByType',
    index=1,
    containing_service=None,
    input_type=_RETRIEVEBYTYPEREQUEST,
    output_type=_RETRIEVEBYTYPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='dfx.proto.meta.Services.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateByType',
    full_name='dfx.proto.meta.Services.UpdateByType',
    index=3,
    containing_service=None,
    input_type=_UPDATEBYTYPEREQUEST,
    output_type=_UPDATEBYTYPERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICES)

DESCRIPTOR.services_by_name['Services'] = _SERVICES

# @@protoc_insertion_point(module_scope)