

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sm_context_create_data import SmContextCreateData
from ..types.sm_context_created_data import SmContextCreatedData
from .raw_client import AsyncRawSmContextsCollectionClient, RawSmContextsCollectionClient


OMIT = typing.cast(typing.Any, ...)


class SmContextsCollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSmContextsCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSmContextsCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSmContextsCollectionClient
        """
        return self._raw_client

    def post_sm_contexts(
        self,
        *,
        json_data: typing.Optional[SmContextCreateData] = OMIT,
        binary_data_n1sm_message: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmContextCreatedData:
        """
        Parameters
        ----------
        json_data : typing.Optional[SmContextCreateData]

        binary_data_n1sm_message : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmContextCreatedData
            successful creation of an SM context

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sm_contexts_collection.post_sm_contexts()
        """
        _response = self._raw_client.post_sm_contexts(
            json_data=json_data, binary_data_n1sm_message=binary_data_n1sm_message, request_options=request_options
        )
        return _response.data


class AsyncSmContextsCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSmContextsCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSmContextsCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSmContextsCollectionClient
        """
        return self._raw_client

    async def post_sm_contexts(
        self,
        *,
        json_data: typing.Optional[SmContextCreateData] = OMIT,
        binary_data_n1sm_message: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmContextCreatedData:
        """
        Parameters
        ----------
        json_data : typing.Optional[SmContextCreateData]

        binary_data_n1sm_message : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmContextCreatedData
            successful creation of an SM context

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sm_contexts_collection.post_sm_contexts()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_sm_contexts(
            json_data=json_data, binary_data_n1sm_message=binary_data_n1sm_message, request_options=request_options
        )
        return _response.data
