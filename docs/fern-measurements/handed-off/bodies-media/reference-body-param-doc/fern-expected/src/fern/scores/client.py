

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScoresClient, RawScoresClient


OMIT = typing.cast(typing.Any, ...)


class ScoresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScoresClient
        """
        return self._raw_client

    def submit_score(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.submit_score(request=request, request_options=request_options)
        return _response.data


class AsyncScoresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScoresClient
        """
        return self._raw_client

    async def submit_score(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.submit_score(request=request, request_options=request_options)
        return _response.data
