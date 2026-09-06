

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
from ..errors.bad_request_error import BadRequestError
from ..types.age_restriction_update_dto import AgeRestrictionUpdateDto
from ..types.authentication_activity_dto import AuthenticationActivityDto
from ..types.page_authentication_activity_dto import PageAuthenticationActivityDto
from ..types.shared_libraries_update_dto import SharedLibrariesUpdateDto
from ..types.user_dto import UserDto
from ..types.validation_error_response import ValidationErrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UserDto]]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[UserDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UserDto],
                    parse_obj_as(
                        type_=typing.List[UserDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def add_user(
        self,
        *,
        email: str,
        password: str,
        roles: typing.Sequence[str],
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        email : str

        password : str

        roles : typing.Sequence[str]

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserDto]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/users",
            method="POST",
            json={
                "ageRestriction": convert_and_respect_annotation_metadata(
                    object_=age_restriction, annotation=AgeRestrictionUpdateDto, direction="write"
                ),
                "email": email,
                "labelsAllow": labels_allow,
                "labelsExclude": labels_exclude,
                "password": password,
                "roles": roles,
                "sharedLibraries": convert_and_respect_annotation_metadata(
                    object_=shared_libraries, annotation=SharedLibrariesUpdateDto, direction="write"
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
                    UserDto,
                    parse_obj_as(
                        type_=UserDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def get_authentication_activity(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageAuthenticationActivityDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageAuthenticationActivityDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/users/authentication-activity",
            method="GET",
            params={
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageAuthenticationActivityDto,
                    parse_obj_as(
                        type_=PageAuthenticationActivityDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def delete_user_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def update_user_by_id(
        self,
        id: str,
        *,
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        roles : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}",
            method="PATCH",
            json={
                "ageRestriction": convert_and_respect_annotation_metadata(
                    object_=age_restriction, annotation=AgeRestrictionUpdateDto, direction="write"
                ),
                "labelsAllow": labels_allow,
                "labelsExclude": labels_exclude,
                "roles": roles,
                "sharedLibraries": convert_and_respect_annotation_metadata(
                    object_=shared_libraries, annotation=SharedLibrariesUpdateDto, direction="write"
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
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def get_latest_authentication_activity_by_user_id(
        self,
        id: str,
        *,
        apikey_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AuthenticationActivityDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        apikey_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AuthenticationActivityDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}/authentication-activity/latest",
            method="GET",
            params={
                "apikey_id": apikey_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthenticationActivityDto,
                    parse_obj_as(
                        type_=AuthenticationActivityDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def update_password_by_user_id(
        self, id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}/password",
            method="PATCH",
            json={
                "password": password,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UserDto]]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[UserDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UserDto],
                    parse_obj_as(
                        type_=typing.List[UserDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def add_user(
        self,
        *,
        email: str,
        password: str,
        roles: typing.Sequence[str],
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        email : str

        password : str

        roles : typing.Sequence[str]

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserDto]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/users",
            method="POST",
            json={
                "ageRestriction": convert_and_respect_annotation_metadata(
                    object_=age_restriction, annotation=AgeRestrictionUpdateDto, direction="write"
                ),
                "email": email,
                "labelsAllow": labels_allow,
                "labelsExclude": labels_exclude,
                "password": password,
                "roles": roles,
                "sharedLibraries": convert_and_respect_annotation_metadata(
                    object_=shared_libraries, annotation=SharedLibrariesUpdateDto, direction="write"
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
                    UserDto,
                    parse_obj_as(
                        type_=UserDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def get_authentication_activity(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageAuthenticationActivityDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageAuthenticationActivityDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/users/authentication-activity",
            method="GET",
            params={
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageAuthenticationActivityDto,
                    parse_obj_as(
                        type_=PageAuthenticationActivityDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def delete_user_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def update_user_by_id(
        self,
        id: str,
        *,
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        roles : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}",
            method="PATCH",
            json={
                "ageRestriction": convert_and_respect_annotation_metadata(
                    object_=age_restriction, annotation=AgeRestrictionUpdateDto, direction="write"
                ),
                "labelsAllow": labels_allow,
                "labelsExclude": labels_exclude,
                "roles": roles,
                "sharedLibraries": convert_and_respect_annotation_metadata(
                    object_=shared_libraries, annotation=SharedLibrariesUpdateDto, direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def get_latest_authentication_activity_by_user_id(
        self,
        id: str,
        *,
        apikey_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AuthenticationActivityDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        apikey_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AuthenticationActivityDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}/authentication-activity/latest",
            method="GET",
            params={
                "apikey_id": apikey_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthenticationActivityDto,
                    parse_obj_as(
                        type_=AuthenticationActivityDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def update_password_by_user_id(
        self, id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/users/{encode_path_param(id)}/password",
            method="PATCH",
            json={
                "password": password,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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
