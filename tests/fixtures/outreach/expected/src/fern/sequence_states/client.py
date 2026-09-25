

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSequenceStatesClient, RawSequenceStatesClient
from .types.sequence_state_create_request_data import SequenceStateCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class SequenceStatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSequenceStatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSequenceStatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSequenceStatesClient
        """
        return self._raw_client

    def list_sequence_states(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

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
        client.sequence_states.list_sequence_states()
        """
        _response = self._raw_client.list_sequence_states(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_sequence_state(
        self,
        *,
        data: typing.Optional[SequenceStateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceStateCreateRequestData]

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
        client.sequence_states.create_sequence_state()
        """
        _response = self._raw_client.create_sequence_state(data=data, request_options=request_options)
        return _response.data


class AsyncSequenceStatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSequenceStatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSequenceStatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSequenceStatesClient
        """
        return self._raw_client

    async def list_sequence_states(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

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
            await client.sequence_states.list_sequence_states()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sequence_states(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_sequence_state(
        self,
        *,
        data: typing.Optional[SequenceStateCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceStateCreateRequestData]

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
            await client.sequence_states.create_sequence_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sequence_state(data=data, request_options=request_options)
        return _response.data
