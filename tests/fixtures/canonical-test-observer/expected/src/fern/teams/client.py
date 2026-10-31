

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artefact_matching_rule_base import ArtefactMatchingRuleBase
from ..types.permission import Permission
from ..types.team_response import TeamResponse
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

    def get_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TeamResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TeamResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.get_teams()
        """
        _response = self._raw_client.get_teams(request_options=request_options)
        return _response.data

    def create_team(
        self,
        *,
        name: str,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamResponse:
        """
        Create a new team

        Parameters
        ----------
        name : str

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.create_team(
            name="name",
        )
        """
        _response = self._raw_client.create_team(
            name=name,
            permissions=permissions,
            artefact_matching_rules=artefact_matching_rules,
            request_options=request_options,
        )
        return _response.data

    def get_team(self, team_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> TeamResponse:
        """
        Parameters
        ----------
        team_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.get_team(
            team_id=1,
        )
        """
        _response = self._raw_client.get_team(team_id, request_options=request_options)
        return _response.data

    def update_team(
        self,
        team_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamResponse:
        """
        Parameters
        ----------
        team_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.update_team(
            team_id=1,
        )
        """
        _response = self._raw_client.update_team(
            team_id,
            permissions=permissions,
            artefact_matching_rules=artefact_matching_rules,
            request_options=request_options,
        )
        return _response.data

    def add_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TeamResponse:
        """
        Add a user to a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.add_team_member(
            team_id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.add_team_member(team_id, user_id, request_options=request_options)
        return _response.data

    def remove_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TeamResponse:
        """
        Remove a user from a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.teams.remove_team_member(
            team_id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.remove_team_member(team_id, user_id, request_options=request_options)
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

    async def get_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TeamResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TeamResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.get_teams()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_teams(request_options=request_options)
        return _response.data

    async def create_team(
        self,
        *,
        name: str,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamResponse:
        """
        Create a new team

        Parameters
        ----------
        name : str

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.create_team(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team(
            name=name,
            permissions=permissions,
            artefact_matching_rules=artefact_matching_rules,
            request_options=request_options,
        )
        return _response.data

    async def get_team(self, team_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> TeamResponse:
        """
        Parameters
        ----------
        team_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.get_team(
                team_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team(team_id, request_options=request_options)
        return _response.data

    async def update_team(
        self,
        team_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeamResponse:
        """
        Parameters
        ----------
        team_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.update_team(
                team_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_team(
            team_id,
            permissions=permissions,
            artefact_matching_rules=artefact_matching_rules,
            request_options=request_options,
        )
        return _response.data

    async def add_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TeamResponse:
        """
        Add a user to a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.add_team_member(
                team_id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_team_member(team_id, user_id, request_options=request_options)
        return _response.data

    async def remove_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TeamResponse:
        """
        Remove a user from a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.teams.remove_team_member(
                team_id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_team_member(team_id, user_id, request_options=request_options)
        return _response.data
