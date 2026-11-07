

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.track_event_request_identification import TrackEventRequestIdentification
from .types.track_event_request_metadata_value import TrackEventRequestMetadataValue
from .types.track_event_response import TrackEventResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTrackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def event(
        self,
        *,
        identification: TrackEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrackEventResponse]:
        """
        Endpoint used to track an event for a user or an account.

        Parameters
        ----------
        identification : TrackEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrackEventResponse]
            Object was created
        """
        _response = self._client_wrapper.httpx_client.request(
            "track",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=TrackEventRequestIdentification, direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=typing.Dict[str, TrackEventRequestMetadataValue], direction="write"
                ),
                "name": name,
                "triggeredAt": triggered_at,
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
                    TrackEventResponse,
                    parse_obj_as(
                        type_=TrackEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawTrackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def event(
        self,
        *,
        identification: TrackEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrackEventResponse]:
        """
        Endpoint used to track an event for a user or an account.

        Parameters
        ----------
        identification : TrackEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrackEventResponse]
            Object was created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "track",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=TrackEventRequestIdentification, direction="write"
                ),
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=typing.Dict[str, TrackEventRequestMetadataValue], direction="write"
                ),
                "name": name,
                "triggeredAt": triggered_at,
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
                    TrackEventResponse,
                    parse_obj_as(
                        type_=TrackEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
