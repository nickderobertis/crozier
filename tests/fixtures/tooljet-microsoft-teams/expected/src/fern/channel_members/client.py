

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conversation_member import ConversationMember
from ..types.conversation_member_input_roles_item import ConversationMemberInputRolesItem
from .raw_client import AsyncRawChannelMembersClient, RawChannelMembersClient
from .types.list_channel_members_response import ListChannelMembersResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelMembersClient
        """
        return self._raw_client

    def list_channel_members(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelMembersResponse:
        """
        Retrieve a list of members in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelMembersResponse
            Successfully retrieved channel members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channel_members.list_channel_members(
            team_id="team-id",
            channel_id="channel-id",
        )
        """
        _response = self._raw_client.list_channel_members(
            team_id, channel_id, top=top, skip=skip, filter=filter, request_options=request_options
        )
        return _response.data

    def add_channel_member(
        self,
        team_id: str,
        channel_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a member to a private channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Member added successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channel_members.add_channel_member(
            team_id="team-id",
            channel_id="channel-id",
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
        )
        """
        _response = self._raw_client.add_channel_member(
            team_id,
            channel_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data


class AsyncChannelMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelMembersClient
        """
        return self._raw_client

    async def list_channel_members(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelMembersResponse:
        """
        Retrieve a list of members in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelMembersResponse
            Successfully retrieved channel members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channel_members.list_channel_members(
                team_id="team-id",
                channel_id="channel-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channel_members(
            team_id, channel_id, top=top, skip=skip, filter=filter, request_options=request_options
        )
        return _response.data

    async def add_channel_member(
        self,
        team_id: str,
        channel_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a member to a private channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Member added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channel_members.add_channel_member(
                team_id="team-id",
                channel_id="channel-id",
                odata_type="#microsoft.graph.aadUserConversationMember",
                user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_channel_member(
            team_id,
            channel_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data
