# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from microtvm_ci.device import microDevice_pb2 as microtvm__ci_dot_device_dot_microDevice__pb2


class RPCRequestStub(object):
    """The device request service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RPCDeviceRequest = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceRequest',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
                )
        self.RPCDeviceRelease = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceRelease',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
                )
        self.RPCDeviceIsAlive = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceIsAlive',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
                )
        self.RPCSessionRequest = channel.unary_unary(
                '/microDevice.RPCRequest/RPCSessionRequest',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
                )
        self.RPCSessionClose = channel.unary_unary(
                '/microDevice.RPCRequest/RPCSessionClose',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
                )
        self.RPCDeviceRequestList = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceRequestList',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
                )
        self.RPCDeviceRequestEnable = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceRequestEnable',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
                )
        self.RPCDeviceRequestDisable = channel.unary_unary(
                '/microDevice.RPCRequest/RPCDeviceRequestDisable',
                request_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
                response_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
                )


class RPCRequestServicer(object):
    """The device request service.
    """

    def RPCDeviceRequest(self, request, context):
        """Send a device serial
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeviceRelease(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeviceIsAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCSessionRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCSessionClose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeviceRequestList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeviceRequestEnable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeviceRequestDisable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCRequestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RPCDeviceRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceRequest,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.SerializeToString,
            ),
            'RPCDeviceRelease': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceRelease,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.SerializeToString,
            ),
            'RPCDeviceIsAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceIsAlive,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.SerializeToString,
            ),
            'RPCSessionRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCSessionRequest,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
            ),
            'RPCSessionClose': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCSessionClose,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
            ),
            'RPCDeviceRequestList': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceRequestList,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.SerializeToString,
            ),
            'RPCDeviceRequestEnable': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceRequestEnable,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.SerializeToString,
            ),
            'RPCDeviceRequestDisable': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeviceRequestDisable,
                    request_deserializer=microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.FromString,
                    response_serializer=microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'microDevice.RPCRequest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCRequest(object):
    """The device request service.
    """

    @staticmethod
    def RPCDeviceRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceRequest',
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCDeviceRelease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceRelease',
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCDeviceIsAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceIsAlive',
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCSessionRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCSessionRequest',
            microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCSessionClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCSessionClose',
            microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.SessionMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCDeviceRequestList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceRequestList',
            microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCDeviceRequestEnable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceRequestEnable',
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RPCDeviceRequestDisable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microDevice.RPCRequest/RPCDeviceRequestDisable',
            microtvm__ci_dot_device_dot_microDevice__pb2.DeviceMessage.SerializeToString,
            microtvm__ci_dot_device_dot_microDevice__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
