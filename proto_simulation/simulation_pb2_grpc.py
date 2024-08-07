# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto_simulation import simulation_pb2 as proto__simulation_dot_simulation__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto_simulation/simulation_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SimulationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartSimulation = channel.unary_unary(
                '/simulation.SimulationService/StartSimulation',
                request_serializer=proto__simulation_dot_simulation__pb2.SimulationRequest.SerializeToString,
                response_deserializer=proto__simulation_dot_simulation__pb2.SimulationResponse.FromString,
                _registered_method=True)
        self.PauseSimulation = channel.unary_unary(
                '/simulation.SimulationService/PauseSimulation',
                request_serializer=proto__simulation_dot_simulation__pb2.PauseRequest.SerializeToString,
                response_deserializer=proto__simulation_dot_simulation__pb2.PauseResponse.FromString,
                _registered_method=True)
        self.StreamUpdates = channel.unary_stream(
                '/simulation.SimulationService/StreamUpdates',
                request_serializer=proto__simulation_dot_simulation__pb2.StreamRequest.SerializeToString,
                response_deserializer=proto__simulation_dot_simulation__pb2.SimulationUpdate.FromString,
                _registered_method=True)


class SimulationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimulationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSimulation,
                    request_deserializer=proto__simulation_dot_simulation__pb2.SimulationRequest.FromString,
                    response_serializer=proto__simulation_dot_simulation__pb2.SimulationResponse.SerializeToString,
            ),
            'PauseSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseSimulation,
                    request_deserializer=proto__simulation_dot_simulation__pb2.PauseRequest.FromString,
                    response_serializer=proto__simulation_dot_simulation__pb2.PauseResponse.SerializeToString,
            ),
            'StreamUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamUpdates,
                    request_deserializer=proto__simulation_dot_simulation__pb2.StreamRequest.FromString,
                    response_serializer=proto__simulation_dot_simulation__pb2.SimulationUpdate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simulation.SimulationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('simulation.SimulationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SimulationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulation.SimulationService/StartSimulation',
            proto__simulation_dot_simulation__pb2.SimulationRequest.SerializeToString,
            proto__simulation_dot_simulation__pb2.SimulationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PauseSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulation.SimulationService/PauseSimulation',
            proto__simulation_dot_simulation__pb2.PauseRequest.SerializeToString,
            proto__simulation_dot_simulation__pb2.PauseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/simulation.SimulationService/StreamUpdates',
            proto__simulation_dot_simulation__pb2.StreamRequest.SerializeToString,
            proto__simulation_dot_simulation__pb2.SimulationUpdate.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
