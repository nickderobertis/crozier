

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_communication_models_file_upload_index_field import (
    ApiPagedResponseCommunicationModelsFileUploadIndexField,
)
from .raw_client import AsyncRawFileuploadindexfieldsClient, RawFileuploadindexfieldsClient


class FileuploadindexfieldsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileuploadindexfieldsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileuploadindexfieldsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileuploadindexfieldsClient
        """
        return self._raw_client

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUploadIndexField:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseCommunicationModelsFileUploadIndexField
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fileuploadindexfields.get()
        """
        _response = self._raw_client.get(limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncFileuploadindexfieldsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileuploadindexfieldsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileuploadindexfieldsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileuploadindexfieldsClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUploadIndexField:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseCommunicationModelsFileUploadIndexField
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fileuploadindexfields.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(limit=limit, offset=offset, request_options=request_options)
        return _response.data
