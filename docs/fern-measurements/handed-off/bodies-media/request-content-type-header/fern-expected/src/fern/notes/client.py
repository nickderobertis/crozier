

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotesClient, RawNotesClient


OMIT = typing.cast(typing.Any, ...)


class NotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotesClient
        """
        return self._raw_client

    def add_note(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        text : typing.Optional[str]

        author : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notes.add_note()
        """
        _response = self._raw_client.add_note(text=text, author=author, request_options=request_options)
        return _response.data


class AsyncNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotesClient
        """
        return self._raw_client

    async def add_note(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        text : typing.Optional[str]

        author : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notes.add_note()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_note(text=text, author=author, request_options=request_options)
        return _response.data
