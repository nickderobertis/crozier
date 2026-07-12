

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.activities_filter import ActivitiesFilter
from ..types.activity_attendee import ActivityAttendee
from ..types.activity_show_as import ActivityShowAs
from ..types.activity_type import ActivityType
from ..types.address import Address
from ..types.bad_request_response import BadRequestResponse
from ..types.create_activity_response import CreateActivityResponse
from ..types.custom_field import CustomField
from ..types.delete_activity_response import DeleteActivityResponse
from ..types.get_activities_response import GetActivitiesResponse
from ..types.get_activity_response import GetActivityResponse
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_activity_response import UpdateActivityResponse


OMIT = typing.cast(typing.Any, ...)


class RawActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ActivitiesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetActivitiesResponse]:
        """
        List activities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ActivitiesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetActivitiesResponse]
            Activities
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/activities",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ActivitiesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActivitiesResponse,
                    parse_obj_as(
                        type_=GetActivitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add(
        self,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateActivityResponse]:
        """
        Create activity

        Parameters
        ----------
        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateActivityResponse]
            Activity created
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/activities",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account_id": account_id,
                "activity_date": activity_date,
                "activity_datetime": activity_datetime,
                "all_day_event": all_day_event,
                "archived": archived,
                "asset_id": asset_id,
                "attendees": convert_and_respect_annotation_metadata(
                    object_=attendees, annotation=typing.Sequence[ActivityAttendee], direction="write"
                ),
                "campaign_id": campaign_id,
                "case_id": case_id,
                "child": child,
                "company_id": company_id,
                "contact_id": contact_id,
                "contract_id": contract_id,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "custom_object_id": custom_object_id,
                "deleted": deleted,
                "description": description,
                "done": done,
                "downstream_id": downstream_id,
                "duration_minutes": duration_minutes,
                "duration_seconds": duration_seconds,
                "end_date": end_date,
                "end_datetime": end_datetime,
                "event_sub_type": event_sub_type,
                "group_event": group_event,
                "group_event_type": group_event_type,
                "id": id,
                "lead_id": lead_id,
                "location": location,
                "location_address": convert_and_respect_annotation_metadata(
                    object_=location_address, annotation=Address, direction="write"
                ),
                "note": note,
                "opportunity_id": opportunity_id,
                "owner_id": owner_id,
                "private": private,
                "product_id": product_id,
                "recurrent": recurrent,
                "reminder_datetime": reminder_datetime,
                "reminder_set": reminder_set,
                "show_as": show_as,
                "solution_id": solution_id,
                "start_datetime": start_datetime,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "user_id": user_id,
                "video_conference_id": video_conference_id,
                "video_conference_url": video_conference_url,
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
                    CreateActivityResponse,
                    parse_obj_as(
                        type_=CreateActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetActivityResponse]:
        """
        Get activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetActivityResponse]
            Activity
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActivityResponse,
                    parse_obj_as(
                        type_=GetActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteActivityResponse]:
        """
        Delete activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteActivityResponse]
            Activity deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteActivityResponse,
                    parse_obj_as(
                        type_=DeleteActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id_: str,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateActivityResponse]:
        """
        Update activity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateActivityResponse]
            Activity updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account_id": account_id,
                "activity_date": activity_date,
                "activity_datetime": activity_datetime,
                "all_day_event": all_day_event,
                "archived": archived,
                "asset_id": asset_id,
                "attendees": convert_and_respect_annotation_metadata(
                    object_=attendees, annotation=typing.Sequence[ActivityAttendee], direction="write"
                ),
                "campaign_id": campaign_id,
                "case_id": case_id,
                "child": child,
                "company_id": company_id,
                "contact_id": contact_id,
                "contract_id": contract_id,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "custom_object_id": custom_object_id,
                "deleted": deleted,
                "description": description,
                "done": done,
                "downstream_id": downstream_id,
                "duration_minutes": duration_minutes,
                "duration_seconds": duration_seconds,
                "end_date": end_date,
                "end_datetime": end_datetime,
                "event_sub_type": event_sub_type,
                "group_event": group_event,
                "group_event_type": group_event_type,
                "id": id,
                "lead_id": lead_id,
                "location": location,
                "location_address": convert_and_respect_annotation_metadata(
                    object_=location_address, annotation=Address, direction="write"
                ),
                "note": note,
                "opportunity_id": opportunity_id,
                "owner_id": owner_id,
                "private": private,
                "product_id": product_id,
                "recurrent": recurrent,
                "reminder_datetime": reminder_datetime,
                "reminder_set": reminder_set,
                "show_as": show_as,
                "solution_id": solution_id,
                "start_datetime": start_datetime,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "user_id": user_id,
                "video_conference_id": video_conference_id,
                "video_conference_url": video_conference_url,
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
                    UpdateActivityResponse,
                    parse_obj_as(
                        type_=UpdateActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ActivitiesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetActivitiesResponse]:
        """
        List activities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ActivitiesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetActivitiesResponse]
            Activities
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/activities",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ActivitiesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActivitiesResponse,
                    parse_obj_as(
                        type_=GetActivitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add(
        self,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateActivityResponse]:
        """
        Create activity

        Parameters
        ----------
        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateActivityResponse]
            Activity created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/activities",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account_id": account_id,
                "activity_date": activity_date,
                "activity_datetime": activity_datetime,
                "all_day_event": all_day_event,
                "archived": archived,
                "asset_id": asset_id,
                "attendees": convert_and_respect_annotation_metadata(
                    object_=attendees, annotation=typing.Sequence[ActivityAttendee], direction="write"
                ),
                "campaign_id": campaign_id,
                "case_id": case_id,
                "child": child,
                "company_id": company_id,
                "contact_id": contact_id,
                "contract_id": contract_id,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "custom_object_id": custom_object_id,
                "deleted": deleted,
                "description": description,
                "done": done,
                "downstream_id": downstream_id,
                "duration_minutes": duration_minutes,
                "duration_seconds": duration_seconds,
                "end_date": end_date,
                "end_datetime": end_datetime,
                "event_sub_type": event_sub_type,
                "group_event": group_event,
                "group_event_type": group_event_type,
                "id": id,
                "lead_id": lead_id,
                "location": location,
                "location_address": convert_and_respect_annotation_metadata(
                    object_=location_address, annotation=Address, direction="write"
                ),
                "note": note,
                "opportunity_id": opportunity_id,
                "owner_id": owner_id,
                "private": private,
                "product_id": product_id,
                "recurrent": recurrent,
                "reminder_datetime": reminder_datetime,
                "reminder_set": reminder_set,
                "show_as": show_as,
                "solution_id": solution_id,
                "start_datetime": start_datetime,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "user_id": user_id,
                "video_conference_id": video_conference_id,
                "video_conference_url": video_conference_url,
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
                    CreateActivityResponse,
                    parse_obj_as(
                        type_=CreateActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetActivityResponse]:
        """
        Get activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetActivityResponse]
            Activity
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActivityResponse,
                    parse_obj_as(
                        type_=GetActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteActivityResponse]:
        """
        Delete activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteActivityResponse]
            Activity deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteActivityResponse,
                    parse_obj_as(
                        type_=DeleteActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id_: str,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateActivityResponse]:
        """
        Update activity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateActivityResponse]
            Activity updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/activities/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account_id": account_id,
                "activity_date": activity_date,
                "activity_datetime": activity_datetime,
                "all_day_event": all_day_event,
                "archived": archived,
                "asset_id": asset_id,
                "attendees": convert_and_respect_annotation_metadata(
                    object_=attendees, annotation=typing.Sequence[ActivityAttendee], direction="write"
                ),
                "campaign_id": campaign_id,
                "case_id": case_id,
                "child": child,
                "company_id": company_id,
                "contact_id": contact_id,
                "contract_id": contract_id,
                "created_at": created_at,
                "created_by": created_by,
                "custom_fields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=typing.Sequence[CustomField], direction="write"
                ),
                "custom_object_id": custom_object_id,
                "deleted": deleted,
                "description": description,
                "done": done,
                "downstream_id": downstream_id,
                "duration_minutes": duration_minutes,
                "duration_seconds": duration_seconds,
                "end_date": end_date,
                "end_datetime": end_datetime,
                "event_sub_type": event_sub_type,
                "group_event": group_event,
                "group_event_type": group_event_type,
                "id": id,
                "lead_id": lead_id,
                "location": location,
                "location_address": convert_and_respect_annotation_metadata(
                    object_=location_address, annotation=Address, direction="write"
                ),
                "note": note,
                "opportunity_id": opportunity_id,
                "owner_id": owner_id,
                "private": private,
                "product_id": product_id,
                "recurrent": recurrent,
                "reminder_datetime": reminder_datetime,
                "reminder_set": reminder_set,
                "show_as": show_as,
                "solution_id": solution_id,
                "start_datetime": start_datetime,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "user_id": user_id,
                "video_conference_id": video_conference_id,
                "video_conference_url": video_conference_url,
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
                    UpdateActivityResponse,
                    parse_obj_as(
                        type_=UpdateActivityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
