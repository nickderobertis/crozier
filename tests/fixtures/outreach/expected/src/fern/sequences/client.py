

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sequence_list_response import SequenceListResponse
from ..types.sequence_response import SequenceResponse
from .raw_client import AsyncRawSequencesClient, RawSequencesClient
from .types.sequence_create_request_data import SequenceCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class SequencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSequencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSequencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSequencesClient
        """
        return self._raw_client

    def list_sequences(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SequenceListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequences.list_sequences()
        """
        _response = self._raw_client.list_sequences(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    def create_sequence(
        self,
        *,
        data: typing.Optional[SequenceCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SequenceResponse:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Sequence created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequences.create_sequence()
        """
        _response = self._raw_client.create_sequence(data=data, request_options=request_options)
        return _response.data

    def get_sequence(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> SequenceResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequences.get_sequence(
            id=1,
        )
        """
        _response = self._raw_client.get_sequence(id, request_options=request_options)
        return _response.data

    def delete_sequence(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequences.delete_sequence(
            id=1,
        )
        """
        _response = self._raw_client.delete_sequence(id, request_options=request_options)
        return _response.data

    def update_sequence(
        self, id: int, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> SequenceResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Sequence updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sequences.update_sequence(
            id=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_sequence(id, request=request, request_options=request_options)
        return _response.data


class AsyncSequencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSequencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSequencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSequencesClient
        """
        return self._raw_client

    async def list_sequences(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SequenceListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequences.list_sequences()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sequences(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    async def create_sequence(
        self,
        *,
        data: typing.Optional[SequenceCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SequenceResponse:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Sequence created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequences.create_sequence()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sequence(data=data, request_options=request_options)
        return _response.data

    async def get_sequence(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SequenceResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequences.get_sequence(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sequence(id, request_options=request_options)
        return _response.data

    async def delete_sequence(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequences.delete_sequence(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sequence(id, request_options=request_options)
        return _response.data

    async def update_sequence(
        self, id: int, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> SequenceResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SequenceResponse
            Sequence updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sequences.update_sequence(
                id=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_sequence(id, request=request, request_options=request_options)
        return _response.data
