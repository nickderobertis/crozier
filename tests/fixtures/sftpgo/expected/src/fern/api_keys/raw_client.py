

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_key import ApiKey
from ..types.api_key_scope import ApiKeyScope
from ..types.api_response import ApiResponse
from .types.add_api_key_response import AddApiKeyResponse
from .types.get_api_keys_request_order import GetApiKeysRequestOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_keys(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetApiKeysRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ApiKey]]:
        """
        Returns an array with one or more API keys. For security reasons hashed keys are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetApiKeysRequestOrder]
            Ordering API keys by id. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ApiKey]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "apikeys",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def add_api_key(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddApiKeyResponse]:
        """
        Adds a new API key

        Parameters
        ----------
        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddApiKeyResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "apikeys",
            method="POST",
            json={
                "id": id,
                "name": name,
                "key": key,
                "scope": scope,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_use_at": last_use_at,
                "expires_at": expires_at,
                "description": description,
                "user": user,
                "admin": admin,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddApiKeyResponse,
                    parse_obj_as(
                        type_=AddApiKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def get_api_key_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKey]:
        """
        Returns the API key with the given id, if it exists. For security reasons the hashed key is omitted in the response

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def update_api_key(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Updates an existing API key. You cannot update the key itself, the creation date and the last use

        Parameters
        ----------
        id_ : str
            the key id

        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id_)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "key": key,
                "scope": scope,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_use_at": last_use_at,
                "expires_at": expires_at,
                "description": description,
                "user": user,
                "admin": admin,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def delete_api_key(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiResponse]:
        """
        Deletes an existing API key

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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


class AsyncRawApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_keys(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetApiKeysRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ApiKey]]:
        """
        Returns an array with one or more API keys. For security reasons hashed keys are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetApiKeysRequestOrder]
            Ordering API keys by id. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ApiKey]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apikeys",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def add_api_key(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddApiKeyResponse]:
        """
        Adds a new API key

        Parameters
        ----------
        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddApiKeyResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apikeys",
            method="POST",
            json={
                "id": id,
                "name": name,
                "key": key,
                "scope": scope,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_use_at": last_use_at,
                "expires_at": expires_at,
                "description": description,
                "user": user,
                "admin": admin,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddApiKeyResponse,
                    parse_obj_as(
                        type_=AddApiKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def get_api_key_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Returns the API key with the given id, if it exists. For security reasons the hashed key is omitted in the response

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def update_api_key(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Updates an existing API key. You cannot update the key itself, the creation date and the last use

        Parameters
        ----------
        id_ : str
            the key id

        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id_)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "key": key,
                "scope": scope,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_use_at": last_use_at,
                "expires_at": expires_at,
                "description": description,
                "user": user,
                "admin": admin,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def delete_api_key(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Deletes an existing API key

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apikeys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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
