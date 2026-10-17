

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account import Account
from .raw_client import AsyncRawLegacyEndpointsClient, RawLegacyEndpointsClient
from .types.list_legacy_moorings_response import ListLegacyMooringsResponse


class LegacyEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLegacyEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLegacyEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLegacyEndpointsClient
        """
        return self._raw_client

    def list_legacy_moorings(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListLegacyMooringsResponse:
        """
        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLegacyMooringsResponse
            Moorings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.legacy_endpoints.list_legacy_moorings(
            include="buoys",
        )
        """
        _response = self._raw_client.list_legacy_moorings(include=include, request_options=request_options)
        return _response.data

    def get_legacy_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            The account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.legacy_endpoints.get_legacy_account()
        """
        _response = self._raw_client.get_legacy_account(request_options=request_options)
        return _response.data


class AsyncLegacyEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLegacyEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLegacyEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLegacyEndpointsClient
        """
        return self._raw_client

    async def list_legacy_moorings(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListLegacyMooringsResponse:
        """
        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLegacyMooringsResponse
            Moorings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.legacy_endpoints.list_legacy_moorings(
                include="buoys",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_legacy_moorings(include=include, request_options=request_options)
        return _response.data

    async def get_legacy_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            The account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.legacy_endpoints.get_legacy_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_legacy_account(request_options=request_options)
        return _response.data
