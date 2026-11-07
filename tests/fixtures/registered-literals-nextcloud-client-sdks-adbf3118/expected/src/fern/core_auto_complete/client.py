

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_auto_complete_get200response import CoreAutoCompleteGet200Response
from .raw_client import AsyncRawCoreAutoCompleteClient, RawCoreAutoCompleteClient


class CoreAutoCompleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreAutoCompleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreAutoCompleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreAutoCompleteClient
        """
        return self._raw_client

    def get(
        self,
        *,
        search: str,
        item_type: typing.Optional[str] = None,
        item_id: typing.Optional[str] = None,
        sorter: typing.Optional[str] = None,
        share_types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreAutoCompleteGet200Response:
        """
        Parameters
        ----------
        search : str
            Text to search for

        item_type : typing.Optional[str]
            Type of the items to search for

        item_id : typing.Optional[str]
            ID of the items to search for

        sorter : typing.Optional[str]
            can be piped, top prio first, e.g.: "commenters|share-recipients"

        share_types : typing.Optional[str]
            Types of shares to search for

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAutoCompleteGet200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_auto_complete.get(
            search="search",
        )
        """
        _response = self._raw_client.get(
            search=search,
            item_type=item_type,
            item_id=item_id,
            sorter=sorter,
            share_types=share_types,
            limit=limit,
            request_options=request_options,
        )
        return _response.data


class AsyncCoreAutoCompleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreAutoCompleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreAutoCompleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreAutoCompleteClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        search: str,
        item_type: typing.Optional[str] = None,
        item_id: typing.Optional[str] = None,
        sorter: typing.Optional[str] = None,
        share_types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreAutoCompleteGet200Response:
        """
        Parameters
        ----------
        search : str
            Text to search for

        item_type : typing.Optional[str]
            Type of the items to search for

        item_id : typing.Optional[str]
            ID of the items to search for

        sorter : typing.Optional[str]
            can be piped, top prio first, e.g.: "commenters|share-recipients"

        share_types : typing.Optional[str]
            Types of shares to search for

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAutoCompleteGet200Response


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
            await client.core_auto_complete.get(
                search="search",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            search=search,
            item_type=item_type,
            item_id=item_id,
            sorter=sorter,
            share_types=share_types,
            limit=limit,
            request_options=request_options,
        )
        return _response.data
