# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foxglove/SceneEntityDeletion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"foxglove/SceneEntityDeletion.proto\x12\x08\x66oxglove\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa4\x01\n\x13SceneEntityDeletion\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\".foxglove.SceneEntityDeletion.Type\x12\n\n\x02id\x18\x03 \x01(\t\" \n\x04Type\x12\x0f\n\x0bMATCHING_ID\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'foxglove.SceneEntityDeletion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENEENTITYDELETION._serialized_start=82
  _SCENEENTITYDELETION._serialized_end=246
  _SCENEENTITYDELETION_TYPE._serialized_start=214
  _SCENEENTITYDELETION_TYPE._serialized_end=246
# @@protoc_insertion_point(module_scope)