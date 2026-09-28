

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.events_get_response import EventsGetResponse
from ..types.logs_get_response import LogsGetResponse
from .raw_client import AsyncRawObservabilityClient, RawObservabilityClient


class ObservabilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObservabilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObservabilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObservabilityClient
        """
        return self._raw_client

    def get_kubernetes_events_for_a_specific_resource(
        self,
        *,
        name: str,
        kind: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventsGetResponse:
        """
        Get Kubernetes events for a specific resource

        Parameters
        ----------
        name : str
            Resource name

        kind : str
            Resource kind

        namespace : typing.Optional[str]
            Resource namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.observability.get_kubernetes_events_for_a_specific_resource(
            name="name",
            kind="kind",
        )
        """
        _response = self._raw_client.get_kubernetes_events_for_a_specific_resource(
            name=name, kind=kind, namespace=namespace, request_options=request_options
        )
        return _response.data

    def get_container_logs_from_a_pod(
        self,
        *,
        name: str,
        namespace: str,
        container: typing.Optional[str] = None,
        tail_lines: typing.Optional[float] = None,
        previous: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogsGetResponse:
        """
        Get container logs from a pod

        Parameters
        ----------
        name : str
            Pod name

        namespace : str
            Pod namespace

        container : typing.Optional[str]
            Container name (defaults to first container)

        tail_lines : typing.Optional[float]
            Number of lines from end

        previous : typing.Optional[bool]
            Get logs from previous container instance

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.observability.get_container_logs_from_a_pod(
            name="name",
            namespace="namespace",
        )
        """
        _response = self._raw_client.get_container_logs_from_a_pod(
            name=name,
            namespace=namespace,
            container=container,
            tail_lines=tail_lines,
            previous=previous,
            request_options=request_options,
        )
        return _response.data


class AsyncObservabilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObservabilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObservabilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObservabilityClient
        """
        return self._raw_client

    async def get_kubernetes_events_for_a_specific_resource(
        self,
        *,
        name: str,
        kind: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventsGetResponse:
        """
        Get Kubernetes events for a specific resource

        Parameters
        ----------
        name : str
            Resource name

        kind : str
            Resource kind

        namespace : typing.Optional[str]
            Resource namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.observability.get_kubernetes_events_for_a_specific_resource(
                name="name",
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kubernetes_events_for_a_specific_resource(
            name=name, kind=kind, namespace=namespace, request_options=request_options
        )
        return _response.data

    async def get_container_logs_from_a_pod(
        self,
        *,
        name: str,
        namespace: str,
        container: typing.Optional[str] = None,
        tail_lines: typing.Optional[float] = None,
        previous: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogsGetResponse:
        """
        Get container logs from a pod

        Parameters
        ----------
        name : str
            Pod name

        namespace : str
            Pod namespace

        container : typing.Optional[str]
            Container name (defaults to first container)

        tail_lines : typing.Optional[float]
            Number of lines from end

        previous : typing.Optional[bool]
            Get logs from previous container instance

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.observability.get_container_logs_from_a_pod(
                name="name",
                namespace="namespace",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_container_logs_from_a_pod(
            name=name,
            namespace=namespace,
            container=container,
            tail_lines=tail_lines,
            previous=previous,
            request_options=request_options,
        )
        return _response.data
