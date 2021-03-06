# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rnetwork.proto\"\x07\n\x05\x45mpty\"\x18\n\x08Identity\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n\nMsgRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\"&\n\x08MsgReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\"%\n\x04Note\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x12\n\x03Img\x12\x0b\n\x03img\x18\x01 \x01(\t2\x9d\x01\n\x0bVideoStream\x12%\n\x0cImgStreaming\x12\x0b.MsgRequest\x1a\x06.Empty\"\x00\x12$\n\nImgGetting\x12\t.Identity\x1a\t.MsgReply\"\x00\x12\x1f\n\x08Register\x12\t.Identity\x1a\x06.Empty\"\x00\x12 \n\tCheckList\x12\x06.Empty\x1a\t.Identity\"\x00\x32\x46\n\nChatServer\x12\x1d\n\nChatStream\x12\x06.Empty\x1a\x05.Note0\x01\x12\x19\n\x08SendNote\x12\x05.Note\x1a\x06.Empty2^\n\x0b\x41udioStream\x12\'\n\x0e\x43hunkStreaming\x12\x0b.MsgRequest\x1a\x06.Empty\"\x00\x12&\n\x0c\x43hunkGetting\x12\t.Identity\x1a\t.MsgReply\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=17,
  serialized_end=24,
)


_IDENTITY = _descriptor.Descriptor(
  name='Identity',
  full_name='Identity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Identity.name', index=0,
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
  serialized_start=26,
  serialized_end=50,
)


_MSGREQUEST = _descriptor.Descriptor(
  name='MsgRequest',
  full_name='MsgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='MsgRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='MsgRequest.name', index=1,
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
  serialized_start=52,
  serialized_end=92,
)


_MSGREPLY = _descriptor.Descriptor(
  name='MsgReply',
  full_name='MsgReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='MsgReply.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='MsgReply.name', index=1,
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
  serialized_start=94,
  serialized_end=132,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Note.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Note.message', index=1,
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
  serialized_start=134,
  serialized_end=171,
)


_IMG = _descriptor.Descriptor(
  name='Img',
  full_name='Img',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='Img.img', index=0,
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
  serialized_start=173,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Identity'] = _IDENTITY
DESCRIPTOR.message_types_by_name['MsgRequest'] = _MSGREQUEST
DESCRIPTOR.message_types_by_name['MsgReply'] = _MSGREPLY
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['Img'] = _IMG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Identity = _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITY,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:Identity)
  })
_sym_db.RegisterMessage(Identity)

MsgRequest = _reflection.GeneratedProtocolMessageType('MsgRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:MsgRequest)
  })
_sym_db.RegisterMessage(MsgRequest)

MsgReply = _reflection.GeneratedProtocolMessageType('MsgReply', (_message.Message,), {
  'DESCRIPTOR' : _MSGREPLY,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:MsgReply)
  })
_sym_db.RegisterMessage(MsgReply)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
  'DESCRIPTOR' : _NOTE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:Note)
  })
_sym_db.RegisterMessage(Note)

Img = _reflection.GeneratedProtocolMessageType('Img', (_message.Message,), {
  'DESCRIPTOR' : _IMG,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:Img)
  })
_sym_db.RegisterMessage(Img)



_VIDEOSTREAM = _descriptor.ServiceDescriptor(
  name='VideoStream',
  full_name='VideoStream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=194,
  serialized_end=351,
  methods=[
  _descriptor.MethodDescriptor(
    name='ImgStreaming',
    full_name='VideoStream.ImgStreaming',
    index=0,
    containing_service=None,
    input_type=_MSGREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImgGetting',
    full_name='VideoStream.ImgGetting',
    index=1,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_MSGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='VideoStream.Register',
    index=2,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckList',
    full_name='VideoStream.CheckList',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_IDENTITY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VIDEOSTREAM)

DESCRIPTOR.services_by_name['VideoStream'] = _VIDEOSTREAM


_CHATSERVER = _descriptor.ServiceDescriptor(
  name='ChatServer',
  full_name='ChatServer',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=353,
  serialized_end=423,
  methods=[
  _descriptor.MethodDescriptor(
    name='ChatStream',
    full_name='ChatServer.ChatStream',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_NOTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendNote',
    full_name='ChatServer.SendNote',
    index=1,
    containing_service=None,
    input_type=_NOTE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATSERVER)

DESCRIPTOR.services_by_name['ChatServer'] = _CHATSERVER


_AUDIOSTREAM = _descriptor.ServiceDescriptor(
  name='AudioStream',
  full_name='AudioStream',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=425,
  serialized_end=519,
  methods=[
  _descriptor.MethodDescriptor(
    name='ChunkStreaming',
    full_name='AudioStream.ChunkStreaming',
    index=0,
    containing_service=None,
    input_type=_MSGREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChunkGetting',
    full_name='AudioStream.ChunkGetting',
    index=1,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_MSGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIOSTREAM)

DESCRIPTOR.services_by_name['AudioStream'] = _AUDIOSTREAM

# @@protoc_insertion_point(module_scope)
