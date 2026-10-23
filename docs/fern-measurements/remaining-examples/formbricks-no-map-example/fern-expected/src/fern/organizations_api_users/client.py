

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_id import OrganizationId
from .raw_client import AsyncRawOrganizationsApiUsersClient, RawOrganizationsApiUsersClient
from .types.create_user_request_role import CreateUserRequestRole
from .types.create_user_response import CreateUserResponse
from .types.get_users_request_filter_date_field import GetUsersRequestFilterDateField
from .types.get_users_request_order import GetUsersRequestOrder
from .types.get_users_request_sort_by import GetUsersRequestSortBy
from .types.get_users_response import GetUsersResponse
from .types.update_user_request_role import UpdateUserRequestRole
from .types.update_user_response import UpdateUserResponse


OMIT = typing.cast(typing.Any, ...)


class OrganizationsApiUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsApiUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsApiUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsApiUsersClient
        """
        return self._raw_client

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
    ) -> GetUsersResponse:
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
        GetUsersResponse
            Users retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_users.get_users(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_users(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            id=id,
            email=email,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateUserResponse:
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
        CreateUserResponse
            User created successfully.

        Examples
        --------
        from fern.organizations_api_users import CreateUserRequestRole

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_users.create_user(
            organization_id="organizationId",
            name="John Doe",
            email="example@example.com",
            role=CreateUserRequestRole.OWNER,
        )
        """
        _response = self._raw_client.create_user(
            organization_id,
            name=name,
            email=email,
            role=role,
            is_active=is_active,
            teams=teams,
            request_options=request_options,
        )
        return _response.data

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
    ) -> UpdateUserResponse:
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
        UpdateUserResponse
            User updated successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_users.update_user(
            organization_id="organizationId",
            email="example@example.com",
        )
        """
        _response = self._raw_client.update_user(
            organization_id,
            email=email,
            is_active=is_active,
            name=name,
            role=role,
            teams=teams,
            request_options=request_options,
        )
        return _response.data


class AsyncOrganizationsApiUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsApiUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsApiUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsApiUsersClient
        """
        return self._raw_client

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
    ) -> GetUsersResponse:
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
        GetUsersResponse
            Users retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_users.get_users(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            id=id,
            email=email,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateUserResponse:
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
        CreateUserResponse
            User created successfully.

        Examples
        --------
        import asyncio

        from fern.organizations_api_users import CreateUserRequestRole

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_users.create_user(
                organization_id="organizationId",
                name="John Doe",
                email="example@example.com",
                role=CreateUserRequestRole.OWNER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            organization_id,
            name=name,
            email=email,
            role=role,
            is_active=is_active,
            teams=teams,
            request_options=request_options,
        )
        return _response.data

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
    ) -> UpdateUserResponse:
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
        UpdateUserResponse
            User updated successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_users.update_user(
                organization_id="organizationId",
                email="example@example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            organization_id,
            email=email,
            is_active=is_active,
            name=name,
            role=role,
            teams=teams,
            request_options=request_options,
        )
        return _response.data
