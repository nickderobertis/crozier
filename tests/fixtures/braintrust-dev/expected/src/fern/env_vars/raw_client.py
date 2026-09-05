

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.app_limit_param import AppLimitParam
from ..types.env_var import EnvVar
from ..types.env_var_id_param import EnvVarIdParam
from ..types.env_var_name import EnvVarName
from ..types.env_var_object_id import EnvVarObjectId
from ..types.env_var_object_type import EnvVarObjectType
from ..types.ids import Ids
from .types.get_env_var_response import GetEnvVarResponse
from .types.post_env_var_request_object_type import PostEnvVarRequestObjectType
from .types.put_env_var_request_object_type import PutEnvVarRequestObjectType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEnvVarsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_env_var(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        env_var_name: typing.Optional[EnvVarName] = None,
        object_type: typing.Optional[EnvVarObjectType] = None,
        object_id: typing.Optional[EnvVarObjectId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetEnvVarResponse]:
        """
        List out all env_vars. The env_vars are sorted by creation date, with the most recently-created env_vars coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        env_var_name : typing.Optional[EnvVarName]
            Name of the env_var to search for

        object_type : typing.Optional[EnvVarObjectType]
            The type of the object the environment variable is scoped for

        object_id : typing.Optional[EnvVarObjectId]
            The id of the object the environment variable is scoped for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEnvVarResponse]
            Returns a list of env_var objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="GET",
            params={
                "limit": limit,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "env_var_name": env_var_name,
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEnvVarResponse,
                    parse_obj_as(
                        type_=GetEnvVarResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_env_var(
        self,
        *,
        object_type: PostEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvVar]:
        """
        Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified

        Parameters
        ----------
        object_type : PostEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvVar]
            Returns the new env_var object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def put_env_var(
        self,
        *,
        object_type: PutEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvVar]:
        """
        Create or replace env_var. If there is an existing env_var with the same name as the one specified in the request, will replace the existing env_var with the provided fields

        Parameters
        ----------
        object_type : PutEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvVar]
            Returns the new env_var object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="PUT",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def get_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvVar]:
        """
        Get an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvVar]
            Returns the env_var object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def delete_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvVar]:
        """
        Delete an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvVar]
            Returns the deleted env_var object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def patch_env_var_id(
        self,
        env_var_id: EnvVarIdParam,
        *,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvVar]:
        """
        Partially update an env_var object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvVar]
            Returns the env_var object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="PATCH",
            json={
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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


class AsyncRawEnvVarsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_env_var(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        env_var_name: typing.Optional[EnvVarName] = None,
        object_type: typing.Optional[EnvVarObjectType] = None,
        object_id: typing.Optional[EnvVarObjectId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetEnvVarResponse]:
        """
        List out all env_vars. The env_vars are sorted by creation date, with the most recently-created env_vars coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        env_var_name : typing.Optional[EnvVarName]
            Name of the env_var to search for

        object_type : typing.Optional[EnvVarObjectType]
            The type of the object the environment variable is scoped for

        object_id : typing.Optional[EnvVarObjectId]
            The id of the object the environment variable is scoped for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEnvVarResponse]
            Returns a list of env_var objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="GET",
            params={
                "limit": limit,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "env_var_name": env_var_name,
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEnvVarResponse,
                    parse_obj_as(
                        type_=GetEnvVarResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_env_var(
        self,
        *,
        object_type: PostEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvVar]:
        """
        Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified

        Parameters
        ----------
        object_type : PostEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvVar]
            Returns the new env_var object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def put_env_var(
        self,
        *,
        object_type: PutEnvVarRequestObjectType,
        object_id: str,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvVar]:
        """
        Create or replace env_var. If there is an existing env_var with the same name as the one specified in the request, will replace the existing env_var with the provided fields

        Parameters
        ----------
        object_type : PutEnvVarRequestObjectType
            The type of the object the environment variable is scoped for

        object_id : str
            The id of the object the environment variable is scoped for

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvVar]
            Returns the new env_var object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/env_var",
            method="PUT",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvVar]:
        """
        Get an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvVar]
            Returns the env_var object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def delete_env_var_id(
        self, env_var_id: EnvVarIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvVar]:
        """
        Delete an env_var object by its id

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvVar]
            Returns the deleted env_var object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def patch_env_var_id(
        self,
        env_var_id: EnvVarIdParam,
        *,
        name: str,
        value: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        secret_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvVar]:
        """
        Partially update an env_var object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        env_var_id : EnvVarIdParam
            EnvVar id

        name : str
            The name of the environment variable

        value : typing.Optional[str]
            The value of the environment variable. Will be encrypted at rest.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata associated with the environment variable when managed via the function secrets API

        secret_type : typing.Optional[str]
            Optional classification for the secret (for example, the AI provider name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvVar]
            Returns the env_var object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/env_var/{encode_path_param(env_var_id)}",
            method="PATCH",
            json={
                "name": name,
                "value": value,
                "metadata": metadata,
                "secret_type": secret_type,
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
                    EnvVar,
                    parse_obj_as(
                        type_=EnvVar,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
