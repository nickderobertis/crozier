

import datetime as dt
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
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.v1day_property import V1DayProperty
from .types.v1day_properties_create_day_property import V1DayPropertiesCreateDayProperty
from .types.v1day_properties_update_day_property import V1DayPropertiesUpdateDayProperty
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDayPropertiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_day_properties(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        dates: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1DayProperty]]:
        """
        Retrieve day properties (locked days) for users in the account. Day properties control whether time entries can be modified for specific dates.

        You can filter by date range using `since` and `until` parameters, or by specific dates using the `dates` parameter.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for filtering (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for filtering (YYYY-MM-DD)

        dates : typing.Optional[str]
            Comma-separated list of specific dates (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1DayProperty]]
            Day properties retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "dates": dates,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def create_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesCreateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1DayProperty]]:
        """
        Create or update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        When a day is locked, users cannot create, update, or delete time entries for that date. Only users with appropriate permissions (admins or managers) can lock/unlock days.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesCreateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1DayProperty]]
            Day properties created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="POST",
            json={
                "day_property": convert_and_respect_annotation_metadata(
                    object_=day_property, annotation=V1DayPropertiesCreateDayProperty, direction="write"
                ),
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
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesUpdateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1DayProperty]]:
        """
        Update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        Use `locked: false` to unlock previously locked days, allowing users to modify time entries for those dates again.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesUpdateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1DayProperty]]
            Day properties updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="PUT",
            json={
                "day_property": convert_and_respect_annotation_metadata(
                    object_=day_property, annotation=V1DayPropertiesUpdateDayProperty, direction="write"
                ),
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
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawDayPropertiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_day_properties(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        dates: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1DayProperty]]:
        """
        Retrieve day properties (locked days) for users in the account. Day properties control whether time entries can be modified for specific dates.

        You can filter by date range using `since` and `until` parameters, or by specific dates using the `dates` parameter.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for filtering (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for filtering (YYYY-MM-DD)

        dates : typing.Optional[str]
            Comma-separated list of specific dates (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1DayProperty]]
            Day properties retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "dates": dates,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def create_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesCreateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1DayProperty]]:
        """
        Create or update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        When a day is locked, users cannot create, update, or delete time entries for that date. Only users with appropriate permissions (admins or managers) can lock/unlock days.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesCreateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1DayProperty]]
            Day properties created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="POST",
            json={
                "day_property": convert_and_respect_annotation_metadata(
                    object_=day_property, annotation=V1DayPropertiesCreateDayProperty, direction="write"
                ),
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
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesUpdateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1DayProperty]]:
        """
        Update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        Use `locked: false` to unlock previously locked days, allowing users to modify time entries for those dates again.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesUpdateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1DayProperty]]
            Day properties updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/day_properties",
            method="PUT",
            json={
                "day_property": convert_and_respect_annotation_metadata(
                    object_=day_property, annotation=V1DayPropertiesUpdateDayProperty, direction="write"
                ),
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
                    typing.List[V1DayProperty],
                    parse_obj_as(
                        type_=typing.List[V1DayProperty],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
