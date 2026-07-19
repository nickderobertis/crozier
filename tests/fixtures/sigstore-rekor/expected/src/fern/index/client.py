

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.error import Error
from .raw_client import AsyncRawIndexClient, RawIndexClient
from .types.search_index_operator import SearchIndexOperator
from .types.search_index_public_key import SearchIndexPublicKey


OMIT = typing.cast(typing.Any, ...)


class IndexClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndexClient
        """
        return self._raw_client

    def search_index(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        operator: typing.Optional[SearchIndexOperator] = OMIT,
        public_key: typing.Optional[SearchIndexPublicKey] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases.
        The results returned from this endpoint may be incomplete.

        Parameters
        ----------
        email : typing.Optional[str]

        hash : typing.Optional[str]

        operator : typing.Optional[SearchIndexOperator]

        public_key : typing.Optional[SearchIndexPublicKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.index.search_index()
        """
        _response = self._raw_client.search_index(
            email=email, hash=hash, operator=operator, public_key=public_key, request_options=request_options
        )
        return _response.data


class AsyncIndexClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndexClient
        """
        return self._raw_client

    async def search_index(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        operator: typing.Optional[SearchIndexOperator] = OMIT,
        public_key: typing.Optional[SearchIndexPublicKey] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Error:
        """
        EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases.
        The results returned from this endpoint may be incomplete.

        Parameters
        ----------
        email : typing.Optional[str]

        hash : typing.Optional[str]

        operator : typing.Optional[SearchIndexOperator]

        public_key : typing.Optional[SearchIndexPublicKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Error
            An issue occurred while processing the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.index.search_index()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_index(
            email=email, hash=hash, operator=operator, public_key=public_key, request_options=request_options
        )
        return _response.data
