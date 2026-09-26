

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.post_v2vectordb_roles_create_response import PostV2VectordbRolesCreateResponse
from .types.post_v2vectordb_roles_describe_response import PostV2VectordbRolesDescribeResponse
from .types.post_v2vectordb_roles_drop_response import PostV2VectordbRolesDropResponse
from .types.post_v2vectordb_roles_grant_privilege_response import PostV2VectordbRolesGrantPrivilegeResponse
from .types.post_v2vectordb_roles_list_response import PostV2VectordbRolesListResponse
from .types.post_v2vectordb_roles_revoke_privilege_response import PostV2VectordbRolesRevokePrivilegeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRoleOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_roles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbRolesListResponse]:
        """
        This operation lists the information about all existing roles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesListResponse]
            A RoleInfo object that contains a list of RoleItem objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/list",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbRolesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesListResponse,
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

    def describe_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbRolesDescribeResponse]:
        """
        This operation describes the details of a specified role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesDescribeResponse]
            An object that contains the detailed desription of a role.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/describe",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesDescribeResponse,
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

    def create_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbRolesCreateResponse]:
        """
        This operation creates the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesCreateResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/create",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesCreateResponse,
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

    def drop_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbRolesDropResponse]:
        """
        This operation drops an existing role. The operation will succeed if the specified role exists. Otherwise, this operation will fail.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesDropResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/drop",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesDropResponse,
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

    def grant_privilege_to_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbRolesGrantPrivilegeResponse]:
        """
        This operation grants a privilege to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
             The type of the object to which the privilege belongs.

        object_name : str
             The name of the object to which the role is granted the specified privilege.

        privilege : str
             The privilege that is granted to the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesGrantPrivilegeResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/grant_privilege",
            method="POST",
            json={
                "roleName": role_name,
                "objectType": object_type,
                "objectName": object_name,
                "privilege": privilege,
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
                    PostV2VectordbRolesGrantPrivilegeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesGrantPrivilegeResponse,
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

    def revoke_privilege_from_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbRolesRevokePrivilegeResponse]:
        """
        This operation revokes a privilege granted to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
            The type of the object to which the privilege belongs.

        object_name : str
            The name of the object to which the role is granted the specified privilege.

        privilege : str
            The privilege that is granted to the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbRolesRevokePrivilegeResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/revoke_privilege",
            method="POST",
            json={
                "roleName": role_name,
                "objectType": object_type,
                "objectName": object_name,
                "privilege": privilege,
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
                    PostV2VectordbRolesRevokePrivilegeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesRevokePrivilegeResponse,
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


class AsyncRawRoleOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_roles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbRolesListResponse]:
        """
        This operation lists the information about all existing roles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesListResponse]
            A RoleInfo object that contains a list of RoleItem objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/list",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbRolesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesListResponse,
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

    async def describe_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbRolesDescribeResponse]:
        """
        This operation describes the details of a specified role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesDescribeResponse]
            An object that contains the detailed desription of a role.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/describe",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesDescribeResponse,
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

    async def create_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbRolesCreateResponse]:
        """
        This operation creates the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesCreateResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/create",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesCreateResponse,
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

    async def drop_role(
        self, *, role_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbRolesDropResponse]:
        """
        This operation drops an existing role. The operation will succeed if the specified role exists. Otherwise, this operation will fail.

        Parameters
        ----------
        role_name : str
            The name of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesDropResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/drop",
            method="POST",
            json={
                "roleName": role_name,
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
                    PostV2VectordbRolesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesDropResponse,
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

    async def grant_privilege_to_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbRolesGrantPrivilegeResponse]:
        """
        This operation grants a privilege to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
             The type of the object to which the privilege belongs.

        object_name : str
             The name of the object to which the role is granted the specified privilege.

        privilege : str
             The privilege that is granted to the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesGrantPrivilegeResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/grant_privilege",
            method="POST",
            json={
                "roleName": role_name,
                "objectType": object_type,
                "objectName": object_name,
                "privilege": privilege,
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
                    PostV2VectordbRolesGrantPrivilegeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesGrantPrivilegeResponse,
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

    async def revoke_privilege_from_role(
        self,
        *,
        role_name: str,
        object_type: str,
        object_name: str,
        privilege: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbRolesRevokePrivilegeResponse]:
        """
        This operation revokes a privilege granted to the current role.

        Parameters
        ----------
        role_name : str
            The name of the role.

        object_type : str
            The type of the object to which the privilege belongs.

        object_name : str
            The name of the object to which the role is granted the specified privilege.

        privilege : str
            The privilege that is granted to the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbRolesRevokePrivilegeResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/roles/revoke_privilege",
            method="POST",
            json={
                "roleName": role_name,
                "objectType": object_type,
                "objectName": object_name,
                "privilege": privilege,
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
                    PostV2VectordbRolesRevokePrivilegeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbRolesRevokePrivilegeResponse,
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
