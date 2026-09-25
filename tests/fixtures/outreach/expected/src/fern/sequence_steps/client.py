

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSequenceStepsClient, RawSequenceStepsClient
from .types.sequence_step_create_request_data import SequenceStepCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class SequenceStepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSequenceStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSequenceStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSequenceStepsClient
        """
        return self._raw_client

    def list_sequence_steps(
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
        client.sequence_steps.list_sequence_steps()
        """
        _response = self._raw_client.list_sequence_steps(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_sequence_step(
        self,
        *,
        data: typing.Optional[SequenceStepCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceStepCreateRequestData]

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
        client.sequence_steps.create_sequence_step()
        """
        _response = self._raw_client.create_sequence_step(data=data, request_options=request_options)
        return _response.data


class AsyncSequenceStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSequenceStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSequenceStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSequenceStepsClient
        """
        return self._raw_client

    async def list_sequence_steps(
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
            await client.sequence_steps.list_sequence_steps()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sequence_steps(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_sequence_step(
        self,
        *,
        data: typing.Optional[SequenceStepCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SequenceStepCreateRequestData]

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
            await client.sequence_steps.create_sequence_step()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sequence_step(data=data, request_options=request_options)
        return _response.data
