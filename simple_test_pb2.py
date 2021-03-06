# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple_test.proto',
  package='simpletest',
  syntax='proto3',
  serialized_pb=_b('\n\x11simple_test.proto\x12\nsimpletest\"\x1b\n\nRequestOne\x12\r\n\x05hello\x18\x01 \x01(\t\"\x1d\n\x0bResponseOne\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1f\n\x0bRequestList\x12\x10\n\x08namelist\x18\x01 \x01(\t\"\"\n\x0cResponseList\x12\x12\n\nresultlist\x18\x01 \x01(\t2\x8c\x02\n\nSimpleTest\x12\x39\n\x06GetOne\x12\x16.simpletest.RequestOne\x1a\x17.simpletest.ResponseOne\x12=\n\x07GetList\x12\x16.simpletest.RequestOne\x1a\x18.simpletest.ResponseList0\x01\x12>\n\x08PostList\x12\x17.simpletest.RequestList\x1a\x17.simpletest.ResponseOne(\x01\x12\x44\n\x0bPostAndPost\x12\x17.simpletest.RequestList\x1a\x18.simpletest.ResponseList(\x01\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTONE = _descriptor.Descriptor(
  name='RequestOne',
  full_name='simpletest.RequestOne',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='simpletest.RequestOne.hello', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=60,
)


_RESPONSEONE = _descriptor.Descriptor(
  name='ResponseOne',
  full_name='simpletest.ResponseOne',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='simpletest.ResponseOne.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=91,
)


_REQUESTLIST = _descriptor.Descriptor(
  name='RequestList',
  full_name='simpletest.RequestList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namelist', full_name='simpletest.RequestList.namelist', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=124,
)


_RESPONSELIST = _descriptor.Descriptor(
  name='ResponseList',
  full_name='simpletest.ResponseList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultlist', full_name='simpletest.ResponseList.resultlist', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['RequestOne'] = _REQUESTONE
DESCRIPTOR.message_types_by_name['ResponseOne'] = _RESPONSEONE
DESCRIPTOR.message_types_by_name['RequestList'] = _REQUESTLIST
DESCRIPTOR.message_types_by_name['ResponseList'] = _RESPONSELIST

RequestOne = _reflection.GeneratedProtocolMessageType('RequestOne', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTONE,
  __module__ = 'simple_test_pb2'
  # @@protoc_insertion_point(class_scope:simpletest.RequestOne)
  ))
_sym_db.RegisterMessage(RequestOne)

ResponseOne = _reflection.GeneratedProtocolMessageType('ResponseOne', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEONE,
  __module__ = 'simple_test_pb2'
  # @@protoc_insertion_point(class_scope:simpletest.ResponseOne)
  ))
_sym_db.RegisterMessage(ResponseOne)

RequestList = _reflection.GeneratedProtocolMessageType('RequestList', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLIST,
  __module__ = 'simple_test_pb2'
  # @@protoc_insertion_point(class_scope:simpletest.RequestList)
  ))
_sym_db.RegisterMessage(RequestList)

ResponseList = _reflection.GeneratedProtocolMessageType('ResponseList', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSELIST,
  __module__ = 'simple_test_pb2'
  # @@protoc_insertion_point(class_scope:simpletest.ResponseList)
  ))
_sym_db.RegisterMessage(ResponseList)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class SimpleTestStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetOne = channel.unary_unary(
          '/simpletest.SimpleTest/GetOne',
          request_serializer=RequestOne.SerializeToString,
          response_deserializer=ResponseOne.FromString,
          )
      self.GetList = channel.unary_stream(
          '/simpletest.SimpleTest/GetList',
          request_serializer=RequestOne.SerializeToString,
          response_deserializer=ResponseList.FromString,
          )
      self.PostList = channel.stream_unary(
          '/simpletest.SimpleTest/PostList',
          request_serializer=RequestList.SerializeToString,
          response_deserializer=ResponseOne.FromString,
          )
      self.PostAndPost = channel.stream_stream(
          '/simpletest.SimpleTest/PostAndPost',
          request_serializer=RequestList.SerializeToString,
          response_deserializer=ResponseList.FromString,
          )


  class SimpleTestServicer(object):

    def GetOne(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetList(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def PostList(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def PostAndPost(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_SimpleTestServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetOne': grpc.unary_unary_rpc_method_handler(
            servicer.GetOne,
            request_deserializer=RequestOne.FromString,
            response_serializer=ResponseOne.SerializeToString,
        ),
        'GetList': grpc.unary_stream_rpc_method_handler(
            servicer.GetList,
            request_deserializer=RequestOne.FromString,
            response_serializer=ResponseList.SerializeToString,
        ),
        'PostList': grpc.stream_unary_rpc_method_handler(
            servicer.PostList,
            request_deserializer=RequestList.FromString,
            response_serializer=ResponseOne.SerializeToString,
        ),
        'PostAndPost': grpc.stream_stream_rpc_method_handler(
            servicer.PostAndPost,
            request_deserializer=RequestList.FromString,
            response_serializer=ResponseList.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'simpletest.SimpleTest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaSimpleTestServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetOne(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetList(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def PostList(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def PostAndPost(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaSimpleTestStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetOne(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetOne.future = None
    def GetList(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    def PostList(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    PostList.future = None
    def PostAndPost(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()


  def beta_create_SimpleTest_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('simpletest.SimpleTest', 'GetList'): RequestOne.FromString,
      ('simpletest.SimpleTest', 'GetOne'): RequestOne.FromString,
      ('simpletest.SimpleTest', 'PostAndPost'): RequestList.FromString,
      ('simpletest.SimpleTest', 'PostList'): RequestList.FromString,
    }
    response_serializers = {
      ('simpletest.SimpleTest', 'GetList'): ResponseList.SerializeToString,
      ('simpletest.SimpleTest', 'GetOne'): ResponseOne.SerializeToString,
      ('simpletest.SimpleTest', 'PostAndPost'): ResponseList.SerializeToString,
      ('simpletest.SimpleTest', 'PostList'): ResponseOne.SerializeToString,
    }
    method_implementations = {
      ('simpletest.SimpleTest', 'GetList'): face_utilities.unary_stream_inline(servicer.GetList),
      ('simpletest.SimpleTest', 'GetOne'): face_utilities.unary_unary_inline(servicer.GetOne),
      ('simpletest.SimpleTest', 'PostAndPost'): face_utilities.stream_stream_inline(servicer.PostAndPost),
      ('simpletest.SimpleTest', 'PostList'): face_utilities.stream_unary_inline(servicer.PostList),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_SimpleTest_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('simpletest.SimpleTest', 'GetList'): RequestOne.SerializeToString,
      ('simpletest.SimpleTest', 'GetOne'): RequestOne.SerializeToString,
      ('simpletest.SimpleTest', 'PostAndPost'): RequestList.SerializeToString,
      ('simpletest.SimpleTest', 'PostList'): RequestList.SerializeToString,
    }
    response_deserializers = {
      ('simpletest.SimpleTest', 'GetList'): ResponseList.FromString,
      ('simpletest.SimpleTest', 'GetOne'): ResponseOne.FromString,
      ('simpletest.SimpleTest', 'PostAndPost'): ResponseList.FromString,
      ('simpletest.SimpleTest', 'PostList'): ResponseOne.FromString,
    }
    cardinalities = {
      'GetList': cardinality.Cardinality.UNARY_STREAM,
      'GetOne': cardinality.Cardinality.UNARY_UNARY,
      'PostAndPost': cardinality.Cardinality.STREAM_STREAM,
      'PostList': cardinality.Cardinality.STREAM_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'simpletest.SimpleTest', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
