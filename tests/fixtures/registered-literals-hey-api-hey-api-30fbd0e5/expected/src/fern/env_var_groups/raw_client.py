

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..types.t_environment_variable import TEnvironmentVariable
from .types.environment_variable_groups_create_response import EnvironmentVariableGroupsCreateResponse
from .types.environment_variable_groups_list_response import EnvironmentVariableGroupsListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEnvVarGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def environment_variable_groups_list(
        self,
        *,
        offset: int,
        limit: int,
        org_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariableGroupsListResponse]:
        """
        List environment variable groups

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariableGroupsListResponse]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/environment-variable-groups/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "orgId": org_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariableGroupsListResponse,
                    parse_obj_as(
                        type_=EnvironmentVariableGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def environment_variable_groups_create(
        self, *, name: str, org_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariableGroupsCreateResponse]:
        """
        Create a new environment variable group

        Parameters
        ----------
        name : str

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariableGroupsCreateResponse]
            An environment variable group
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/environment-variable-groups/",
            method="POST",
            json={
                "name": name,
                "orgId": org_id,
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
                    EnvironmentVariableGroupsCreateResponse,
                    parse_obj_as(
                        type_=EnvironmentVariableGroupsCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def environment_variable_groups_rename(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Rename an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        name : str
            New name for group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def environment_variable_groups_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}",
            method="DELETE",
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

    def environment_variable_groups_get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TEnvironmentVariable]]:
        """
        List variables in an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TEnvironmentVariable]]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TEnvironmentVariable],
                    parse_obj_as(
                        type_=typing.List[TEnvironmentVariable],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def environment_variable_groups_create_variable(
        self,
        id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TEnvironmentVariable]:
        """
        Create an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables",
            method="POST",
            json={
                "value": value,
                "description": description,
                "key": key,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def environment_variable_groups_upsert_variable(
        self,
        id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TEnvironmentVariable]:
        """
        Create or update an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables/{encode_path_param(key)}",
            method="POST",
            json={
                "value": value,
                "description": description,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def environment_variable_groups_variable_delete(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables/{encode_path_param(key)}",
            method="DELETE",
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


class AsyncRawEnvVarGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def environment_variable_groups_list(
        self,
        *,
        offset: int,
        limit: int,
        org_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariableGroupsListResponse]:
        """
        List environment variable groups

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariableGroupsListResponse]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/environment-variable-groups/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "orgId": org_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariableGroupsListResponse,
                    parse_obj_as(
                        type_=EnvironmentVariableGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def environment_variable_groups_create(
        self, *, name: str, org_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvironmentVariableGroupsCreateResponse]:
        """
        Create a new environment variable group

        Parameters
        ----------
        name : str

        org_id : typing.Optional[str]
            Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariableGroupsCreateResponse]
            An environment variable group
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/environment-variable-groups/",
            method="POST",
            json={
                "name": name,
                "orgId": org_id,
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
                    EnvironmentVariableGroupsCreateResponse,
                    parse_obj_as(
                        type_=EnvironmentVariableGroupsCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def environment_variable_groups_rename(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Rename an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        name : str
            New name for group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def environment_variable_groups_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}",
            method="DELETE",
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

    async def environment_variable_groups_get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TEnvironmentVariable]]:
        """
        List variables in an environment variable group

        Parameters
        ----------
        id : str
            Environment variable group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TEnvironmentVariable]]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TEnvironmentVariable],
                    parse_obj_as(
                        type_=typing.List[TEnvironmentVariable],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def environment_variable_groups_create_variable(
        self,
        id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TEnvironmentVariable]:
        """
        Create an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables",
            method="POST",
            json={
                "value": value,
                "description": description,
                "key": key,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def environment_variable_groups_upsert_variable(
        self,
        id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TEnvironmentVariable]:
        """
        Create or update an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables/{encode_path_param(key)}",
            method="POST",
            json={
                "value": value,
                "description": description,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def environment_variable_groups_variable_delete(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an environment variable in a group

        Parameters
        ----------
        id : str
            Environment variable group ID

        key : str
            Environment variable key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/environment-variable-groups/{encode_path_param(id)}/environment-variables/{encode_path_param(key)}",
            method="DELETE",
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
