

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGrpcClient, RawGrpcClient
from .types.put_mockserver_grpc_descriptors_response import PutMockserverGrpcDescriptorsResponse
from .types.put_mockserver_grpc_health_request_status import PutMockserverGrpcHealthRequestStatus
from .types.put_mockserver_grpc_health_response import PutMockserverGrpcHealthResponse
from .types.put_mockserver_grpc_services_response_item import PutMockserverGrpcServicesResponseItem


OMIT = typing.cast(typing.Any, ...)


class GrpcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGrpcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGrpcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGrpcClient
        """
        return self._raw_client

    def load_ag_rpc_proto_descriptor_set(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGrpcDescriptorsResponse:
        """
        loads a compiled protobuf FileDescriptorSet (raw bytes) so gRPC services can be matched and mocked

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGrpcDescriptorsResponse
            descriptor set loaded
        """
        _response = self._raw_client.load_ag_rpc_proto_descriptor_set(request=request, request_options=request_options)
        return _response.data

    def retrieve_g_rpc_health_serving_statuses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the configured gRPC health serving status for each service (the default is reported under "_default")

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            serving statuses returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.grpc.retrieve_g_rpc_health_serving_statuses()
        """
        _response = self._raw_client.retrieve_g_rpc_health_serving_statuses(request_options=request_options)
        return _response.data

    def set_ag_rpc_health_serving_status(
        self,
        *,
        service: typing.Optional[str] = OMIT,
        status: typing.Optional[PutMockserverGrpcHealthRequestStatus] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGrpcHealthResponse:
        """
        Sets the gRPC health-checking serving status for a service (an empty service name sets the default), or removes a service override with 'remove':true.

        Parameters
        ----------
        service : typing.Optional[str]
            gRPC service name; an empty string sets the overall server status (the empty service name defined by the gRPC health checking protocol), rather than the status of any named service

        status : typing.Optional[PutMockserverGrpcHealthRequestStatus]

        remove : typing.Optional[bool]
            when true, removes the service override

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGrpcHealthResponse
            serving status set or removed

        Examples
        --------
        from fern.grpc import PutMockserverGrpcHealthRequestStatus

        from fern import FernApi

        client = FernApi()
        client.grpc.set_ag_rpc_health_serving_status(
            service="helloworld.Greeter",
            status=PutMockserverGrpcHealthRequestStatus.SERVING,
        )
        """
        _response = self._raw_client.set_ag_rpc_health_serving_status(
            service=service, status=status, remove=remove, request_options=request_options
        )
        return _response.data

    def list_loaded_g_rpc_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PutMockserverGrpcServicesResponseItem]:
        """
        Returns the gRPC services available from the loaded proto descriptor set, each with its methods and their input/output types and streaming flags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PutMockserverGrpcServicesResponseItem]
            loaded gRPC services returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.grpc.list_loaded_g_rpc_services()
        """
        _response = self._raw_client.list_loaded_g_rpc_services(request_options=request_options)
        return _response.data

    def reset_the_g_rpc_descriptor_store(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        clears all loaded gRPC proto descriptors and the services derived from them

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.grpc.reset_the_g_rpc_descriptor_store()
        """
        _response = self._raw_client.reset_the_g_rpc_descriptor_store(request_options=request_options)
        return _response.data


class AsyncGrpcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGrpcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGrpcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGrpcClient
        """
        return self._raw_client

    async def load_ag_rpc_proto_descriptor_set(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGrpcDescriptorsResponse:
        """
        loads a compiled protobuf FileDescriptorSet (raw bytes) so gRPC services can be matched and mocked

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGrpcDescriptorsResponse
            descriptor set loaded
        """
        _response = await self._raw_client.load_ag_rpc_proto_descriptor_set(
            request=request, request_options=request_options
        )
        return _response.data

    async def retrieve_g_rpc_health_serving_statuses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the configured gRPC health serving status for each service (the default is reported under "_default")

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            serving statuses returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.grpc.retrieve_g_rpc_health_serving_statuses()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_g_rpc_health_serving_statuses(request_options=request_options)
        return _response.data

    async def set_ag_rpc_health_serving_status(
        self,
        *,
        service: typing.Optional[str] = OMIT,
        status: typing.Optional[PutMockserverGrpcHealthRequestStatus] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverGrpcHealthResponse:
        """
        Sets the gRPC health-checking serving status for a service (an empty service name sets the default), or removes a service override with 'remove':true.

        Parameters
        ----------
        service : typing.Optional[str]
            gRPC service name; an empty string sets the overall server status (the empty service name defined by the gRPC health checking protocol), rather than the status of any named service

        status : typing.Optional[PutMockserverGrpcHealthRequestStatus]

        remove : typing.Optional[bool]
            when true, removes the service override

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverGrpcHealthResponse
            serving status set or removed

        Examples
        --------
        import asyncio

        from fern.grpc import PutMockserverGrpcHealthRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.grpc.set_ag_rpc_health_serving_status(
                service="helloworld.Greeter",
                status=PutMockserverGrpcHealthRequestStatus.SERVING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_ag_rpc_health_serving_status(
            service=service, status=status, remove=remove, request_options=request_options
        )
        return _response.data

    async def list_loaded_g_rpc_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PutMockserverGrpcServicesResponseItem]:
        """
        Returns the gRPC services available from the loaded proto descriptor set, each with its methods and their input/output types and streaming flags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PutMockserverGrpcServicesResponseItem]
            loaded gRPC services returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.grpc.list_loaded_g_rpc_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_loaded_g_rpc_services(request_options=request_options)
        return _response.data

    async def reset_the_g_rpc_descriptor_store(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        clears all loaded gRPC proto descriptors and the services derived from them

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.grpc.reset_the_g_rpc_descriptor_store()


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_the_g_rpc_descriptor_store(request_options=request_options)
        return _response.data
