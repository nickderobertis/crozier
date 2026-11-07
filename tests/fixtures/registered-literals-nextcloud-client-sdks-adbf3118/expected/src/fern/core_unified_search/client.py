

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_unified_search_get_providers200response import CoreUnifiedSearchGetProviders200Response
from ..types.core_unified_search_search200response import CoreUnifiedSearchSearch200Response
from .raw_client import AsyncRawCoreUnifiedSearchClient, RawCoreUnifiedSearchClient


class CoreUnifiedSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreUnifiedSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreUnifiedSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreUnifiedSearchClient
        """
        return self._raw_client

    def get_providers(
        self, *, from_: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreUnifiedSearchGetProviders200Response:
        """
        Parameters
        ----------
        from_ : typing.Optional[str]
            the url the user is currently at

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreUnifiedSearchGetProviders200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_unified_search.get_providers()
        """
        _response = self._raw_client.get_providers(from_=from_, request_options=request_options)
        return _response.data

    def search(
        self,
        provider_id: str,
        *,
        term: typing.Optional[str] = None,
        sort_order: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreUnifiedSearchSearch200Response:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        term : typing.Optional[str]
            Term to search

        sort_order : typing.Optional[int]
            Order of entries

        limit : typing.Optional[int]
            Maximum amount of entries

        cursor : typing.Optional[str]
            Offset for searching

        from_ : typing.Optional[str]
            The current user URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreUnifiedSearchSearch200Response
            Search entries returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_unified_search.search(
            provider_id="providerId",
        )
        """
        _response = self._raw_client.search(
            provider_id,
            term=term,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
            from_=from_,
            request_options=request_options,
        )
        return _response.data


class AsyncCoreUnifiedSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreUnifiedSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreUnifiedSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreUnifiedSearchClient
        """
        return self._raw_client

    async def get_providers(
        self, *, from_: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreUnifiedSearchGetProviders200Response:
        """
        Parameters
        ----------
        from_ : typing.Optional[str]
            the url the user is currently at

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreUnifiedSearchGetProviders200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_unified_search.get_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_providers(from_=from_, request_options=request_options)
        return _response.data

    async def search(
        self,
        provider_id: str,
        *,
        term: typing.Optional[str] = None,
        sort_order: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreUnifiedSearchSearch200Response:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        term : typing.Optional[str]
            Term to search

        sort_order : typing.Optional[int]
            Order of entries

        limit : typing.Optional[int]
            Maximum amount of entries

        cursor : typing.Optional[str]
            Offset for searching

        from_ : typing.Optional[str]
            The current user URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreUnifiedSearchSearch200Response
            Search entries returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_unified_search.search(
                provider_id="providerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            provider_id,
            term=term,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
            from_=from_,
            request_options=request_options,
        )
        return _response.data
