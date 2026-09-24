

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_notes_response import GetNotesResponse
from .types.get_notes_request_filter_entity_name import GetNotesRequestFilterEntityName
from .types.get_notes_request_sort_field import GetNotesRequestSortField
from .types.get_notes_request_sort_order import GetNotesRequestSortOrder
from pydantic import ValidationError


class RawNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetNotesResponse]:
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
        HttpResponse[GetNotesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "notes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterEntityId": filter_entity_id,
                "filterEntityName": filter_entity_name,
                "filterCreatedById": filter_created_by_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotesResponse,
                    parse_obj_as(
                        type_=GetNotesResponse,
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


class AsyncRawNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetNotesResponse]:
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
        AsyncHttpResponse[GetNotesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notes",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterEntityId": filter_entity_id,
                "filterEntityName": filter_entity_name,
                "filterCreatedById": filter_created_by_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotesResponse,
                    parse_obj_as(
                        type_=GetNotesResponse,
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
