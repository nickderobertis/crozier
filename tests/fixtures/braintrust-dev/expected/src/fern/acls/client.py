

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.acl import Acl
from ..types.acl_batch_update_response import AclBatchUpdateResponse
from ..types.acl_id_param import AclIdParam
from ..types.acl_item import AclItem
from ..types.acl_list_group_id import AclListGroupId
from ..types.acl_list_org_object_id import AclListOrgObjectId
from ..types.acl_list_org_object_type import AclListOrgObjectType
from ..types.acl_list_permission import AclListPermission
from ..types.acl_list_restrict_object_type import AclListRestrictObjectType
from ..types.acl_list_role_id import AclListRoleId
from ..types.acl_list_user_id import AclListUserId
from ..types.acl_object_id import AclObjectId
from ..types.acl_object_type import AclObjectType
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.permission import Permission
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawAclsClient, RawAclsClient
from .types.get_acl_response import GetAclResponse


OMIT = typing.cast(typing.Any, ...)


class AclsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAclsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAclsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAclsClient
        """
        return self._raw_client

    def get_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAclResponse:
        """
        List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

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

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAclResponse
            Returns a list of acl objects

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.get_acl(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.get_acl(
            object_type=object_type,
            object_id=object_id,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    def post_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Acl:
        """
        Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the new acl object

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.post_acl(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.post_acl(
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    def delete_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Acl:
        """
        Delete a single acl

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the deleted acl object

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.delete_acl(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.delete_acl(
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    def get_acl_id(self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Acl:
        """
        Get an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the acl object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.get_acl_id(
            acl_id="acl_id",
        )
        """
        _response = self._raw_client.get_acl_id(acl_id, request_options=request_options)
        return _response.data

    def delete_acl_id(self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Acl:
        """
        Delete an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the deleted acl object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.delete_acl_id(
            acl_id="acl_id",
        )
        """
        _response = self._raw_client.delete_acl_id(acl_id, request_options=request_options)
        return _response.data

    def acl_batch_update(
        self,
        *,
        add_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        remove_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AclBatchUpdateResponse:
        """
        Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.

        Parameters
        ----------
        add_acls : typing.Optional[typing.Sequence[AclItem]]

        remove_acls : typing.Optional[typing.Sequence[AclItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AclBatchUpdateResponse
            A success status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.acl_batch_update()
        """
        _response = self._raw_client.acl_batch_update(
            add_acls=add_acls, remove_acls=remove_acls, request_options=request_options
        )
        return _response.data

    def acl_list_org(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        object_type: typing.Optional[AclListOrgObjectType] = None,
        object_id: typing.Optional[AclListOrgObjectId] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Acl]:
        """
        List all acls in the org. This query requires the caller to have `read_acls` permission at the organization level

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        object_type : typing.Optional[AclListOrgObjectType]
            The object type that the ACL applies to

        object_id : typing.Optional[AclListOrgObjectId]
            The id of the object the ACL applies to

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Acl]
            A list of acls

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.acls.acl_list_org()
        """
        _response = self._raw_client.acl_list_org(
            limit=limit,
            ids=ids,
            starting_after=starting_after,
            ending_before=ending_before,
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data


class AsyncAclsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAclsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAclsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAclsClient
        """
        return self._raw_client

    async def get_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAclResponse:
        """
        List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

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

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAclResponse
            Returns a list of acl objects

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.get_acl(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_acl(
            object_type=object_type,
            object_id=object_id,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    async def post_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Acl:
        """
        Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the new acl object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.post_acl(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_acl(
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Acl:
        """
        Delete a single acl

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the deleted acl object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.delete_acl(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_acl(
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            request_options=request_options,
        )
        return _response.data

    async def get_acl_id(self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Acl:
        """
        Get an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the acl object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.get_acl_id(
                acl_id="acl_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_acl_id(acl_id, request_options=request_options)
        return _response.data

    async def delete_acl_id(
        self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Acl:
        """
        Delete an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Acl
            Returns the deleted acl object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.delete_acl_id(
                acl_id="acl_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_acl_id(acl_id, request_options=request_options)
        return _response.data

    async def acl_batch_update(
        self,
        *,
        add_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        remove_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AclBatchUpdateResponse:
        """
        Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.

        Parameters
        ----------
        add_acls : typing.Optional[typing.Sequence[AclItem]]

        remove_acls : typing.Optional[typing.Sequence[AclItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AclBatchUpdateResponse
            A success status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.acl_batch_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.acl_batch_update(
            add_acls=add_acls, remove_acls=remove_acls, request_options=request_options
        )
        return _response.data

    async def acl_list_org(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        object_type: typing.Optional[AclListOrgObjectType] = None,
        object_id: typing.Optional[AclListOrgObjectId] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Acl]:
        """
        List all acls in the org. This query requires the caller to have `read_acls` permission at the organization level

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        object_type : typing.Optional[AclListOrgObjectType]
            The object type that the ACL applies to

        object_id : typing.Optional[AclListOrgObjectId]
            The id of the object the ACL applies to

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Acl]
            A list of acls

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.acls.acl_list_org()


        asyncio.run(main())
        """
        _response = await self._raw_client.acl_list_org(
            limit=limit,
            ids=ids,
            starting_after=starting_after,
            ending_before=ending_before,
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            group_id=group_id,
            permission=permission,
            restrict_object_type=restrict_object_type,
            role_id=role_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data
