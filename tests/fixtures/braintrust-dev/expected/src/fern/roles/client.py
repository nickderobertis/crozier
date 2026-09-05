

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.create_role_member_permissions_item import CreateRoleMemberPermissionsItem
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.role import Role
from ..types.role_id_param import RoleIdParam
from ..types.role_name import RoleName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawRolesClient, RawRolesClient
from .types.get_role_response import GetRoleResponse
from .types.patch_role_add_member_permissions_item import PatchRoleAddMemberPermissionsItem
from .types.patch_role_remove_member_permissions_item import PatchRoleRemoveMemberPermissionsItem


OMIT = typing.cast(typing.Any, ...)


class RolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRolesClient
        """
        return self._raw_client

    def get_role(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        role_name: typing.Optional[RoleName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetRoleResponse:
        """
        List out all roles. The roles are sorted by creation date, with the most recently-created roles coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        role_name : typing.Optional[RoleName]
            Name of the role to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoleResponse
            Returns a list of role objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.get_role()
        """
        _response = self._raw_client.get_role(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            role_name=role_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_role(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_permissions: typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]] = OMIT,
        member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a new role. If there is an existing role with the same name as the one specified in the request, will return the existing role unmodified

        Parameters
        ----------
        name : str
            Name of the role

        description : typing.Optional[str]
            Textual description of the role

        member_permissions : typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]]
            (permission, restrict_object_type) tuples which belong to this role

        member_roles : typing.Optional[typing.Sequence[str]]
            Ids of the roles this role inherits from

            An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the role belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the new role object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.post_role(
            name="name",
        )
        """
        _response = self._raw_client.post_role(
            name=name,
            description=description,
            member_permissions=member_permissions,
            member_roles=member_roles,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def put_role(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_permissions: typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]] = OMIT,
        member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create or replace role. If there is an existing role with the same name as the one specified in the request, will replace the existing role with the provided fields

        Parameters
        ----------
        name : str
            Name of the role

        description : typing.Optional[str]
            Textual description of the role

        member_permissions : typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]]
            (permission, restrict_object_type) tuples which belong to this role

        member_roles : typing.Optional[typing.Sequence[str]]
            Ids of the roles this role inherits from

            An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the role belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the new role object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.put_role(
            name="name",
        )
        """
        _response = self._raw_client.put_role(
            name=name,
            description=description,
            member_permissions=member_permissions,
            member_roles=member_roles,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def get_role_id(self, role_id: RoleIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Get a role object by its id

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the role object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.get_role_id(
            role_id="role_id",
        )
        """
        _response = self._raw_client.get_role_id(role_id, request_options=request_options)
        return _response.data

    def delete_role_id(self, role_id: RoleIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Delete a role object by its id

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the deleted role object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.delete_role_id(
            role_id="role_id",
        )
        """
        _response = self._raw_client.delete_role_id(role_id, request_options=request_options)
        return _response.data

    def patch_role_id(
        self,
        role_id: RoleIdParam,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_member_permissions: typing.Optional[typing.Sequence[PatchRoleAddMemberPermissionsItem]] = OMIT,
        remove_member_permissions: typing.Optional[typing.Sequence[PatchRoleRemoveMemberPermissionsItem]] = OMIT,
        add_member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Partially update a role object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        description : typing.Optional[str]
            Textual description of the role

        name : typing.Optional[str]
            Name of the role

        add_member_permissions : typing.Optional[typing.Sequence[PatchRoleAddMemberPermissionsItem]]
            A list of permissions to add to the role

        remove_member_permissions : typing.Optional[typing.Sequence[PatchRoleRemoveMemberPermissionsItem]]
            A list of permissions to remove from the role

        add_member_roles : typing.Optional[typing.Sequence[str]]
            A list of role IDs to add to the role's inheriting-from set

        remove_member_roles : typing.Optional[typing.Sequence[str]]
            A list of role IDs to remove from the role's inheriting-from set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the role object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.patch_role_id(
            role_id="role_id",
        )
        """
        _response = self._raw_client.patch_role_id(
            role_id,
            description=description,
            name=name,
            add_member_permissions=add_member_permissions,
            remove_member_permissions=remove_member_permissions,
            add_member_roles=add_member_roles,
            remove_member_roles=remove_member_roles,
            request_options=request_options,
        )
        return _response.data


class AsyncRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRolesClient
        """
        return self._raw_client

    async def get_role(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        role_name: typing.Optional[RoleName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetRoleResponse:
        """
        List out all roles. The roles are sorted by creation date, with the most recently-created roles coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        role_name : typing.Optional[RoleName]
            Name of the role to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoleResponse
            Returns a list of role objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.get_role()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_role(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            role_name=role_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_role(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_permissions: typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]] = OMIT,
        member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create a new role. If there is an existing role with the same name as the one specified in the request, will return the existing role unmodified

        Parameters
        ----------
        name : str
            Name of the role

        description : typing.Optional[str]
            Textual description of the role

        member_permissions : typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]]
            (permission, restrict_object_type) tuples which belong to this role

        member_roles : typing.Optional[typing.Sequence[str]]
            Ids of the roles this role inherits from

            An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the role belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the new role object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.post_role(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_role(
            name=name,
            description=description,
            member_permissions=member_permissions,
            member_roles=member_roles,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def put_role(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_permissions: typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]] = OMIT,
        member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Create or replace role. If there is an existing role with the same name as the one specified in the request, will replace the existing role with the provided fields

        Parameters
        ----------
        name : str
            Name of the role

        description : typing.Optional[str]
            Textual description of the role

        member_permissions : typing.Optional[typing.Sequence[CreateRoleMemberPermissionsItem]]
            (permission, restrict_object_type) tuples which belong to this role

        member_roles : typing.Optional[typing.Sequence[str]]
            Ids of the roles this role inherits from

            An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the role belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the new role object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.put_role(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_role(
            name=name,
            description=description,
            member_permissions=member_permissions,
            member_roles=member_roles,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def get_role_id(
        self, role_id: RoleIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Role:
        """
        Get a role object by its id

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the role object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.get_role_id(
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_role_id(role_id, request_options=request_options)
        return _response.data

    async def delete_role_id(
        self, role_id: RoleIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Role:
        """
        Delete a role object by its id

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the deleted role object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.delete_role_id(
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_role_id(role_id, request_options=request_options)
        return _response.data

    async def patch_role_id(
        self,
        role_id: RoleIdParam,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_member_permissions: typing.Optional[typing.Sequence[PatchRoleAddMemberPermissionsItem]] = OMIT,
        remove_member_permissions: typing.Optional[typing.Sequence[PatchRoleRemoveMemberPermissionsItem]] = OMIT,
        add_member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Partially update a role object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        role_id : RoleIdParam
            Role id

        description : typing.Optional[str]
            Textual description of the role

        name : typing.Optional[str]
            Name of the role

        add_member_permissions : typing.Optional[typing.Sequence[PatchRoleAddMemberPermissionsItem]]
            A list of permissions to add to the role

        remove_member_permissions : typing.Optional[typing.Sequence[PatchRoleRemoveMemberPermissionsItem]]
            A list of permissions to remove from the role

        add_member_roles : typing.Optional[typing.Sequence[str]]
            A list of role IDs to add to the role's inheriting-from set

        remove_member_roles : typing.Optional[typing.Sequence[str]]
            A list of role IDs to remove from the role's inheriting-from set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Returns the role object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.patch_role_id(
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_role_id(
            role_id,
            description=description,
            name=name,
            add_member_permissions=add_member_permissions,
            remove_member_permissions=remove_member_permissions,
            add_member_roles=add_member_roles,
            remove_member_roles=remove_member_roles,
            request_options=request_options,
        )
        return _response.data
