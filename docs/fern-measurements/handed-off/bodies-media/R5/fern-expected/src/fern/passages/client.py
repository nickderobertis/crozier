

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.passage import Passage
from .raw_client import AsyncRawPassagesClient, RawPassagesClient


class PassagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPassagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPassagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPassagesClient
        """
        return self._raw_client

    def get_passage(self, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Passage:
        """
        Parameters
        ----------
        passage_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Passage
            The passage.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.passages.get_passage(
            passage_id="passageId",
        )
        """
        _response = self._raw_client.get_passage(passage_id, request_options=request_options)
        return _response.data


class AsyncPassagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPassagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPassagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPassagesClient
        """
        return self._raw_client

    async def get_passage(self, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Passage:
        """
        Parameters
        ----------
        passage_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Passage
            The passage.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.passages.get_passage(
                passage_id="passageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_passage(passage_id, request_options=request_options)
        return _response.data
