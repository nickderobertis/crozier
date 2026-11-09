

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.common_event_association import CommonEventAssociation
from ..types.crm_create_or_update_event_response import CrmCreateOrUpdateEventResponse
from ..types.crm_delete_event_response import CrmDeleteEventResponse
from ..types.crm_get_event_response import CrmGetEventResponse
from ..types.crm_get_events_response import CrmGetEventsResponse
from ..types.crm_search_events_response import CrmSearchEventsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrmEventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crm_event_get_event(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetEventResponse]:
        """
        Get details of a event

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetEventResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetEventResponse,
                    parse_obj_as(
                        type_=CrmGetEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_event_delete_event(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CrmDeleteEventResponse]:
        """
        Delete details of an event in a CRM

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmDeleteEventResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmDeleteEventResponse,
                    parse_obj_as(
                        type_=CrmDeleteEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_event_update_event(
        self,
        id: str,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateEventResponse]:
        """
        Update a event

        Parameters
        ----------
        id : str

        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateEventResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonEventAssociation, direction="write"
                ),
                "type": type,
                "subject": subject,
                "startDateTime": start_date_time,
                "endDateTime": end_date_time,
                "isAllDayEvent": is_all_day_event,
                "description": description,
                "location": location,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmCreateOrUpdateEventResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_event_get_events(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetEventsResponse]:
        """
        Get all the events

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetEventsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/events",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetEventsResponse,
                    parse_obj_as(
                        type_=CrmGetEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_event_create_event(
        self,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateEventResponse]:
        """
        Create a new event

        Parameters
        ----------
        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateEventResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/events",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonEventAssociation, direction="write"
                ),
                "type": type,
                "subject": subject,
                "startDateTime": start_date_time,
                "endDateTime": end_date_time,
                "isAllDayEvent": is_all_day_event,
                "description": description,
                "location": location,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmCreateOrUpdateEventResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_event_search_events(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmSearchEventsResponse]:
        """
        Search for events

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmSearchEventsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/events/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmSearchEventsResponse,
                    parse_obj_as(
                        type_=CrmSearchEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCrmEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crm_event_get_event(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetEventResponse]:
        """
        Get details of a event

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetEventResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetEventResponse,
                    parse_obj_as(
                        type_=CrmGetEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_event_delete_event(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CrmDeleteEventResponse]:
        """
        Delete details of an event in a CRM

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmDeleteEventResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmDeleteEventResponse,
                    parse_obj_as(
                        type_=CrmDeleteEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_event_update_event(
        self,
        id: str,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateEventResponse]:
        """
        Update a event

        Parameters
        ----------
        id : str

        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateEventResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/events/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonEventAssociation, direction="write"
                ),
                "type": type,
                "subject": subject,
                "startDateTime": start_date_time,
                "endDateTime": end_date_time,
                "isAllDayEvent": is_all_day_event,
                "description": description,
                "location": location,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmCreateOrUpdateEventResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_event_get_events(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetEventsResponse]:
        """
        Get all the events

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetEventsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/events",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetEventsResponse,
                    parse_obj_as(
                        type_=CrmGetEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_event_create_event(
        self,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateEventResponse]:
        """
        Create a new event

        Parameters
        ----------
        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateEventResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/events",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonEventAssociation, direction="write"
                ),
                "type": type,
                "subject": subject,
                "startDateTime": start_date_time,
                "endDateTime": end_date_time,
                "isAllDayEvent": is_all_day_event,
                "description": description,
                "location": location,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmCreateOrUpdateEventResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_event_search_events(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmSearchEventsResponse]:
        """
        Search for events

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmSearchEventsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/events/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmSearchEventsResponse,
                    parse_obj_as(
                        type_=CrmSearchEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
