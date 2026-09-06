

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_communication_models_file_upload import ApiPagedResponseCommunicationModelsFileUpload
from ..types.communication_models_field_filter import CommunicationModelsFieldFilter
from .raw_client import AsyncRawFileuploadsClient, RawFileuploadsClient


OMIT = typing.cast(typing.Any, ...)


class FileuploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileuploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileuploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileuploadsClient
        """
        return self._raw_client

    def postreport(
        self,
        *,
        field_filters: typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]] = OMIT,
        include_index_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        include_stored_data_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUpload:
        """
        No Documentation Found.

        Parameters
        ----------
        field_filters : typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]]
            Optional. Filter results by field values. Multiple filters are combined with 'AND' logic.

        include_index_fields : typing.Optional[typing.Sequence[str]]
            Optional. The index data fields to include in the results.
                        By default any index data fields included in FieldFilters will be included.

        include_stored_data_fields : typing.Optional[typing.Sequence[str]]
            Optional. The stored data fields to include in the results.
                        By default stored data fields are omitted in the result.
                        Limit must be 25 or less to return stored data fields.

        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseCommunicationModelsFileUpload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fileuploads.postreport()
        """
        _response = self._raw_client.postreport(
            field_filters=field_filters,
            include_index_fields=include_index_fields,
            include_stored_data_fields=include_stored_data_fields,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data


class AsyncFileuploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileuploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileuploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileuploadsClient
        """
        return self._raw_client

    async def postreport(
        self,
        *,
        field_filters: typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]] = OMIT,
        include_index_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        include_stored_data_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseCommunicationModelsFileUpload:
        """
        No Documentation Found.

        Parameters
        ----------
        field_filters : typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]]
            Optional. Filter results by field values. Multiple filters are combined with 'AND' logic.

        include_index_fields : typing.Optional[typing.Sequence[str]]
            Optional. The index data fields to include in the results.
                        By default any index data fields included in FieldFilters will be included.

        include_stored_data_fields : typing.Optional[typing.Sequence[str]]
            Optional. The stored data fields to include in the results.
                        By default stored data fields are omitted in the result.
                        Limit must be 25 or less to return stored data fields.

        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseCommunicationModelsFileUpload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fileuploads.postreport()


        asyncio.run(main())
        """
        _response = await self._raw_client.postreport(
            field_filters=field_filters,
            include_index_fields=include_index_fields,
            include_stored_data_fields=include_stored_data_fields,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data
