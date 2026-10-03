

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.items_result_of_team import ItemsResultOfTeam
from ..types.items_result_of_team_membership import ItemsResultOfTeamMembership
from ..types.sort_direction import SortDirection
from ..types.team import Team
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

    def getteams(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfTeam:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfTeam


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.getteams()
        """
        _response = self._raw_client.getteams(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createteam(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.createteam()
        """
        _response = self._raw_client.createteam(
            organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def getteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.getteam(
            id="id",
        )
        """
        _response = self._raw_client.getteam(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def updateteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.updateteam(
            id="id",
        )
        """
        _response = self._raw_client.updateteam(
            id, organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def deleteteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.deleteteam(
            id="id",
        )
        """
        _response = self._raw_client.deleteteam(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def addmember(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.addmember(
            id="id",
        )
        """
        _response = self._raw_client.addmember(
            id, organization_id=organization_id, user_id=user_id, request_options=request_options
        )
        return _response.data

    def removemember(
        self,
        id: str,
        user_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        user_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.removemember(
            id="id",
            user_id="userId",
        )
        """
        _response = self._raw_client.removemember(
            id, user_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def getmemberships(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfTeamMembership:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfTeamMembership


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.teams.getmemberships(
            id="id",
        )
        """
        _response = self._raw_client.getmemberships(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
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

    async def getteams(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfTeam:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfTeam


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.getteams()


        asyncio.run(main())
        """
        _response = await self._raw_client.getteams(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createteam(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.createteam()


        asyncio.run(main())
        """
        _response = await self._raw_client.createteam(
            organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def getteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.getteam(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getteam(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    async def updateteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.updateteam(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateteam(
            id, organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def deleteteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.deleteteam(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteteam(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def addmember(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.addmember(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addmember(
            id, organization_id=organization_id, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def removemember(
        self,
        id: str,
        user_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        user_id : str

        organization_id : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.removemember(
                id="id",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removemember(
            id, user_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def getmemberships(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfTeamMembership:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfTeamMembership


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.teams.getmemberships(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmemberships(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data
