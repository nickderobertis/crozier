

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTagsClient, RawTagsClient
from .types.tags_create_response import TagsCreateResponse
from .types.tags_list_response import TagsListResponse


OMIT = typing.cast(typing.Any, ...)


class TagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> TagsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(self, *, label: str, request_options: typing.Optional[RequestOptions] = None) -> TagsCreateResponse:
        """
        Parameters
        ----------
        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCreateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.create(
            label="label",
        )
        """
        _response = self._raw_client.create(label=label, request_options=request_options)
        return _response.data


class AsyncTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> TagsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self, *, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TagsCreateResponse:
        """
        Parameters
        ----------
        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.create(
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(label=label, request_options=request_options)
        return _response.data
