

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.read_list_request_match_dto import ReadListRequestMatchDto
from .raw_client import AsyncRawComicRackClient, RawComicRackClient


OMIT = typing.cast(typing.Any, ...)


class ComicRackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComicRackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComicRackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComicRackClient
        """
        return self._raw_client

    def match_comic_rack_list(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadListRequestMatchDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListRequestMatchDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.comic_rack.match_comic_rack_list()
        """
        _response = self._raw_client.match_comic_rack_list(file=file, request_options=request_options)
        return _response.data


class AsyncComicRackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComicRackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComicRackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComicRackClient
        """
        return self._raw_client

    async def match_comic_rack_list(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadListRequestMatchDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListRequestMatchDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comic_rack.match_comic_rack_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.match_comic_rack_list(file=file, request_options=request_options)
        return _response.data
