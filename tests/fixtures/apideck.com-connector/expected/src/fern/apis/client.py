

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apis_filter import ApisFilter
from ..types.get_api_response import GetApiResponse
from ..types.get_apis_response import GetApisResponse
from .raw_client import AsyncRawApisClient, RawApisClient


class ApisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApisClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ApisFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApisResponse:
        """
        List APIs

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ApisFilter]
            Apply filters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApisResponse
            Apis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.apis.all_()
        """
        _response = self._raw_client.all_(cursor=cursor, limit=limit, filter=filter, request_options=request_options)
        return _response.data

    def one(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiResponse:
        """
        Get API

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResponse
            Apis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.apis.one(
            id="id",
        )
        """
        _response = self._raw_client.one(id, request_options=request_options)
        return _response.data


class AsyncApisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApisClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ApisFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApisResponse:
        """
        List APIs

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ApisFilter]
            Apply filters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApisResponse
            Apis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apis.all_()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            cursor=cursor, limit=limit, filter=filter, request_options=request_options
        )
        return _response.data

    async def one(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiResponse:
        """
        Get API

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResponse
            Apis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apis.one(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, request_options=request_options)
        return _response.data
