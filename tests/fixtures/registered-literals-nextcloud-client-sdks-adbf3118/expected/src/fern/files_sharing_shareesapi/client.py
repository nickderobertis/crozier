

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.files_sharing_shareesapi_find_recommended200response import (
    FilesSharingShareesapiFindRecommended200Response,
)
from ..types.files_sharing_shareesapi_search200response import FilesSharingShareesapiSearch200Response
from .raw_client import AsyncRawFilesSharingShareesapiClient, RawFilesSharingShareesapiClient


class FilesSharingShareesapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesSharingShareesapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesSharingShareesapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesSharingShareesapiClient
        """
        return self._raw_client

    def search(
        self,
        *,
        search: typing.Optional[str] = None,
        item_type: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        share_type: typing.Optional[str] = None,
        lookup: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareesapiSearch200Response:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        item_type : typing.Optional[str]
            Limit to specific item types

        page : typing.Optional[int]
            Page offset for searching

        per_page : typing.Optional[int]
            Limit amount of search results per page

        share_type : typing.Optional[str]
            Limit to specific share types

        lookup : typing.Optional[int]
            If a global lookup should be performed too

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareesapiSearch200Response
            Sharees search result returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareesapi.search()
        """
        _response = self._raw_client.search(
            search=search,
            item_type=item_type,
            page=page,
            per_page=per_page,
            share_type=share_type,
            lookup=lookup,
            request_options=request_options,
        )
        return _response.data

    def find_recommended(
        self,
        *,
        item_type: str,
        share_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareesapiFindRecommended200Response:
        """
        Parameters
        ----------
        item_type : str
            Limit to specific item types

        share_type : typing.Optional[str]
            Limit to specific share types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareesapiFindRecommended200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareesapi.find_recommended(
            item_type="itemType",
        )
        """
        _response = self._raw_client.find_recommended(
            item_type=item_type, share_type=share_type, request_options=request_options
        )
        return _response.data


class AsyncFilesSharingShareesapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesSharingShareesapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesSharingShareesapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesSharingShareesapiClient
        """
        return self._raw_client

    async def search(
        self,
        *,
        search: typing.Optional[str] = None,
        item_type: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        share_type: typing.Optional[str] = None,
        lookup: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareesapiSearch200Response:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        item_type : typing.Optional[str]
            Limit to specific item types

        page : typing.Optional[int]
            Page offset for searching

        per_page : typing.Optional[int]
            Limit amount of search results per page

        share_type : typing.Optional[str]
            Limit to specific share types

        lookup : typing.Optional[int]
            If a global lookup should be performed too

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareesapiSearch200Response
            Sharees search result returned

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
            await client.files_sharing_shareesapi.search()


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            search=search,
            item_type=item_type,
            page=page,
            per_page=per_page,
            share_type=share_type,
            lookup=lookup,
            request_options=request_options,
        )
        return _response.data

    async def find_recommended(
        self,
        *,
        item_type: str,
        share_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareesapiFindRecommended200Response:
        """
        Parameters
        ----------
        item_type : str
            Limit to specific item types

        share_type : typing.Optional[str]
            Limit to specific share types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareesapiFindRecommended200Response


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
            await client.files_sharing_shareesapi.find_recommended(
                item_type="itemType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_recommended(
            item_type=item_type, share_type=share_type, request_options=request_options
        )
        return _response.data
