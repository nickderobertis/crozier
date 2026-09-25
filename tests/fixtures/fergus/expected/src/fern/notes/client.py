

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_notes_response import GetNotesResponse
from .raw_client import AsyncRawNotesClient, RawNotesClient
from .types.get_notes_request_filter_entity_name import GetNotesRequestFilterEntityName
from .types.get_notes_request_sort_field import GetNotesRequestSortField
from .types.get_notes_request_sort_order import GetNotesRequestSortOrder


class NotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotesClient
        """
        return self._raw_client

    def get_notes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetNotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetNotesRequestSortField] = None,
        filter_entity_id: typing.Optional[float] = None,
        filter_entity_name: typing.Optional[GetNotesRequestFilterEntityName] = None,
        filter_created_by_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotesResponse:
        """
        Schema for Notes

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetNotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetNotesRequestSortField]

        filter_entity_id : typing.Optional[float]
            The entity id to filter notes by

        filter_entity_name : typing.Optional[GetNotesRequestFilterEntityName]

        filter_created_by_id : typing.Optional[float]
            The user id who created the notes to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notes.get_notes()
        """
        _response = self._raw_client.get_notes(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_entity_id=filter_entity_id,
            filter_entity_name=filter_entity_name,
            filter_created_by_id=filter_created_by_id,
            request_options=request_options,
        )
        return _response.data


class AsyncNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotesClient
        """
        return self._raw_client

    async def get_notes(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetNotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetNotesRequestSortField] = None,
        filter_entity_id: typing.Optional[float] = None,
        filter_entity_name: typing.Optional[GetNotesRequestFilterEntityName] = None,
        filter_created_by_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotesResponse:
        """
        Schema for Notes

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetNotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetNotesRequestSortField]

        filter_entity_id : typing.Optional[float]
            The entity id to filter notes by

        filter_entity_name : typing.Optional[GetNotesRequestFilterEntityName]

        filter_created_by_id : typing.Optional[float]
            The user id who created the notes to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notes.get_notes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notes(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_entity_id=filter_entity_id,
            filter_entity_name=filter_entity_name,
            filter_created_by_id=filter_created_by_id,
            request_options=request_options,
        )
        return _response.data
