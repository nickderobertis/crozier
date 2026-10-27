

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.team import Team
from ..types.team_discovery_settings import TeamDiscoverySettings
from ..types.team_fun_settings import TeamFunSettings
from ..types.team_guest_settings import TeamGuestSettings
from ..types.team_member_settings import TeamMemberSettings
from ..types.team_messaging_settings import TeamMessagingSettings
from .raw_client import AsyncRawTeamsClient, RawTeamsClient
from .types.create_team_request import CreateTeamRequest
from .types.get_team_request_expand import GetTeamRequestExpand
from .types.list_all_teams_response import ListAllTeamsResponse
from .types.list_joined_teams_response import ListJoinedTeamsResponse
from .types.update_team_request_visibility import UpdateTeamRequestVisibility


OMIT = typing.cast(typing.Any, ...)


class TeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeamsClient
        """
        return self._raw_client

    def list_joined_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListJoinedTeamsResponse:
        """
        Get the teams in Microsoft Teams that the user is a direct member of

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListJoinedTeamsResponse
            Successfully retrieved joined teams

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.list_joined_teams()
        """
        _response = self._raw_client.list_joined_teams(request_options=request_options)
        return _response.data

    def list_all_teams(
        self,
        *,
        filter: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllTeamsResponse:
        """
        List all teams in an organization (requires admin permissions)

        Parameters
        ----------
        filter : typing.Optional[str]
            OData filter query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllTeamsResponse
            Successfully retrieved teams

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.list_all_teams()
        """
        _response = self._raw_client.list_all_teams(filter=filter, top=top, skip=skip, request_options=request_options)
        return _response.data

    def create_team(
        self, *, request: CreateTeamRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a new team

        Parameters
        ----------
        request : CreateTeamRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.teams import CreateTeamRequestChannels

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.create_team(
            request=CreateTeamRequestChannels(
                template_odata_bind="https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
                display_name="displayName",
                description="description",
            ),
        )
        """
        _response = self._raw_client.create_team(request=request, request_options=request_options)
        return _response.data

    def get_team(
        self,
        team_id: str,
        *,
        select: typing.Optional[str] = None,
        expand: typing.Optional[GetTeamRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Retrieve the properties and relationships of the specified team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        select : typing.Optional[str]
            OData select query

        expand : typing.Optional[GetTeamRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Successfully retrieved team

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.get_team(
            team_id="team-id",
        )
        """
        _response = self._raw_client.get_team(team_id, select=select, expand=expand, request_options=request_options)
        return _response.data

    def delete_team(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
        client.teams.delete_team(
            team_id="team-id",
        )
        """
        _response = self._raw_client.delete_team(team_id, request_options=request_options)
        return _response.data

    def update_team(
        self,
        team_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        visibility: typing.Optional[UpdateTeamRequestVisibility] = OMIT,
        member_settings: typing.Optional[TeamMemberSettings] = OMIT,
        guest_settings: typing.Optional[TeamGuestSettings] = OMIT,
        messaging_settings: typing.Optional[TeamMessagingSettings] = OMIT,
        fun_settings: typing.Optional[TeamFunSettings] = OMIT,
        discovery_settings: typing.Optional[TeamDiscoverySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        display_name : typing.Optional[str]

        description : typing.Optional[str]

        visibility : typing.Optional[UpdateTeamRequestVisibility]

        member_settings : typing.Optional[TeamMemberSettings]

        guest_settings : typing.Optional[TeamGuestSettings]

        messaging_settings : typing.Optional[TeamMessagingSettings]

        fun_settings : typing.Optional[TeamFunSettings]

        discovery_settings : typing.Optional[TeamDiscoverySettings]

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
        client.teams.update_team(
            team_id="team-id",
        )
        """
        _response = self._raw_client.update_team(
            team_id,
            display_name=display_name,
            description=description,
            visibility=visibility,
            member_settings=member_settings,
            guest_settings=guest_settings,
            messaging_settings=messaging_settings,
            fun_settings=fun_settings,
            discovery_settings=discovery_settings,
            request_options=request_options,
        )
        return _response.data

    def archive_team(
        self,
        team_id: str,
        *,
        should_set_spo_site_read_only_for_members: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive the specified team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        should_set_spo_site_read_only_for_members : typing.Optional[bool]

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
        client.teams.archive_team(
            team_id="team-id",
        )
        """
        _response = self._raw_client.archive_team(
            team_id,
            should_set_spo_site_read_only_for_members=should_set_spo_site_read_only_for_members,
            request_options=request_options,
        )
        return _response.data

    def unarchive_team(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Restore an archived team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
        client.teams.unarchive_team(
            team_id="team-id",
        )
        """
        _response = self._raw_client.unarchive_team(team_id, request_options=request_options)
        return _response.data


class AsyncTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeamsClient
        """
        return self._raw_client

    async def list_joined_teams(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListJoinedTeamsResponse:
        """
        Get the teams in Microsoft Teams that the user is a direct member of

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListJoinedTeamsResponse
            Successfully retrieved joined teams

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.list_joined_teams()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_joined_teams(request_options=request_options)
        return _response.data

    async def list_all_teams(
        self,
        *,
        filter: typing.Optional[str] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllTeamsResponse:
        """
        List all teams in an organization (requires admin permissions)

        Parameters
        ----------
        filter : typing.Optional[str]
            OData filter query

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllTeamsResponse
            Successfully retrieved teams

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.list_all_teams()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_teams(
            filter=filter, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    async def create_team(
        self, *, request: CreateTeamRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a new team

        Parameters
        ----------
        request : CreateTeamRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.teams import CreateTeamRequestChannels

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.create_team(
                request=CreateTeamRequestChannels(
                    template_odata_bind="https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
                    display_name="displayName",
                    description="description",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team(request=request, request_options=request_options)
        return _response.data

    async def get_team(
        self,
        team_id: str,
        *,
        select: typing.Optional[str] = None,
        expand: typing.Optional[GetTeamRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Retrieve the properties and relationships of the specified team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        select : typing.Optional[str]
            OData select query

        expand : typing.Optional[GetTeamRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Successfully retrieved team

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.get_team(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team(
            team_id, select=select, expand=expand, request_options=request_options
        )
        return _response.data

    async def delete_team(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
            await client.teams.delete_team(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_team(team_id, request_options=request_options)
        return _response.data

    async def update_team(
        self,
        team_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        visibility: typing.Optional[UpdateTeamRequestVisibility] = OMIT,
        member_settings: typing.Optional[TeamMemberSettings] = OMIT,
        guest_settings: typing.Optional[TeamGuestSettings] = OMIT,
        messaging_settings: typing.Optional[TeamMessagingSettings] = OMIT,
        fun_settings: typing.Optional[TeamFunSettings] = OMIT,
        discovery_settings: typing.Optional[TeamDiscoverySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        display_name : typing.Optional[str]

        description : typing.Optional[str]

        visibility : typing.Optional[UpdateTeamRequestVisibility]

        member_settings : typing.Optional[TeamMemberSettings]

        guest_settings : typing.Optional[TeamGuestSettings]

        messaging_settings : typing.Optional[TeamMessagingSettings]

        fun_settings : typing.Optional[TeamFunSettings]

        discovery_settings : typing.Optional[TeamDiscoverySettings]

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
            await client.teams.update_team(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_team(
            team_id,
            display_name=display_name,
            description=description,
            visibility=visibility,
            member_settings=member_settings,
            guest_settings=guest_settings,
            messaging_settings=messaging_settings,
            fun_settings=fun_settings,
            discovery_settings=discovery_settings,
            request_options=request_options,
        )
        return _response.data

    async def archive_team(
        self,
        team_id: str,
        *,
        should_set_spo_site_read_only_for_members: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive the specified team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        should_set_spo_site_read_only_for_members : typing.Optional[bool]

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
            await client.teams.archive_team(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_team(
            team_id,
            should_set_spo_site_read_only_for_members=should_set_spo_site_read_only_for_members,
            request_options=request_options,
        )
        return _response.data

    async def unarchive_team(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Restore an archived team

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

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
            await client.teams.unarchive_team(
                team_id="team-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unarchive_team(team_id, request_options=request_options)
        return _response.data
