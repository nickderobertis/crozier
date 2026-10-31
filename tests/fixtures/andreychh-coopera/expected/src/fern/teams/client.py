

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.team import Team
from ..types.team_list import TeamList
from ..types.team_name import TeamName
from .raw_client import AsyncRawTeamsClient, RawTeamsClient


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

    def create_team(self, *, name: TeamName, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Creates a team and makes the caller its owner. The caller must have introduced themselves first: a team has members, members are shown to one another, and someone without a name has nothing to show.

        Parameters
        ----------
        name : TeamName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.create_team(
            name="name",
        )
        """
        _response = self._raw_client.create_team(name=name, request_options=request_options)
        return _response.data

    def get_team(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Returns a team by its id.

        Parameters
        ----------
        id : str
            The team to read.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.get_team(
            id="id",
        )
        """
        _response = self._raw_client.get_team(id, request_options=request_options)
        return _response.data

    def list_my_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> TeamList:
        """
        Returns teams where the caller has an active membership, whatever their role in it, most recently joined first. A team left is a team gone from this list. Having no teams is not a failure but an ordinary state, and answers with an empty list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamList
            Caller's teams

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.teams.list_my_teams()
        """
        _response = self._raw_client.list_my_teams(request_options=request_options)
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

    async def create_team(self, *, name: TeamName, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Creates a team and makes the caller its owner. The caller must have introduced themselves first: a team has members, members are shown to one another, and someone without a name has nothing to show.

        Parameters
        ----------
        name : TeamName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.create_team(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team(name=name, request_options=request_options)
        return _response.data

    async def get_team(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Team:
        """
        Returns a team by its id.

        Parameters
        ----------
        id : str
            The team to read.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team
            Team found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.get_team(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team(id, request_options=request_options)
        return _response.data

    async def list_my_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> TeamList:
        """
        Returns teams where the caller has an active membership, whatever their role in it, most recently joined first. A team left is a team gone from this list. Having no teams is not a failure but an ordinary state, and answers with an empty list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamList
            Caller's teams

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.teams.list_my_teams()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_teams(request_options=request_options)
        return _response.data
