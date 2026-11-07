

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
from ..errors.not_found_error import NotFoundError
from ..types.metadata import Metadata
from ..types.role import Role
from .types.list_merchant_roles_response import ListMerchantRolesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_merchant_roles(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListMerchantRolesResponse]:
        """
        List merchant's custom roles.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMerchantRolesResponse]
            Returns a list of Role objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMerchantRolesResponse,
                    parse_obj_as(
                        type_=ListMerchantRolesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def create_merchant_role(
        self,
        merchant_code: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        metadata: typing.Optional[Metadata] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Role]:
        """
        Create a custom role for the merchant. Roles are defined by the set of permissions that they grant to the members that they are assigned to.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        name : str
            User-defined name of the role.

        permissions : typing.Sequence[str]
            User's permissions.

        metadata : typing.Optional[Metadata]

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Role]
            Returns the Role object after successful custom role creation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "metadata": metadata,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
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

    def get_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Role]:
        """
        Retrieve a custom role by ID.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Role]
            Returns the Role object for a valid identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Role,
                    parse_obj_as(
                        type_=Role,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def delete_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a custom role.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
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

    def update_merchant_role(
        self,
        merchant_code: str,
        role_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Role]:
        """
        Updates a custom role's name, description, or permissions and returns the updated role.

        Providing `permissions` replaces the role's permission list and changes the access granted to members assigned to that role. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        name : typing.Optional[str]
            User-defined name of the role.

        permissions : typing.Optional[typing.Sequence[str]]
            User's permissions.

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Role]
            Returns the updated Role object if the update succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "name": name,
                "permissions": permissions,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
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


class AsyncRawRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_merchant_roles(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListMerchantRolesResponse]:
        """
        List merchant's custom roles.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMerchantRolesResponse]
            Returns a list of Role objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMerchantRolesResponse,
                    parse_obj_as(
                        type_=ListMerchantRolesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def create_merchant_role(
        self,
        merchant_code: str,
        *,
        name: str,
        permissions: typing.Sequence[str],
        metadata: typing.Optional[Metadata] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Role]:
        """
        Create a custom role for the merchant. Roles are defined by the set of permissions that they grant to the members that they are assigned to.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        name : str
            User-defined name of the role.

        permissions : typing.Sequence[str]
            User's permissions.

        metadata : typing.Optional[Metadata]

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Role]
            Returns the Role object after successful custom role creation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "metadata": metadata,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
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

    async def get_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Role]:
        """
        Retrieve a custom role by ID.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Role]
            Returns the Role object for a valid identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Role,
                    parse_obj_as(
                        type_=Role,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def delete_merchant_role(
        self, merchant_code: str, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a custom role.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
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

    async def update_merchant_role(
        self,
        merchant_code: str,
        role_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Role]:
        """
        Updates a custom role's name, description, or permissions and returns the updated role.

        Providing `permissions` replaces the role's permission list and changes the access granted to members assigned to that role. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        role_id : str
            The ID of the role to retrieve.

        name : typing.Optional[str]
            User-defined name of the role.

        permissions : typing.Optional[typing.Sequence[str]]
            User's permissions.

        description : typing.Optional[str]
            User-defined description of the role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Role]
            Returns the updated Role object if the update succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/roles/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "name": name,
                "permissions": permissions,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
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
