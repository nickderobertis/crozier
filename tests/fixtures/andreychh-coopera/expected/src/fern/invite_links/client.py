

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.invite_link import InviteLink
from ..types.invite_link_list import InviteLinkList
from ..types.team import Team
from .raw_client import AsyncRawInviteLinksClient, RawInviteLinksClient
from .types.list_invite_links_request_status import ListInviteLinksRequestStatus


OMIT = typing.cast(typing.Any, ...)


class InviteLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInviteLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInviteLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInviteLinksClient
        """
        return self._raw_client

    def list_invite_links(
        self,
        team_id: str,
        *,
        status: typing.Optional[ListInviteLinksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteLinkList:
        """
        Returns invite links for the team, optionally filtered by status. Only the team's owner may list them.

        Parameters
        ----------
        team_id : str
            The team the links belong to.

        status : typing.Optional[ListInviteLinksRequestStatus]
            Keeps only the links in that state. Without it every link the team has comes back, spent and revoked ones included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteLinkList
            Invite links

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invite_links.list_invite_links(
            team_id="team_id",
        )
        """
        _response = self._raw_client.list_invite_links(team_id, status=status, request_options=request_options)
        return _response.data

    def create_invite_link(
        self,
        team_id: str,
        *,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteLink:
        """
        Creates a link that can be used to join the team. Only the team's owner may create one.

        Parameters
        ----------
        team_id : str
            The team the links belong to.

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteLink
            Invite link created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invite_links.create_invite_link(
            team_id="team_id",
        )
        """
        _response = self._raw_client.create_invite_link(team_id, expires_at=expires_at, request_options=request_options)
        return _response.data

    def revoke_invite_link(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Marks the invite link as revoked. Only the owner of the team it belongs to may revoke it.

        Parameters
        ----------
        code : str
            The invite link to revoke.

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
        client.invite_links.revoke_invite_link(
            code="code",
        )
        """
        _response = self._raw_client.revoke_invite_link(code, request_options=request_options)
        return _response.data

    def accept_invite_link(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Adds the caller as a member of the team the invite link belongs to. Joining happens once: someone who is already a member is told so rather than answered as though they had just joined, so that a success here always means the same thing. The caller must have introduced themselves first — a team sees its members by name.

        Parameters
        ----------
        code : str
            The invite link being accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Joined the team

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invite_links.accept_invite_link(
            code="code",
        )
        """
        _response = self._raw_client.accept_invite_link(code, request_options=request_options)
        return _response.data


class AsyncInviteLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInviteLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInviteLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInviteLinksClient
        """
        return self._raw_client

    async def list_invite_links(
        self,
        team_id: str,
        *,
        status: typing.Optional[ListInviteLinksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteLinkList:
        """
        Returns invite links for the team, optionally filtered by status. Only the team's owner may list them.

        Parameters
        ----------
        team_id : str
            The team the links belong to.

        status : typing.Optional[ListInviteLinksRequestStatus]
            Keeps only the links in that state. Without it every link the team has comes back, spent and revoked ones included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteLinkList
            Invite links

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invite_links.list_invite_links(
                team_id="team_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_invite_links(team_id, status=status, request_options=request_options)
        return _response.data

    async def create_invite_link(
        self,
        team_id: str,
        *,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteLink:
        """
        Creates a link that can be used to join the team. Only the team's owner may create one.

        Parameters
        ----------
        team_id : str
            The team the links belong to.

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteLink
            Invite link created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invite_links.create_invite_link(
                team_id="team_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_invite_link(
            team_id, expires_at=expires_at, request_options=request_options
        )
        return _response.data

    async def revoke_invite_link(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Marks the invite link as revoked. Only the owner of the team it belongs to may revoke it.

        Parameters
        ----------
        code : str
            The invite link to revoke.

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
            await client.invite_links.revoke_invite_link(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_invite_link(code, request_options=request_options)
        return _response.data

    async def accept_invite_link(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Adds the caller as a member of the team the invite link belongs to. Joining happens once: someone who is already a member is told so rather than answered as though they had just joined, so that a success here always means the same thing. The caller must have introduced themselves first — a team sees its members by name.

        Parameters
        ----------
        code : str
            The invite link being accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Joined the team

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invite_links.accept_invite_link(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_invite_link(code, request_options=request_options)
        return _response.data
