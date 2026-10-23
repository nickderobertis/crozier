

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.status import Status
from .raw_client import AsyncRawGeneralClient, RawGeneralClient


class GeneralClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGeneralClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGeneralClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGeneralClient
        """
        return self._raw_client

    def service_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        <ul><li>Return the seismic store service status.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Service status.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.general.service_status()
        """
        _response = self._raw_client.service_status(request_options=request_options)
        return _response.data

    def service_status_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> Status:
        """
        <ul><li>Validates if the token audience is allowed</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            User token audience is allowed by seismic store service.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.general.service_status_check()
        """
        _response = self._raw_client.service_status_check(request_options=request_options)
        return _response.data


class AsyncGeneralClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGeneralClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGeneralClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGeneralClient
        """
        return self._raw_client

    async def service_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        <ul><li>Return the seismic store service status.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Service status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.general.service_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.service_status(request_options=request_options)
        return _response.data

    async def service_status_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> Status:
        """
        <ul><li>Validates if the token audience is allowed</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Status
            User token audience is allowed by seismic store service.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.general.service_status_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.service_status_check(request_options=request_options)
        return _response.data
