

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.internal_create_telemetry_entry_response import InternalCreateTelemetryEntryResponse
from .raw_client import AsyncRawInternalTelemetryClient, RawInternalTelemetryClient


OMIT = typing.cast(typing.Any, ...)


class InternalTelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalTelemetryClient
        """
        return self._raw_client

    def internal_telemetry_create_telemetry_entry(
        self,
        *,
        number_of_users: int,
        number_of_accounts: int,
        number_of_connections: int,
        number_of_api_calls: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalCreateTelemetryEntryResponse:
        """
        Create telemetry entry for a deployment

        Parameters
        ----------
        number_of_users : int

        number_of_accounts : int

        number_of_connections : int

        number_of_api_calls : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalCreateTelemetryEntryResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_telemetry.internal_telemetry_create_telemetry_entry(
            number_of_users=1,
            number_of_accounts=1,
            number_of_connections=1,
            number_of_api_calls=1,
        )
        """
        _response = self._raw_client.internal_telemetry_create_telemetry_entry(
            number_of_users=number_of_users,
            number_of_accounts=number_of_accounts,
            number_of_connections=number_of_connections,
            number_of_api_calls=number_of_api_calls,
            request_options=request_options,
        )
        return _response.data


class AsyncInternalTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalTelemetryClient
        """
        return self._raw_client

    async def internal_telemetry_create_telemetry_entry(
        self,
        *,
        number_of_users: int,
        number_of_accounts: int,
        number_of_connections: int,
        number_of_api_calls: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalCreateTelemetryEntryResponse:
        """
        Create telemetry entry for a deployment

        Parameters
        ----------
        number_of_users : int

        number_of_accounts : int

        number_of_connections : int

        number_of_api_calls : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalCreateTelemetryEntryResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_telemetry.internal_telemetry_create_telemetry_entry(
                number_of_users=1,
                number_of_accounts=1,
                number_of_connections=1,
                number_of_api_calls=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_telemetry_create_telemetry_entry(
            number_of_users=number_of_users,
            number_of_accounts=number_of_accounts,
            number_of_connections=number_of_connections,
            number_of_api_calls=number_of_api_calls,
            request_options=request_options,
        )
        return _response.data
