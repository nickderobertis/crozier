

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
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.daily_activity import DailyActivity
from ..types.error import Error
from pydantic import ValidationError


class RawActivityDetailsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_activity_details_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        kid_id: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Optional[typing.List[DailyActivity]]]]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns an array of per-kid activity arrays, not a flat activity array. Kids are sorted by key when kid_id is omitted. A missing kid may produce a null inner array; filtering with since can produce an empty array.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        kid_id : typing.Optional[str]
            Optional kid UUID. If absent, returns activity lists for all kids in the school.

        since : typing.Optional[dt.datetime]
            Optional RFC3339 timestamp to filter activities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Optional[typing.List[DailyActivity]]]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "activity_details",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "kid_id": kid_id,
                "since": serialize_datetime(since) if since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Optional[typing.List[DailyActivity]]],
                    parse_obj_as(
                        type_=typing.List[typing.Optional[typing.List[DailyActivity]]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
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


class AsyncRawActivityDetailsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_activity_details_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        kid_id: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Optional[typing.List[DailyActivity]]]]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns an array of per-kid activity arrays, not a flat activity array. Kids are sorted by key when kid_id is omitted. A missing kid may produce a null inner array; filtering with since can produce an empty array.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        kid_id : typing.Optional[str]
            Optional kid UUID. If absent, returns activity lists for all kids in the school.

        since : typing.Optional[dt.datetime]
            Optional RFC3339 timestamp to filter activities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Optional[typing.List[DailyActivity]]]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "activity_details",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "kid_id": kid_id,
                "since": serialize_datetime(since) if since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Optional[typing.List[DailyActivity]]],
                    parse_obj_as(
                        type_=typing.List[typing.Optional[typing.List[DailyActivity]]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
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
