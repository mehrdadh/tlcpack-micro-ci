# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: microDevice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='microDevice.proto',
  package='microDevice',
  syntax='proto3',
  serialized_options=b'B\020MicroDeviceProtoP\001\242\002\004MDev',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11microDevice.proto\x12\x0bmicroDevice\"Z\n\rDeviceMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x16\n\x0esession_number\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\"P\n\x0b\x44\x65viceReply\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x10\n\x08is_alive\x18\x02 \x01(\x08\x12\x0b\n\x03vid\x18\x03 \x01(\t\x12\x0b\n\x03pid\x18\x04 \x01(\t\"6\n\x0eSessionMessage\x12\x16\n\x0esession_number\x18\x01 \x01(\t\x12\x0c\n\x04task\x18\x02 \x01(\t\"\x1d\n\rStringMessage\x12\x0c\n\x04text\x18\x01 \x01(\t2\xdb\x05\n\nRPCRequest\x12J\n\x10RPCDeviceRequest\x12\x1a.microDevice.DeviceMessage\x1a\x18.microDevice.DeviceReply\"\x00\x12J\n\x10RPCDeviceRelease\x12\x1a.microDevice.DeviceMessage\x1a\x18.microDevice.DeviceReply\"\x00\x12J\n\x10RPCDeviceIsAlive\x12\x1a.microDevice.DeviceMessage\x1a\x18.microDevice.DeviceReply\"\x00\x12O\n\x11RPCSessionRequest\x12\x1b.microDevice.SessionMessage\x1a\x1b.microDevice.SessionMessage\"\x00\x12M\n\x0fRPCSessionClose\x12\x1b.microDevice.SessionMessage\x1a\x1b.microDevice.SessionMessage\"\x00\x12P\n\x14RPCDeviceRequestList\x12\x1a.microDevice.StringMessage\x1a\x1a.microDevice.StringMessage\"\x00\x12R\n\x16RPCDeviceRequestEnable\x12\x1a.microDevice.DeviceMessage\x1a\x1a.microDevice.StringMessage\"\x00\x12S\n\x17RPCDeviceRequestDisable\x12\x1a.microDevice.DeviceMessage\x1a\x1a.microDevice.StringMessage\"\x00\x12N\n\x14RPCGetDeviceTypeInfo\x12\x1a.microDevice.DeviceMessage\x1a\x18.microDevice.DeviceReply\"\x00\x42\x1b\x42\x10MicroDeviceProtoP\x01\xa2\x02\x04MDevb\x06proto3'
)




_DEVICEMESSAGE = _descriptor.Descriptor(
  name='DeviceMessage',
  full_name='microDevice.DeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='microDevice.DeviceMessage.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='microDevice.DeviceMessage.serial_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_number', full_name='microDevice.DeviceMessage.session_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='microDevice.DeviceMessage.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=34,
  serialized_end=124,
)


_DEVICEREPLY = _descriptor.Descriptor(
  name='DeviceReply',
  full_name='microDevice.DeviceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='microDevice.DeviceReply.serial_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_alive', full_name='microDevice.DeviceReply.is_alive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vid', full_name='microDevice.DeviceReply.vid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='microDevice.DeviceReply.pid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=126,
  serialized_end=206,
)


_SESSIONMESSAGE = _descriptor.Descriptor(
  name='SessionMessage',
  full_name='microDevice.SessionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_number', full_name='microDevice.SessionMessage.session_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='microDevice.SessionMessage.task', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=208,
  serialized_end=262,
)


_STRINGMESSAGE = _descriptor.Descriptor(
  name='StringMessage',
  full_name='microDevice.StringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='microDevice.StringMessage.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=264,
  serialized_end=293,
)

DESCRIPTOR.message_types_by_name['DeviceMessage'] = _DEVICEMESSAGE
DESCRIPTOR.message_types_by_name['DeviceReply'] = _DEVICEREPLY
DESCRIPTOR.message_types_by_name['SessionMessage'] = _SESSIONMESSAGE
DESCRIPTOR.message_types_by_name['StringMessage'] = _STRINGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceMessage = _reflection.GeneratedProtocolMessageType('DeviceMessage', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEMESSAGE,
  '__module__' : 'microDevice_pb2'
  # @@protoc_insertion_point(class_scope:microDevice.DeviceMessage)
  })
_sym_db.RegisterMessage(DeviceMessage)

DeviceReply = _reflection.GeneratedProtocolMessageType('DeviceReply', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEREPLY,
  '__module__' : 'microDevice_pb2'
  # @@protoc_insertion_point(class_scope:microDevice.DeviceReply)
  })
_sym_db.RegisterMessage(DeviceReply)

SessionMessage = _reflection.GeneratedProtocolMessageType('SessionMessage', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONMESSAGE,
  '__module__' : 'microDevice_pb2'
  # @@protoc_insertion_point(class_scope:microDevice.SessionMessage)
  })
_sym_db.RegisterMessage(SessionMessage)

StringMessage = _reflection.GeneratedProtocolMessageType('StringMessage', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMESSAGE,
  '__module__' : 'microDevice_pb2'
  # @@protoc_insertion_point(class_scope:microDevice.StringMessage)
  })
_sym_db.RegisterMessage(StringMessage)


DESCRIPTOR._options = None

_RPCREQUEST = _descriptor.ServiceDescriptor(
  name='RPCRequest',
  full_name='microDevice.RPCRequest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=296,
  serialized_end=1027,
  methods=[
  _descriptor.MethodDescriptor(
    name='RPCDeviceRequest',
    full_name='microDevice.RPCRequest.RPCDeviceRequest',
    index=0,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_DEVICEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCDeviceRelease',
    full_name='microDevice.RPCRequest.RPCDeviceRelease',
    index=1,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_DEVICEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCDeviceIsAlive',
    full_name='microDevice.RPCRequest.RPCDeviceIsAlive',
    index=2,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_DEVICEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCSessionRequest',
    full_name='microDevice.RPCRequest.RPCSessionRequest',
    index=3,
    containing_service=None,
    input_type=_SESSIONMESSAGE,
    output_type=_SESSIONMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCSessionClose',
    full_name='microDevice.RPCRequest.RPCSessionClose',
    index=4,
    containing_service=None,
    input_type=_SESSIONMESSAGE,
    output_type=_SESSIONMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCDeviceRequestList',
    full_name='microDevice.RPCRequest.RPCDeviceRequestList',
    index=5,
    containing_service=None,
    input_type=_STRINGMESSAGE,
    output_type=_STRINGMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCDeviceRequestEnable',
    full_name='microDevice.RPCRequest.RPCDeviceRequestEnable',
    index=6,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_STRINGMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCDeviceRequestDisable',
    full_name='microDevice.RPCRequest.RPCDeviceRequestDisable',
    index=7,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_STRINGMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RPCGetDeviceTypeInfo',
    full_name='microDevice.RPCRequest.RPCGetDeviceTypeInfo',
    index=8,
    containing_service=None,
    input_type=_DEVICEMESSAGE,
    output_type=_DEVICEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPCREQUEST)

DESCRIPTOR.services_by_name['RPCRequest'] = _RPCREQUEST

# @@protoc_insertion_point(module_scope)
