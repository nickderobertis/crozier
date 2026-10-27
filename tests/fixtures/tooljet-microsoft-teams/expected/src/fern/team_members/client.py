

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conversation_member import ConversationMember
from ..types.conversation_member_input import ConversationMemberInput
from ..types.conversation_member_input_roles_item import ConversationMemberInputRolesItem
from .raw_client import AsyncRawTeamMembersClient, RawTeamMembersClient
from .types.add_multiple_team_members_response_item import AddMultipleTeamMembersResponseItem
from .types.list_team_members_response import ListTeamMembersResponse


OMIT = typing.cast(typing.Any, ...)


class TeamMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeamMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeamMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeamMembersClient
        """
        return self._raw_client

    def list_team_members(
        self,
        team_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMembersResponse:
        """
        Get the members of a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
        ListTeamMembersResponse
            Successfully retrieved team members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.team_members.list_team_members(
            team_id="team-id",
        )
        """
        _response = self._raw_client.list_team_members(
            team_id, top=top, skip=skip, filter=filter, request_options=request_options
        )
        return _response.data

    def add_team_member(
        self,
        team_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a new member to a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
        client.team_members.add_team_member(
            team_id="team-id",
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
        )
        """
        _response = self._raw_client.add_team_member(
            team_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data

    def add_multiple_team_members(
        self,
        team_id: str,
        *,
        values: typing.Sequence[ConversationMemberInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AddMultipleTeamMembersResponseItem]:
        """
        Add multiple members to a team in a single request

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        values : typing.Sequence[ConversationMemberInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMultipleTeamMembersResponseItem]
            Members addition completed

        Examples
        --------
        from fern import ConversationMemberInput, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.team_members.add_multiple_team_members(
            team_id="team-id",
            values=[
                ConversationMemberInput(
                    odata_type="#microsoft.graph.aadUserConversationMember",
                    user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                )
            ],
        )
        """
        _response = self._raw_client.add_multiple_team_members(team_id, values=values, request_options=request_options)
        return _response.data


class AsyncTeamMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeamMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeamMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeamMembersClient
        """
        return self._raw_client

    async def list_team_members(
        self,
        team_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMembersResponse:
        """
        Get the members of a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
        ListTeamMembersResponse
            Successfully retrieved team members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team_members.list_team_members(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_team_members(
            team_id, top=top, skip=skip, filter=filter, request_options=request_options
        )
        return _response.data

    async def add_team_member(
        self,
        team_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a new member to a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
            await client.team_members.add_team_member(
                team_id="team-id",
                odata_type="#microsoft.graph.aadUserConversationMember",
                user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_team_member(
            team_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data

    async def add_multiple_team_members(
        self,
        team_id: str,
        *,
        values: typing.Sequence[ConversationMemberInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AddMultipleTeamMembersResponseItem]:
        """
        Add multiple members to a team in a single request

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        values : typing.Sequence[ConversationMemberInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMultipleTeamMembersResponseItem]
            Members addition completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationMemberInput

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team_members.add_multiple_team_members(
                team_id="team-id",
                values=[
                    ConversationMemberInput(
                        odata_type="#microsoft.graph.aadUserConversationMember",
                        user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_multiple_team_members(
            team_id, values=values, request_options=request_options
        )
        return _response.data
