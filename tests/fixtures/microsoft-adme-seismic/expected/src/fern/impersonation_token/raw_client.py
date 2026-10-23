

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.impersonation_token import ImpersonationToken
from ..types.resource import Resource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImpersonationTokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate(
        self,
        *,
        user_token: str,
        resources: typing.Sequence[Resource],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImpersonationToken]:
        """
        <ul><li>Generate a credential token to impersonate user access for a set of subproject resources.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        user_token : str
            The credential of the user to impersonate.

        resources : typing.Sequence[Resource]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImpersonationToken]
            The impersonation token has been successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "impersonation-token",
            method="POST",
            json={
                "resources": convert_and_respect_annotation_metadata(
                    object_=resources, annotation=typing.Sequence[Resource], direction="write"
                ),
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
                "user-token": str(user_token) if user_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImpersonationToken,
                    parse_obj_as(
                        type_=ImpersonationToken,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def refresh(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImpersonationToken]:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        impersonation_token : str
            The impersonation token to refresh.

        impersonation_token_context : str
            The impersonation token context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImpersonationToken]
            Refreshed impersonation credential token successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "impersonation-token",
            method="PUT",
            headers={
                "impersonation-token": str(impersonation_token) if impersonation_token is not None else None,
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImpersonationToken,
                    parse_obj_as(
                        type_=ImpersonationToken,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawImpersonationTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate(
        self,
        *,
        user_token: str,
        resources: typing.Sequence[Resource],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImpersonationToken]:
        """
        <ul><li>Generate a credential token to impersonate user access for a set of subproject resources.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        user_token : str
            The credential of the user to impersonate.

        resources : typing.Sequence[Resource]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImpersonationToken]
            The impersonation token has been successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "impersonation-token",
            method="POST",
            json={
                "resources": convert_and_respect_annotation_metadata(
                    object_=resources, annotation=typing.Sequence[Resource], direction="write"
                ),
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
                "user-token": str(user_token) if user_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImpersonationToken,
                    parse_obj_as(
                        type_=ImpersonationToken,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def refresh(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImpersonationToken]:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        impersonation_token : str
            The impersonation token to refresh.

        impersonation_token_context : str
            The impersonation token context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImpersonationToken]
            Refreshed impersonation credential token successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "impersonation-token",
            method="PUT",
            headers={
                "impersonation-token": str(impersonation_token) if impersonation_token is not None else None,
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImpersonationToken,
                    parse_obj_as(
                        type_=ImpersonationToken,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
