

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
from .types.delete_user_request_identification import DeleteUserRequestIdentification
from .types.delete_user_response import DeleteUserResponse
from .types.link_request_identification import LinkRequestIdentification
from .types.link_response import LinkResponse
from .types.upsert_user_request_identification import UpsertUserRequestIdentification
from .types.upsert_user_request_properties_value import UpsertUserRequestPropertiesValue
from .types.upsert_user_response import UpsertUserResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def link(
        self,
        *,
        device_id: str,
        identification: LinkRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LinkResponse]:
        """
        💡 You don't need to use this endpoint if you use our JavaScript snippet in your application.

        This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.

        When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named "__journey" will be set.

        This will only work if your website and application are under the same top level domain.

        Website, blog or landing pages
        * www.my-domain.tld
        * blog.my-domain.tld
        * landing-page.my-domain.tld

        Application
        * app.my-domain.tld

        The cookie on my-domain.tld will also be send to your app domain.

        You should call this endpoint after the user succesfully logged in (so that you know the user's ID). Use the value of the cookie as device ID.

        Parameters
        ----------
        device_id : str

        identification : LinkRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LinkResponse]
            Object was created
        """
        _response = self._client_wrapper.httpx_client.request(
            "link",
            method="POST",
            json={
                "deviceId": device_id,
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=LinkRequestIdentification, direction="write"
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
                    LinkResponse,
                    parse_obj_as(
                        type_=LinkResponse,
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

    def delete_user(
        self,
        *,
        identification: DeleteUserRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteUserResponse]:
        """
        Endpoint to delete a user.

        Parameters
        ----------
        identification : DeleteUserRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteUserResponse]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="DELETE",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=DeleteUserRequestIdentification, direction="write"
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
                    DeleteUserResponse,
                    parse_obj_as(
                        type_=DeleteUserResponse,
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

    def upsert_user(
        self,
        *,
        identification: UpsertUserRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertUserResponse]:
        """
        Endpoint to create or update a user.

        Parameters
        ----------
        identification : UpsertUserRequestIdentification
            User identification requires a userId, email or both

        properties : typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpsertUserResponse]
            User will be created
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/upsert",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=UpsertUserRequestIdentification, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Dict[str, UpsertUserRequestPropertiesValue], direction="write"
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
                    UpsertUserResponse,
                    parse_obj_as(
                        type_=UpsertUserResponse,
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


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def link(
        self,
        *,
        device_id: str,
        identification: LinkRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LinkResponse]:
        """
        💡 You don't need to use this endpoint if you use our JavaScript snippet in your application.

        This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.

        When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named "__journey" will be set.

        This will only work if your website and application are under the same top level domain.

        Website, blog or landing pages
        * www.my-domain.tld
        * blog.my-domain.tld
        * landing-page.my-domain.tld

        Application
        * app.my-domain.tld

        The cookie on my-domain.tld will also be send to your app domain.

        You should call this endpoint after the user succesfully logged in (so that you know the user's ID). Use the value of the cookie as device ID.

        Parameters
        ----------
        device_id : str

        identification : LinkRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LinkResponse]
            Object was created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "link",
            method="POST",
            json={
                "deviceId": device_id,
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=LinkRequestIdentification, direction="write"
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
                    LinkResponse,
                    parse_obj_as(
                        type_=LinkResponse,
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

    async def delete_user(
        self,
        *,
        identification: DeleteUserRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteUserResponse]:
        """
        Endpoint to delete a user.

        Parameters
        ----------
        identification : DeleteUserRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteUserResponse]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="DELETE",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=DeleteUserRequestIdentification, direction="write"
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
                    DeleteUserResponse,
                    parse_obj_as(
                        type_=DeleteUserResponse,
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

    async def upsert_user(
        self,
        *,
        identification: UpsertUserRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpsertUserResponse]:
        """
        Endpoint to create or update a user.

        Parameters
        ----------
        identification : UpsertUserRequestIdentification
            User identification requires a userId, email or both

        properties : typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpsertUserResponse]
            User will be created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/upsert",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=UpsertUserRequestIdentification, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Dict[str, UpsertUserRequestPropertiesValue], direction="write"
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
                    UpsertUserResponse,
                    parse_obj_as(
                        type_=UpsertUserResponse,
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
