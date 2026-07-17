

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.deleted import Deleted
from ..types.patch import Patch
from ..types.validation_authority import ValidationAuthority
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawValidationAuthoritiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_all_client_validators(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ValidationAuthority]]:
        """
        Get all validation authoritiess

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ValidationAuthority]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/client-validators",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ValidationAuthority],
                    parse_obj_as(
                        type_=typing.List[ValidationAuthority],
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

    def create_client_validator(
        self,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ValidationAuthority]:
        """
        Create one validation authorities

        Parameters
        ----------
        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/client-validators",
            method="POST",
            json={
                "alwaysValid": always_valid,
                "badTtl": bad_ttl,
                "description": description,
                "goodTtl": good_ttl,
                "headers": headers,
                "host": host,
                "id": id,
                "method": method,
                "name": name,
                "noCache": no_cache,
                "path": path,
                "timeout": timeout,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    def find_client_validator_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ValidationAuthority]:
        """
        Get one validation authorities by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    def update_client_validator(
        self,
        id_: str,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ValidationAuthority]:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id_ : str
            The validation authorities id

        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id_)}",
            method="PUT",
            json={
                "alwaysValid": always_valid,
                "badTtl": bad_ttl,
                "description": description,
                "goodTtl": good_ttl,
                "headers": headers,
                "host": host,
                "id": id,
                "method": method,
                "name": name,
                "noCache": no_cache,
                "path": path,
                "timeout": timeout,
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
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    def delete_client_validator(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
        """
        Delete one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
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

    def patch_client_validator(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ValidationAuthority]:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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


class AsyncRawValidationAuthoritiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_all_client_validators(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ValidationAuthority]]:
        """
        Get all validation authoritiess

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ValidationAuthority]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/client-validators",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ValidationAuthority],
                    parse_obj_as(
                        type_=typing.List[ValidationAuthority],
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

    async def create_client_validator(
        self,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ValidationAuthority]:
        """
        Create one validation authorities

        Parameters
        ----------
        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/client-validators",
            method="POST",
            json={
                "alwaysValid": always_valid,
                "badTtl": bad_ttl,
                "description": description,
                "goodTtl": good_ttl,
                "headers": headers,
                "host": host,
                "id": id,
                "method": method,
                "name": name,
                "noCache": no_cache,
                "path": path,
                "timeout": timeout,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    async def find_client_validator_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ValidationAuthority]:
        """
        Get one validation authorities by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    async def update_client_validator(
        self,
        id_: str,
        *,
        always_valid: bool,
        bad_ttl: int,
        description: str,
        good_ttl: int,
        headers: typing.Dict[str, str],
        host: str,
        id: str,
        method: str,
        name: str,
        no_cache: bool,
        path: str,
        timeout: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ValidationAuthority]:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id_ : str
            The validation authorities id

        always_valid : bool
            Bypass http calls, every certificates are valids

        bad_ttl : int
            The TTL for invalid access response caching

        description : str
            The description of the settings

        good_ttl : int
            The TTL for valid access response caching

        headers : typing.Dict[str, str]
            HTTP call headers

        host : str
            The host of the server

        id : str
            The id of the settings

        method : str
            The HTTP method

        name : str
            The name of the settings

        no_cache : bool
            Avoid caching responses

        path : str
            The URL path

        timeout : int
            The call timeout

        url : str
            The URL of the server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id_)}",
            method="PUT",
            json={
                "alwaysValid": always_valid,
                "badTtl": bad_ttl,
                "description": description,
                "goodTtl": good_ttl,
                "headers": headers,
                "host": host,
                "id": id,
                "method": method,
                "name": name,
                "noCache": no_cache,
                "path": path,
                "timeout": timeout,
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
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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

    async def delete_client_validator(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
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

    async def patch_client_validator(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ValidationAuthority]:
        """
        Update one validation authorities by id

        Parameters
        ----------
        id : str
            The validation authorities id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValidationAuthority]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/client-validators/{encode_path_param(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValidationAuthority,
                    parse_obj_as(
                        type_=ValidationAuthority,
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
