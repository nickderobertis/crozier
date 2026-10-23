

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.organization_id import OrganizationId
from .types.create_user_request_role import CreateUserRequestRole
from .types.create_user_response import CreateUserResponse
from .types.get_users_request_filter_date_field import GetUsersRequestFilterDateField
from .types.get_users_request_order import GetUsersRequestOrder
from .types.get_users_request_sort_by import GetUsersRequestSortBy
from .types.get_users_response import GetUsersResponse
from .types.update_user_request_role import UpdateUserRequestRole
from .types.update_user_response import UpdateUserResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOrganizationsApiUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetUsersRequestSortBy] = None,
        order: typing.Optional[GetUsersRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetUsersRequestFilterDateField] = None,
        id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetUsersResponse]:
        """
        Gets users from the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetUsersRequestSortBy]
            Sort by field

        order : typing.Optional[GetUsersRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetUsersRequestFilterDateField]
            Date field to filter by

        id : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUsersResponse]
            Users retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "id": id,
                "email": email,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUsersResponse,
                    parse_obj_as(
                        type_=GetUsersResponse,
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

    def create_user(
        self,
        organization_id: OrganizationId,
        *,
        name: str,
        email: str,
        role: CreateUserRequestRole,
        is_active: typing.Optional[bool] = OMIT,
        teams: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateUserResponse]:
        """
        Create a new user in the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        name : str
            The name of the user

        email : str
            The email of the user

        role : CreateUserRequestRole
            The role of the user in the organization

        is_active : typing.Optional[bool]
            Whether the user is active

        teams : typing.Optional[typing.Sequence[str]]
            The list of teams the user is a member of

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateUserResponse]
            User created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="POST",
            json={
                "isActive": is_active,
                "name": name,
                "email": email,
                "role": role,
                "teams": teams,
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
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
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

    def update_user(
        self,
        organization_id: OrganizationId,
        *,
        email: str,
        is_active: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        role: typing.Optional[UpdateUserRequestRole] = OMIT,
        teams: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateUserResponse]:
        """
        Updates an existing user in the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        email : str
            The email of the user

        is_active : typing.Optional[bool]
            Whether the user is active

        name : typing.Optional[str]

        role : typing.Optional[UpdateUserRequestRole]
            The role of the user in the organization

        teams : typing.Optional[typing.Sequence[str]]
            The list of teams the user is a member of

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateUserResponse]
            User updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="PATCH",
            json={
                "isActive": is_active,
                "name": name,
                "email": email,
                "role": role,
                "teams": teams,
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
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
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


class AsyncRawOrganizationsApiUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_users(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetUsersRequestSortBy] = None,
        order: typing.Optional[GetUsersRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetUsersRequestFilterDateField] = None,
        id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetUsersResponse]:
        """
        Gets users from the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetUsersRequestSortBy]
            Sort by field

        order : typing.Optional[GetUsersRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetUsersRequestFilterDateField]
            Date field to filter by

        id : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUsersResponse]
            Users retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "id": id,
                "email": email,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUsersResponse,
                    parse_obj_as(
                        type_=GetUsersResponse,
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

    async def create_user(
        self,
        organization_id: OrganizationId,
        *,
        name: str,
        email: str,
        role: CreateUserRequestRole,
        is_active: typing.Optional[bool] = OMIT,
        teams: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateUserResponse]:
        """
        Create a new user in the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        name : str
            The name of the user

        email : str
            The email of the user

        role : CreateUserRequestRole
            The role of the user in the organization

        is_active : typing.Optional[bool]
            Whether the user is active

        teams : typing.Optional[typing.Sequence[str]]
            The list of teams the user is a member of

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateUserResponse]
            User created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="POST",
            json={
                "isActive": is_active,
                "name": name,
                "email": email,
                "role": role,
                "teams": teams,
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
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
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

    async def update_user(
        self,
        organization_id: OrganizationId,
        *,
        email: str,
        is_active: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        role: typing.Optional[UpdateUserRequestRole] = OMIT,
        teams: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateUserResponse]:
        """
        Updates an existing user in the database.<br />Only available for self-hosted Formbricks.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        email : str
            The email of the user

        is_active : typing.Optional[bool]
            Whether the user is active

        name : typing.Optional[str]

        role : typing.Optional[UpdateUserRequestRole]
            The role of the user in the organization

        teams : typing.Optional[typing.Sequence[str]]
            The list of teams the user is a member of

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateUserResponse]
            User updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/users",
            method="PATCH",
            json={
                "isActive": is_active,
                "name": name,
                "email": email,
                "role": role,
                "teams": teams,
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
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
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
