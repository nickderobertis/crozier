

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.telemetry_data import TelemetryData
from .raw_client import AsyncRawAgentTelemetryClient, RawAgentTelemetryClient


OMIT = typing.cast(typing.Any, ...)


class AgentTelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentTelemetryClient
        """
        return self._raw_client

    def post_api_v1agent_telemetry(
        self, *, request: typing.Sequence[TelemetryData], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[TelemetryData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, TelemetryData

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_telemetry.post_api_v1agent_telemetry(
            request=[TelemetryData()],
        )
        """
        _response = self._raw_client.post_api_v1agent_telemetry(request=request, request_options=request_options)
        return _response.data

    def post_api_v1agent_telemetry_standalone(
        self, *, request: typing.Sequence[TelemetryData], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[TelemetryData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, TelemetryData

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_telemetry.post_api_v1agent_telemetry_standalone(
            request=[TelemetryData()],
        )
        """
        _response = self._raw_client.post_api_v1agent_telemetry_standalone(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncAgentTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentTelemetryClient
        """
        return self._raw_client

    async def post_api_v1agent_telemetry(
        self, *, request: typing.Sequence[TelemetryData], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[TelemetryData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TelemetryData

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_telemetry.post_api_v1agent_telemetry(
                request=[TelemetryData()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1agent_telemetry(request=request, request_options=request_options)
        return _response.data

    async def post_api_v1agent_telemetry_standalone(
        self, *, request: typing.Sequence[TelemetryData], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Sequence[TelemetryData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TelemetryData

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_telemetry.post_api_v1agent_telemetry_standalone(
                request=[TelemetryData()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1agent_telemetry_standalone(
            request=request, request_options=request_options
        )
        return _response.data
