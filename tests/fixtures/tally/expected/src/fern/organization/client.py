

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from .raw_client import AsyncRawOrganizationClient, RawOrganizationClient
from .types.list_organization_invites_response_item import ListOrganizationInvitesResponseItem


OMIT = typing.cast(typing.Any, ...)


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationClient
        """
        return self._raw_client

    def list_organization_users(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Returns a list of all users in your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            A list of organization users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.list_organization_users(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.list_organization_users(organization_id, request_options=request_options)
        return _response.data

    def remove_organization_user(
        self, organization_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from your organization. Only the organization creator can remove other members, or users can remove themselves.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        user_id : str
            The ID of the user to remove from the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.remove_organization_user(
            organization_id="organizationId",
            user_id="userId",
        )
        """
        _response = self._raw_client.remove_organization_user(organization_id, user_id, request_options=request_options)
        return _response.data

    def list_organization_invites(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListOrganizationInvitesResponseItem]:
        """
        Returns a list of all invites in your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListOrganizationInvitesResponseItem]
            A list of organization invites

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.list_organization_invites(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.list_organization_invites(organization_id, request_options=request_options)
        return _response.data

    def create_organization_invites(
        self,
        organization_id: str,
        *,
        workspace_ids: typing.Sequence[str],
        emails: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Invites users to join specific workspaces within your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        workspace_ids : typing.Sequence[str]
            Array of workspace IDs to invite users to

        emails : str
            Comma or semicolon separated list of email addresses to invite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.create_organization_invites(
            organization_id="organizationId",
            workspace_ids=["workspaceIds"],
            emails="emails",
        )
        """
        _response = self._raw_client.create_organization_invites(
            organization_id, workspace_ids=workspace_ids, emails=emails, request_options=request_options
        )
        return _response.data

    def cancel_organization_invite(
        self, organization_id: str, invite_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancels a pending invitation to join workspaces within your organization. Only the user who created the invite can cancel it.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        invite_id : str
            The ID of the invite to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.cancel_organization_invite(
            organization_id="organizationId",
            invite_id="inviteId",
        )
        """
        _response = self._raw_client.cancel_organization_invite(
            organization_id, invite_id, request_options=request_options
        )
        return _response.data


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationClient
        """
        return self._raw_client

    async def list_organization_users(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Returns a list of all users in your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            A list of organization users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.list_organization_users(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_organization_users(organization_id, request_options=request_options)
        return _response.data

    async def remove_organization_user(
        self, organization_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from your organization. Only the organization creator can remove other members, or users can remove themselves.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        user_id : str
            The ID of the user to remove from the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.remove_organization_user(
                organization_id="organizationId",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_organization_user(
            organization_id, user_id, request_options=request_options
        )
        return _response.data

    async def list_organization_invites(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListOrganizationInvitesResponseItem]:
        """
        Returns a list of all invites in your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListOrganizationInvitesResponseItem]
            A list of organization invites

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.list_organization_invites(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_organization_invites(organization_id, request_options=request_options)
        return _response.data

    async def create_organization_invites(
        self,
        organization_id: str,
        *,
        workspace_ids: typing.Sequence[str],
        emails: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Invites users to join specific workspaces within your organization.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        workspace_ids : typing.Sequence[str]
            Array of workspace IDs to invite users to

        emails : str
            Comma or semicolon separated list of email addresses to invite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.create_organization_invites(
                organization_id="organizationId",
                workspace_ids=["workspaceIds"],
                emails="emails",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_organization_invites(
            organization_id, workspace_ids=workspace_ids, emails=emails, request_options=request_options
        )
        return _response.data

    async def cancel_organization_invite(
        self, organization_id: str, invite_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancels a pending invitation to join workspaces within your organization. Only the user who created the invite can cancel it.

        Parameters
        ----------
        organization_id : str
            The ID of the organization

        invite_id : str
            The ID of the invite to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.cancel_organization_invite(
                organization_id="organizationId",
                invite_id="inviteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_organization_invite(
            organization_id, invite_id, request_options=request_options
        )
        return _response.data
