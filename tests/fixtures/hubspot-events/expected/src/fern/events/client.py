

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
from .raw_client import AsyncRawEventsClient, RawEventsClient


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def get_events_v3events_get_page(
        self,
        *,
        object_type: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        occurred_after: typing.Optional[dt.datetime] = None,
        occurred_before: typing.Optional[dt.datetime] = None,
        object_id: typing.Optional[int] = None,
        index_table_name: typing.Optional[str] = None,
        index_specific_metadata: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        object_property_propname: typing.Optional[typing.Dict[str, typing.Any]] = None,
        property_propname: typing.Optional[typing.Dict[str, typing.Any]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionResponseExternalUnifiedEvent:
        """
        Parameters
        ----------
        object_type : typing.Optional[str]

        event_type : typing.Optional[str]

        occurred_after : typing.Optional[dt.datetime]

        occurred_before : typing.Optional[dt.datetime]

        object_id : typing.Optional[int]

        index_table_name : typing.Optional[str]

        index_specific_metadata : typing.Optional[str]

        after : typing.Optional[str]
            The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.

        before : typing.Optional[str]

        limit : typing.Optional[int]
            The maximum number of results to display per page.

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        object_property_propname : typing.Optional[typing.Dict[str, typing.Any]]

        property_propname : typing.Optional[typing.Dict[str, typing.Any]]

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionResponseExternalUnifiedEvent
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
            token="YOUR_TOKEN",
        )
        client.events.get_events_v3events_get_page()
        """
        _response = self._raw_client.get_events_v3events_get_page(
            object_type=object_type,
            event_type=event_type,
            occurred_after=occurred_after,
            occurred_before=occurred_before,
            object_id=object_id,
            index_table_name=index_table_name,
            index_specific_metadata=index_specific_metadata,
            after=after,
            before=before,
            limit=limit,
            sort=sort,
            object_property_propname=object_property_propname,
            property_propname=property_propname,
            id=id,
            request_options=request_options,
        )
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def get_events_v3events_get_page(
        self,
        *,
        object_type: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        occurred_after: typing.Optional[dt.datetime] = None,
        occurred_before: typing.Optional[dt.datetime] = None,
        object_id: typing.Optional[int] = None,
        index_table_name: typing.Optional[str] = None,
        index_specific_metadata: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        object_property_propname: typing.Optional[typing.Dict[str, typing.Any]] = None,
        property_propname: typing.Optional[typing.Dict[str, typing.Any]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionResponseExternalUnifiedEvent:
        """
        Parameters
        ----------
        object_type : typing.Optional[str]

        event_type : typing.Optional[str]

        occurred_after : typing.Optional[dt.datetime]

        occurred_before : typing.Optional[dt.datetime]

        object_id : typing.Optional[int]

        index_table_name : typing.Optional[str]

        index_specific_metadata : typing.Optional[str]

        after : typing.Optional[str]
            The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.

        before : typing.Optional[str]

        limit : typing.Optional[int]
            The maximum number of results to display per page.

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        object_property_propname : typing.Optional[typing.Dict[str, typing.Any]]

        property_propname : typing.Optional[typing.Dict[str, typing.Any]]

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionResponseExternalUnifiedEvent
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            private_app_legacy="YOUR_PRIVATE_APP_LEGACY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.get_events_v3events_get_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events_v3events_get_page(
            object_type=object_type,
            event_type=event_type,
            occurred_after=occurred_after,
            occurred_before=occurred_before,
            object_id=object_id,
            index_table_name=index_table_name,
            index_specific_metadata=index_specific_metadata,
            after=after,
            before=before,
            limit=limit,
            sort=sort,
            object_property_propname=object_property_propname,
            property_propname=property_propname,
            id=id,
            request_options=request_options,
        )
        return _response.data
