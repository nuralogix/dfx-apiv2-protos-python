# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: general.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='general.proto',
  package='dfx.proto.general',
  syntax='proto3',
  serialized_options=b'\n\020ai.nuralogix.dfxB\007General\370\001\001',
  serialized_pb=b'\n\rgeneral.proto\x12\x11\x64\x66x.proto.general\x1a\x1cgoogle/protobuf/struct.proto\"\x0f\n\rStatusRequest\"\xed\x01\n\x0eStatusResponse\x12\x10\n\x08StatusID\x18\x01 \x01(\t\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12;\n\x05Notes\x18\x03 \x03(\x0b\x32,.dfx.proto.general.StatusResponse.NotesEntry\x1a%\n\x04Note\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\r\x12\x0f\n\x07Message\x18\x02 \x01(\t\x1aT\n\nNotesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.dfx.proto.general.StatusResponse.Note:\x02\x38\x01\"\x12\n\x10MimeTypesRequest\"\x86\x01\n\x11MimeTypesResponse\x12=\n\x06Values\x18\x01 \x03(\x0b\x32-.dfx.proto.general.MimeTypesResponse.MimeType\x1a\x32\n\x08MimeType\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x0c\n\x04Mime\x18\x03 \x01(\t\"$\n\x14HeartbeatReadRequest\x12\x0c\n\x04UUID\x18\x01 \x01(\t\";\n\x15HeartbeatReadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"3\n\x15HeartbeatWriteRequest\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12\x0c\n\x04Mode\x18\x02 \x01(\t\"Q\n\x16HeartbeatWriteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12&\n\x05stats\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct2\xb5\x01\n\x08Services\x12O\n\x06Status\x12 .dfx.proto.general.StatusRequest\x1a!.dfx.proto.general.StatusResponse\"\x00\x12X\n\tMimeTypes\x12#.dfx.proto.general.MimeTypesRequest\x1a$.dfx.proto.general.MimeTypesResponse\"\x00\x42\x1e\n\x10\x61i.nuralogix.dfxB\x07General\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='dfx.proto.general.StatusRequest',
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
  serialized_start=66,
  serialized_end=81,
)


_STATUSRESPONSE_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='dfx.proto.general.StatusResponse.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Date', full_name='dfx.proto.general.StatusResponse.Note.Date', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Message', full_name='dfx.proto.general.StatusResponse.Note.Message', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=235,
)

_STATUSRESPONSE_NOTESENTRY = _descriptor.Descriptor(
  name='NotesEntry',
  full_name='dfx.proto.general.StatusResponse.NotesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfx.proto.general.StatusResponse.NotesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfx.proto.general.StatusResponse.NotesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=237,
  serialized_end=321,
)

_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='dfx.proto.general.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StatusID', full_name='dfx.proto.general.StatusResponse.StatusID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Version', full_name='dfx.proto.general.StatusResponse.Version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Notes', full_name='dfx.proto.general.StatusResponse.Notes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATUSRESPONSE_NOTE, _STATUSRESPONSE_NOTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=321,
)


_MIMETYPESREQUEST = _descriptor.Descriptor(
  name='MimeTypesRequest',
  full_name='dfx.proto.general.MimeTypesRequest',
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
  serialized_start=323,
  serialized_end=341,
)


_MIMETYPESRESPONSE_MIMETYPE = _descriptor.Descriptor(
  name='MimeType',
  full_name='dfx.proto.general.MimeTypesResponse.MimeType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='dfx.proto.general.MimeTypesResponse.MimeType.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Name', full_name='dfx.proto.general.MimeTypesResponse.MimeType.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Mime', full_name='dfx.proto.general.MimeTypesResponse.MimeType.Mime', index=2,
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
  serialized_start=428,
  serialized_end=478,
)

_MIMETYPESRESPONSE = _descriptor.Descriptor(
  name='MimeTypesResponse',
  full_name='dfx.proto.general.MimeTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Values', full_name='dfx.proto.general.MimeTypesResponse.Values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MIMETYPESRESPONSE_MIMETYPE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=478,
)


_HEARTBEATREADREQUEST = _descriptor.Descriptor(
  name='HeartbeatReadRequest',
  full_name='dfx.proto.general.HeartbeatReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UUID', full_name='dfx.proto.general.HeartbeatReadRequest.UUID', index=0,
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
  serialized_start=480,
  serialized_end=516,
)


_HEARTBEATREADRESPONSE = _descriptor.Descriptor(
  name='HeartbeatReadResponse',
  full_name='dfx.proto.general.HeartbeatReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfx.proto.general.HeartbeatReadResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='dfx.proto.general.HeartbeatReadResponse.timestamp', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=577,
)


_HEARTBEATWRITEREQUEST = _descriptor.Descriptor(
  name='HeartbeatWriteRequest',
  full_name='dfx.proto.general.HeartbeatWriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UUID', full_name='dfx.proto.general.HeartbeatWriteRequest.UUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='dfx.proto.general.HeartbeatWriteRequest.Mode', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=630,
)


