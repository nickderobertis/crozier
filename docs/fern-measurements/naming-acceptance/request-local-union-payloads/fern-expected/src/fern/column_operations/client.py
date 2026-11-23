

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.update_job import UpdateJob
from .raw_client import AsyncRawColumnOperationsClient, RawColumnOperationsClient
from .types.update_data_lite_input_input_options import UpdateDataLiteInputInputOptions


OMIT = typing.cast(typing.Any, ...)


class ColumnOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawColumnOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawColumnOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawColumnOperationsClient
        """
        return self._raw_client

    def update_block_data(
        self,
        model_id: str,
        *,
        comment: str,
        input_options: typing.Optional[UpdateDataLiteInputInputOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateJob:
        """
        Parameters
        ----------
        model_id : str

        comment : str

        input_options : typing.Optional[UpdateDataLiteInputInputOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateJob
            The update job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.column_operations.update_block_data(
            model_id="model_id",
            comment="comment",
        )
        """
        _response = self._raw_client.update_block_data(
            model_id, comment=comment, input_options=input_options, request_options=request_options
        )
        return _response.data


class AsyncColumnOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawColumnOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawColumnOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawColumnOperationsClient
        """
        return self._raw_client

    async def update_block_data(
        self,
        model_id: str,
        *,
        comment: str,
        input_options: typing.Optional[UpdateDataLiteInputInputOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateJob:
        """
        Parameters
        ----------
        model_id : str

        comment : str

        input_options : typing.Optional[UpdateDataLiteInputInputOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateJob
            The update job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.column_operations.update_block_data(
                model_id="model_id",
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_block_data(
            model_id, comment=comment, input_options=input_options, request_options=request_options
        )
        return _response.data
