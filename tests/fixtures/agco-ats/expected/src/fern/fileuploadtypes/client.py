

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_communication_models_file_upload_type import (
    ApiPagedResponseCommunicationModelsFileUploadType,
)
from .raw_client import AsyncRawFileuploadtypesClient, RawFileuploadtypesClient


class FileuploadtypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileuploadtypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileuploadtypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileuploadtypesClient
        """
        return self._raw_client

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUploadType:
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
        ApiPagedResponseCommunicationModelsFileUploadType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fileuploadtypes.get()
        """
        _response = self._raw_client.get(limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncFileuploadtypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileuploadtypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileuploadtypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileuploadtypesClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUploadType:
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
        ApiPagedResponseCommunicationModelsFileUploadType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fileuploadtypes.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(limit=limit, offset=offset, request_options=request_options)
        return _response.data