_HEARTBEATWRITERESPONSE = _descriptor.Descriptor(
  name='HeartbeatWriteResponse',
  full_name='dfx.proto.general.HeartbeatWriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfx.proto.general.HeartbeatWriteResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='dfx.proto.general.HeartbeatWriteResponse.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=632,
  serialized_end=713,
)

_STATUSRESPONSE_NOTE.containing_type = _STATUSRESPONSE
_STATUSRESPONSE_NOTESENTRY.fields_by_name['value'].message_type = _STATUSRESPONSE_NOTE
_STATUSRESPONSE_NOTESENTRY.containing_type = _STATUSRESPONSE
_STATUSRESPONSE.fields_by_name['Notes'].message_type = _STATUSRESPONSE_NOTESENTRY
_MIMETYPESRESPONSE_MIMETYPE.containing_type = _MIMETYPESRESPONSE
_MIMETYPESRESPONSE.fields_by_name['Values'].message_type = _MIMETYPESRESPONSE_MIMETYPE
_HEARTBEATWRITERESPONSE.fields_by_name['stats'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['MimeTypesRequest'] = _MIMETYPESREQUEST
DESCRIPTOR.message_types_by_name['MimeTypesResponse'] = _MIMETYPESRESPONSE
DESCRIPTOR.message_types_by_name['HeartbeatReadRequest'] = _HEARTBEATREADREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatReadResponse'] = _HEARTBEATREADRESPONSE
DESCRIPTOR.message_types_by_name['HeartbeatWriteRequest'] = _HEARTBEATWRITEREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatWriteResponse'] = _HEARTBEATWRITERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {

  'Note' : _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
    'DESCRIPTOR' : _STATUSRESPONSE_NOTE,
    '__module__' : 'general_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.general.StatusResponse.Note)
    })
  ,

  'NotesEntry' : _reflection.GeneratedProtocolMessageType('NotesEntry', (_message.Message,), {
    'DESCRIPTOR' : _STATUSRESPONSE_NOTESENTRY,
    '__module__' : 'general_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.general.StatusResponse.NotesEntry)
    })
  ,
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)
_sym_db.RegisterMessage(StatusResponse.Note)
_sym_db.RegisterMessage(StatusResponse.NotesEntry)

MimeTypesRequest = _reflection.GeneratedProtocolMessageType('MimeTypesRequest', (_message.Message,), {
  'DESCRIPTOR' : _MIMETYPESREQUEST,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.MimeTypesRequest)
  })
_sym_db.RegisterMessage(MimeTypesRequest)

MimeTypesResponse = _reflection.GeneratedProtocolMessageType('MimeTypesResponse', (_message.Message,), {

  'MimeType' : _reflection.GeneratedProtocolMessageType('MimeType', (_message.Message,), {
    'DESCRIPTOR' : _MIMETYPESRESPONSE_MIMETYPE,
    '__module__' : 'general_pb2'
    # @@protoc_insertion_point(class_scope:dfx.proto.general.MimeTypesResponse.MimeType)
    })
  ,
  'DESCRIPTOR' : _MIMETYPESRESPONSE,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.MimeTypesResponse)
  })
_sym_db.RegisterMessage(MimeTypesResponse)
_sym_db.RegisterMessage(MimeTypesResponse.MimeType)

HeartbeatReadRequest = _reflection.GeneratedProtocolMessageType('HeartbeatReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREADREQUEST,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.HeartbeatReadRequest)
  })
_sym_db.RegisterMessage(HeartbeatReadRequest)

HeartbeatReadResponse = _reflection.GeneratedProtocolMessageType('HeartbeatReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREADRESPONSE,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.HeartbeatReadResponse)
  })
_sym_db.RegisterMessage(HeartbeatReadResponse)

HeartbeatWriteRequest = _reflection.GeneratedProtocolMessageType('HeartbeatWriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATWRITEREQUEST,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.HeartbeatWriteRequest)
  })
_sym_db.RegisterMessage(HeartbeatWriteRequest)

HeartbeatWriteResponse = _reflection.GeneratedProtocolMessageType('HeartbeatWriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATWRITERESPONSE,
  '__module__' : 'general_pb2'
  # @@protoc_insertion_point(class_scope:dfx.proto.general.HeartbeatWriteResponse)
  })
_sym_db.RegisterMessage(HeartbeatWriteResponse)


DESCRIPTOR._options = None
_STATUSRESPONSE_NOTESENTRY._options = None

_SERVICES = _descriptor.ServiceDescriptor(
  name='Services',
  full_name='dfx.proto.general.Services',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=716,
  serialized_end=897,
  methods=[
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='dfx.proto.general.Services.Status',
    index=0,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MimeTypes',
    full_name='dfx.proto.general.Services.MimeTypes',
    index=1,
    containing_service=None,
    input_type=_MIMETYPESREQUEST,
    output_type=_MIMETYPESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICES)

DESCRIPTOR.services_by_name['Services'] = _SERVICES

# @@protoc_insertion_point(module_scope)