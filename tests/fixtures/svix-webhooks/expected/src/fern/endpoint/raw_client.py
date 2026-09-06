

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.endpoint_headers_out import EndpointHeadersOut
from ..types.endpoint_out import EndpointOut
from ..types.endpoint_secret_out import EndpointSecretOut
from ..types.endpoint_stats import EndpointStats
from ..types.http_error_out import HttpErrorOut
from ..types.http_validation_error import HttpValidationError
from ..types.list_response_endpoint_out import ListResponseEndpointOut
from ..types.message_out import MessageOut
from ..types.ordering import Ordering
from ..types.recover_out import RecoverOut
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEndpointClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1endpoint_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseEndpointOut]:
        """
        List the application's endpoints.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseEndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEndpointOut,
                    parse_obj_as(
                        type_=ListResponseEndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_create(
        self,
        app_id: str,
        *,
        url: str,
        idempotency_key: typing.Optional[str] = None,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointOut]:
        """
        Create a new endpoint for the application.

        When `secret` is `null` the secret is automatically generated (recommended)

        Parameters
        ----------
        app_id : str

        url : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        secret : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint",
            method="POST",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "secret": secret,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_get(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointOut]:
        """
        Get an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_update(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        url: str,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointOut]:
        """
        Update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        url : str

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="PUT",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
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
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_delete(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def patch_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointOut]:
        """
        Partially update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        channels : typing.Optional[typing.Sequence[str]]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="PATCH",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
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
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_get_headers(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointHeadersOut]:
        """
        Get the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointHeadersOut]
            The value of the headers is returned in the `headers` field.

            Sensitive headers that have been redacted are returned in the sensitive field.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointHeadersOut,
                    parse_obj_as(
                        type_=EndpointHeadersOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_update_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="PUT",
            json={
                "headers": headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_patch_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Partially set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="PATCH",
            json={
                "headers": headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_recover(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecoverOut]:
        """
        Resend all failed messages since a given time.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : dt.datetime

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecoverOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/recover",
            method="POST",
            json={
                "since": since,
                "until": until,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecoverOut,
                    parse_obj_as(
                        type_=RecoverOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_get_secret(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointSecretOut]:
        """
        Get the endpoint's signing secret.

        This is used to verify the authenticity of the webhook.
        For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointSecretOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/secret",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointSecretOut,
                    parse_obj_as(
                        type_=EndpointSecretOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_rotate_secret(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Rotates the endpoint's signing secret.  The previous secret will be valid for the next 24 hours.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        grace_period_seconds : typing.Optional[int]
            How long the old secret will be valid for, in seconds.

            Valid values are between 0 (immediate expiry) and 7 days. The default is 24 hours.

        key : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/secret/rotate",
            method="POST",
            json={
                "gracePeriodSeconds": grace_period_seconds,
                "key": key,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_send_example(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        event_type: str,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageOut]:
        """
        Send an example message for an event

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        event_type : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/send-example",
            method="POST",
            json={
                "eventType": event_type,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageOut,
                    parse_obj_as(
                        type_=MessageOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1endpoint_get_stats(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        until: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointStats]:
        """
        Get basic statistics for the endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : typing.Optional[dt.datetime]

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointStats]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/stats",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
                "until": serialize_datetime(until) if until is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointStats,
                    parse_obj_as(
                        type_=EndpointStats,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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


class AsyncRawEndpointClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1endpoint_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseEndpointOut]:
        """
        List the application's endpoints.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseEndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEndpointOut,
                    parse_obj_as(
                        type_=ListResponseEndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_create(
        self,
        app_id: str,
        *,
        url: str,
        idempotency_key: typing.Optional[str] = None,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        secret: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointOut]:
        """
        Create a new endpoint for the application.

        When `secret` is `null` the secret is automatically generated (recommended)

        Parameters
        ----------
        app_id : str

        url : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        secret : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint",
            method="POST",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "secret": secret,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_get(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointOut]:
        """
        Get an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_update(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        url: str,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointOut]:
        """
        Update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        url : str

        channels : typing.Optional[typing.Sequence[str]]
            List of message channels this endpoint listens to (omit for all)

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="PUT",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
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
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_delete(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def patch_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointOut]:
        """
        Partially update an endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        channels : typing.Optional[typing.Sequence[str]]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]

        event_types : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this endpoint.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}",
            method="PATCH",
            json={
                "channels": channels,
                "description": description,
                "disabled": disabled,
                "eventTypes": event_types,
                "metadata": metadata,
                "throttleRate": throttle_rate,
                "uid": uid,
                "url": url,
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
                    EndpointOut,
                    parse_obj_as(
                        type_=EndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_get_headers(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointHeadersOut]:
        """
        Get the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointHeadersOut]
            The value of the headers is returned in the `headers` field.

            Sensitive headers that have been redacted are returned in the sensitive field.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointHeadersOut,
                    parse_obj_as(
                        type_=EndpointHeadersOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_update_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="PUT",
            json={
                "headers": headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_patch_headers(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        headers: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Partially set the additional headers to be sent with the webhook

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        headers : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/headers",
            method="PATCH",
            json={
                "headers": headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_recover(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecoverOut]:
        """
        Resend all failed messages since a given time.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : dt.datetime

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecoverOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/recover",
            method="POST",
            json={
                "since": since,
                "until": until,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecoverOut,
                    parse_obj_as(
                        type_=RecoverOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_get_secret(
        self, app_id: str, endpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointSecretOut]:
        """
        Get the endpoint's signing secret.

        This is used to verify the authenticity of the webhook.
        For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointSecretOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/secret",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointSecretOut,
                    parse_obj_as(
                        type_=EndpointSecretOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_rotate_secret(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Rotates the endpoint's signing secret.  The previous secret will be valid for the next 24 hours.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        grace_period_seconds : typing.Optional[int]
            How long the old secret will be valid for, in seconds.

            Valid values are between 0 (immediate expiry) and 7 days. The default is 24 hours.

        key : typing.Optional[str]
            The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/secret/rotate",
            method="POST",
            json={
                "gracePeriodSeconds": grace_period_seconds,
                "key": key,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_send_example(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        event_type: str,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageOut]:
        """
        Send an example message for an event

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        event_type : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/send-example",
            method="POST",
            json={
                "eventType": event_type,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageOut,
                    parse_obj_as(
                        type_=MessageOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1endpoint_get_stats(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        until: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointStats]:
        """
        Get basic statistics for the endpoint.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        since : typing.Optional[dt.datetime]

        until : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointStats]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/stats",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
                "until": serialize_datetime(until) if until is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointStats,
                    parse_obj_as(
                        type_=EndpointStats,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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
