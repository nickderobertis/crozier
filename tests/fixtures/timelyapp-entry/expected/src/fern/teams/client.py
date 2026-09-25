

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1team import V1Team
from .raw_client import AsyncRawTeamsClient, RawTeamsClient
from .types.delete11account_id_teams_id_response import Delete11AccountIdTeamsIdResponse
from .types.v1teams_create_team import V1TeamsCreateTeam
from .types.v1teams_patch_team import V1TeamsPatchTeam
from .types.v1teams_update_team import V1TeamsUpdateTeam


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

    def search_teams(
        self,
        account_id: int,
        *,
        q: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Team]:
        """
        Search for teams by name

        Parameters
        ----------
        account_id : int
            Account ID for the teams you want to search

        q : typing.Optional[str]
            Search query

        per_page : typing.Optional[int]
            Number of results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Team]
            Teams found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.search_teams(
            account_id=1,
        )
        """
        _response = self._raw_client.search_teams(
            account_id, q=q, per_page=per_page, page=page, request_options=request_options
        )
        return _response.data

    def list_all_teams_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Team]:
        """
        NOTE: By default, team list will return first 100 teams in alphabetical order. You can also use optional parameters like "limit", "offset", and "order" to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the teams you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of teams

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve teams from offset

        filter : typing.Optional[str]
            Filter teams by "mine" or show all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Team]
            Team details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.list_all_teams_of_an_account(
            account_id=1,
        )
        """
        _response = self._raw_client.list_all_teams_of_an_account(
            account_id, limit=limit, order=order, offset=offset, filter=filter, request_options=request_options
        )
        return _response.data

    def create_team(
        self, account_id: int, *, team: V1TeamsCreateTeam, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Team:
        """
        This API lets you create a team for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to create

        team : V1TeamsCreateTeam

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team

        Examples
        --------
        from fern.teams import V1TeamsCreateTeam

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.create_team(
            account_id=1,
            team=V1TeamsCreateTeam(
                name="New Team",
                color="FF5733",
                emoji="🚀",
            ),
        )
        """
        _response = self._raw_client.create_team(account_id, team=team, request_options=request_options)
        return _response.data

    def team_details(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Team:
        """
        Team details including users and project IDs

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to retrieve

        id : int
            Team ID to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.team_details(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.team_details(account_id, id, request_options=request_options)
        return _response.data

    def team_update(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsUpdateTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Team:
        """
        Update team details just by using a team ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to update

        id : int
            Team ID to update

        team : V1TeamsUpdateTeam

        add_users_to_team_projects : typing.Optional[bool]
            Whether to add users to team projects

        delete_users_from_team_projects : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        from fern.teams import V1TeamsUpdateTeam

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.team_update(
            account_id=1,
            id=1,
            team=V1TeamsUpdateTeam(
                name="Updated Team Name",
            ),
        )
        """
        _response = self._raw_client.team_update(
            account_id,
            id,
            team=team,
            add_users_to_team_projects=add_users_to_team_projects,
            delete_users_from_team_projects=delete_users_from_team_projects,
            request_options=request_options,
        )
        return _response.data

    def team_delete(
        self,
        account_id: int,
        id: int,
        *,
        delete_project_users: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Delete11AccountIdTeamsIdResponse:
        """
        Delete a team by ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to delete

        id : int
            Team ID to delete

        delete_project_users : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Delete11AccountIdTeamsIdResponse
            Team deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.team_delete(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.team_delete(
            account_id, id, delete_project_users=delete_project_users, request_options=request_options
        )
        return _response.data

    def team_patch(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsPatchTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Team:
        """
        Patch team details just by using a team ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to patch

        id : int
            Team ID to patch

        team : V1TeamsPatchTeam

        add_users_to_team_projects : typing.Optional[bool]
            Whether to add users to team projects

        delete_users_from_team_projects : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        from fern.teams import V1TeamsPatchTeam

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.team_patch(
            account_id=1,
            id=1,
            team=V1TeamsPatchTeam(
                name="Patched Team Name",
            ),
        )
        """
        _response = self._raw_client.team_patch(
            account_id,
            id,
            team=team,
            add_users_to_team_projects=add_users_to_team_projects,
            delete_users_from_team_projects=delete_users_from_team_projects,
            request_options=request_options,
        )
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

    async def search_teams(
        self,
        account_id: int,
        *,
        q: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Team]:
        """
        Search for teams by name

        Parameters
        ----------
        account_id : int
            Account ID for the teams you want to search

        q : typing.Optional[str]
            Search query

        per_page : typing.Optional[int]
            Number of results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Team]
            Teams found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.search_teams(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_teams(
            account_id, q=q, per_page=per_page, page=page, request_options=request_options
        )
        return _response.data

    async def list_all_teams_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Team]:
        """
        NOTE: By default, team list will return first 100 teams in alphabetical order. You can also use optional parameters like "limit", "offset", and "order" to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the teams you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of teams

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve teams from offset

        filter : typing.Optional[str]
            Filter teams by "mine" or show all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Team]
            Team details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.list_all_teams_of_an_account(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_teams_of_an_account(
            account_id, limit=limit, order=order, offset=offset, filter=filter, request_options=request_options
        )
        return _response.data

    async def create_team(
        self, account_id: int, *, team: V1TeamsCreateTeam, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Team:
        """
        This API lets you create a team for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to create

        team : V1TeamsCreateTeam

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team

        Examples
        --------
        import asyncio

        from fern.teams import V1TeamsCreateTeam

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.create_team(
                account_id=1,
                team=V1TeamsCreateTeam(
                    name="New Team",
                    color="FF5733",
                    emoji="🚀",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team(account_id, team=team, request_options=request_options)
        return _response.data

    async def team_details(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Team:
        """
        Team details including users and project IDs

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to retrieve

        id : int
            Team ID to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.team_details(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.team_details(account_id, id, request_options=request_options)
        return _response.data

    async def team_update(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsUpdateTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Team:
        """
        Update team details just by using a team ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to update

        id : int
            Team ID to update

        team : V1TeamsUpdateTeam

        add_users_to_team_projects : typing.Optional[bool]
            Whether to add users to team projects

        delete_users_from_team_projects : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        import asyncio

        from fern.teams import V1TeamsUpdateTeam

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.team_update(
                account_id=1,
                id=1,
                team=V1TeamsUpdateTeam(
                    name="Updated Team Name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.team_update(
            account_id,
            id,
            team=team,
            add_users_to_team_projects=add_users_to_team_projects,
            delete_users_from_team_projects=delete_users_from_team_projects,
            request_options=request_options,
        )
        return _response.data

    async def team_delete(
        self,
        account_id: int,
        id: int,
        *,
        delete_project_users: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Delete11AccountIdTeamsIdResponse:
        """
        Delete a team by ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to delete

        id : int
            Team ID to delete

        delete_project_users : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Delete11AccountIdTeamsIdResponse
            Team deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.team_delete(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.team_delete(
            account_id, id, delete_project_users=delete_project_users, request_options=request_options
        )
        return _response.data

    async def team_patch(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsPatchTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Team:
        """
        Patch team details just by using a team ID.

        Parameters
        ----------
        account_id : int
            Account ID for the team you want to patch

        id : int
            Team ID to patch

        team : V1TeamsPatchTeam

        add_users_to_team_projects : typing.Optional[bool]
            Whether to add users to team projects

        delete_users_from_team_projects : typing.Optional[bool]
            Whether to delete users from team projects

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Team
            Team details

        Examples
        --------
        import asyncio

        from fern.teams import V1TeamsPatchTeam

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.team_patch(
                account_id=1,
                id=1,
                team=V1TeamsPatchTeam(
                    name="Patched Team Name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.team_patch(
            account_id,
            id,
            team=team,
            add_users_to_team_projects=add_users_to_team_projects,
            delete_users_from_team_projects=delete_users_from_team_projects,
            request_options=request_options,
        )
        return _response.data
