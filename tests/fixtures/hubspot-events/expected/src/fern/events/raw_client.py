

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
from pydantic import ValidationError


class RawEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[CollectionResponseExternalUnifiedEvent]:
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
        HttpResponse[CollectionResponseExternalUnifiedEvent]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "events/v3/events/",
            method="GET",
            params={
                "objectType": object_type,
                "eventType": event_type,
                "occurredAfter": serialize_datetime(occurred_after) if occurred_after is not None else None,
                "occurredBefore": serialize_datetime(occurred_before) if occurred_before is not None else None,
                "objectId": object_id,
                "indexTableName": index_table_name,
                "indexSpecificMetadata": index_specific_metadata,
                "after": after,
                "before": before,
                "limit": limit,
                "sort": sort,
                "objectProperty.{propname}": object_property_propname,
                "property.{propname}": property_propname,
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollectionResponseExternalUnifiedEvent,
                    parse_obj_as(
                        type_=CollectionResponseExternalUnifiedEvent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[CollectionResponseExternalUnifiedEvent]:
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
        AsyncHttpResponse[CollectionResponseExternalUnifiedEvent]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events/v3/events/",
            method="GET",
            params={
                "objectType": object_type,
                "eventType": event_type,
                "occurredAfter": serialize_datetime(occurred_after) if occurred_after is not None else None,
                "occurredBefore": serialize_datetime(occurred_before) if occurred_before is not None else None,
                "objectId": object_id,
                "indexTableName": index_table_name,
                "indexSpecificMetadata": index_specific_metadata,
                "after": after,
                "before": before,
                "limit": limit,
                "sort": sort,
                "objectProperty.{propname}": object_property_propname,
                "property.{propname}": property_propname,
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollectionResponseExternalUnifiedEvent,
                    parse_obj_as(
                        type_=CollectionResponseExternalUnifiedEvent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
