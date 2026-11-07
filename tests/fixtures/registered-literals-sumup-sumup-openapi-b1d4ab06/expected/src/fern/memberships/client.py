

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.membership_status import MembershipStatus
from ..types.resource_type import ResourceType
from .raw_client import AsyncRawMembershipsClient, RawMembershipsClient
from .types.list_memberships_response import ListMembershipsResponse


class MembershipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMembershipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMembershipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMembershipsClient
        """
        return self._raw_client

    def list_memberships(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        kind: typing.Optional[ResourceType] = None,
        status: typing.Optional[MembershipStatus] = None,
        resource_type: typing.Optional[ResourceType] = None,
        resource_attributes_sandbox: typing.Optional[bool] = None,
        resource_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_parent_id: typing.Optional[str] = None,
        resource_parent_type: typing.Optional[ResourceType] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMembershipsResponse:
        """
        List memberships of the current user.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        kind : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        status : typing.Optional[MembershipStatus]
            Filter the returned memberships by the membership status.

        resource_type : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        resource_attributes_sandbox : typing.Optional[bool]
            Filter memberships by the sandbox status of the resource the membership is in.

        resource_name : typing.Optional[str]
            Filter memberships by the name of the resource the membership is in.

        resource_id : typing.Optional[str]
            Filter memberships by the ID of the resource the membership is in.

        resource_parent_id : typing.Optional[str]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        resource_parent_type : typing.Optional[ResourceType]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned memberships by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMembershipsResponse
            Returns a list of Membership objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.memberships.list_memberships(
            offset=0,
            limit=10,
            kind="merchant",
            resource_type="merchant",
            resource_parent_type="merchant",
        )
        """
        _response = self._raw_client.list_memberships(
            offset=offset,
            limit=limit,
            kind=kind,
            status=status,
            resource_type=resource_type,
            resource_attributes_sandbox=resource_attributes_sandbox,
            resource_name=resource_name,
            resource_id=resource_id,
            resource_parent_id=resource_parent_id,
            resource_parent_type=resource_parent_type,
            roles=roles,
            request_options=request_options,
        )
        return _response.data


class AsyncMembershipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMembershipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMembershipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMembershipsClient
        """
        return self._raw_client

    async def list_memberships(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        kind: typing.Optional[ResourceType] = None,
        status: typing.Optional[MembershipStatus] = None,
        resource_type: typing.Optional[ResourceType] = None,
        resource_attributes_sandbox: typing.Optional[bool] = None,
        resource_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_parent_id: typing.Optional[str] = None,
        resource_parent_type: typing.Optional[ResourceType] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMembershipsResponse:
        """
        List memberships of the current user.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        kind : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        status : typing.Optional[MembershipStatus]
            Filter the returned memberships by the membership status.

        resource_type : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        resource_attributes_sandbox : typing.Optional[bool]
            Filter memberships by the sandbox status of the resource the membership is in.

        resource_name : typing.Optional[str]
            Filter memberships by the name of the resource the membership is in.

        resource_id : typing.Optional[str]
            Filter memberships by the ID of the resource the membership is in.

        resource_parent_id : typing.Optional[str]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        resource_parent_type : typing.Optional[ResourceType]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned memberships by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMembershipsResponse
            Returns a list of Membership objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.memberships.list_memberships(
                offset=0,
                limit=10,
                kind="merchant",
                resource_type="merchant",
                resource_parent_type="merchant",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_memberships(
            offset=offset,
            limit=limit,
            kind=kind,
            status=status,
            resource_type=resource_type,
            resource_attributes_sandbox=resource_attributes_sandbox,
            resource_name=resource_name,
            resource_id=resource_id,
            resource_parent_id=resource_parent_id,
            resource_parent_type=resource_parent_type,
            roles=roles,
            request_options=request_options,
        )
        return _response.data
