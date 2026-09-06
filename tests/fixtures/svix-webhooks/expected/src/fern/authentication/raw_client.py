

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.app_portal_access_out import AppPortalAccessOut
from ..types.application_in import ApplicationIn
from ..types.http_error_out import HttpErrorOut
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1authentication_app_portal_access(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        feature_flags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AppPortalAccessOut]:
        """
        Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        feature_flags : typing.Optional[typing.Sequence[str]]
            The set of feature flags the created token will have access to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppPortalAccessOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/auth/app-portal-access/{encode_path_param(app_id)}",
            method="POST",
            json={
                "application": convert_and_respect_annotation_metadata(
                    object_=application, annotation=ApplicationIn, direction="write"
                ),
                "featureFlags": feature_flags,
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
                    AppPortalAccessOut,
                    parse_obj_as(
                        type_=AppPortalAccessOut,
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

    def logout_api_v1auth_logout_post(
        self, *, idempotency_key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """

        Logout an app token.

        Trying to log out other tokens will fail.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/auth/logout",
            method="POST",
            headers={
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1authentication_app_portal_access(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        feature_flags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AppPortalAccessOut]:
        """
        Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        feature_flags : typing.Optional[typing.Sequence[str]]
            The set of feature flags the created token will have access to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppPortalAccessOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/auth/app-portal-access/{encode_path_param(app_id)}",
            method="POST",
            json={
                "application": convert_and_respect_annotation_metadata(
                    object_=application, annotation=ApplicationIn, direction="write"
                ),
                "featureFlags": feature_flags,
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
                    AppPortalAccessOut,
                    parse_obj_as(
                        type_=AppPortalAccessOut,
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

    async def logout_api_v1auth_logout_post(
        self, *, idempotency_key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """

        Logout an app token.

        Trying to log out other tokens will fail.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/auth/logout",
            method="POST",
            headers={
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
