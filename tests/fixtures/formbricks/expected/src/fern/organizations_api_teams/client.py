

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_id import OrganizationId
from ..types.team_id import TeamId
from .raw_client import AsyncRawOrganizationsApiTeamsClient, RawOrganizationsApiTeamsClient
from .types.create_team_response import CreateTeamResponse
from .types.delete_team_response import DeleteTeamResponse
from .types.get_team_response import GetTeamResponse
from .types.get_teams_request_filter_date_field import GetTeamsRequestFilterDateField
from .types.get_teams_request_order import GetTeamsRequestOrder
from .types.get_teams_request_sort_by import GetTeamsRequestSortBy
from .types.get_teams_response import GetTeamsResponse
from .types.update_team_response import UpdateTeamResponse


OMIT = typing.cast(typing.Any, ...)


class OrganizationsApiTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsApiTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsApiTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsApiTeamsClient
        """
        return self._raw_client

    def get_teams(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetTeamsRequestSortBy] = None,
        order: typing.Optional[GetTeamsRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetTeamsRequestFilterDateField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTeamsResponse:
        """
        Gets teams from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetTeamsRequestSortBy]
            Sort by field

        order : typing.Optional[GetTeamsRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetTeamsRequestFilterDateField]
            Date field to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamsResponse
            Teams retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_teams.get_teams(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_teams(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            request_options=request_options,
        )
        return _response.data

    def create_team(
        self, organization_id: OrganizationId, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTeamResponse:
        """
        Creates a team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        name : str
            The name of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTeamResponse
            Team created successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_teams.create_team(
            organization_id="organizationId",
            name="My team",
        )
        """
        _response = self._raw_client.create_team(organization_id, name=name, request_options=request_options)
        return _response.data

    def get_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTeamResponse:
        """
        Gets a team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamResponse
            Team retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_teams.get_team(
            organization_id="organizationId",
            id="id",
        )
        """
        _response = self._raw_client.get_team(organization_id, id, request_options=request_options)
        return _response.data

    def update_team(
        self,
        organization_id: OrganizationId,
        id: TeamId,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTeamResponse:
        """
        Updates a team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        name : str
            The name of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTeamResponse
            Team updated successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_teams.update_team(
            organization_id="organizationId",
            id="id",
            name="My team",
        )
        """
        _response = self._raw_client.update_team(organization_id, id, name=name, request_options=request_options)
        return _response.data

    def delete_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTeamResponse:
        """
        Deletes a team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTeamResponse
            Team deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_teams.delete_team(
            organization_id="organizationId",
            id="id",
        )
        """
        _response = self._raw_client.delete_team(organization_id, id, request_options=request_options)
        return _response.data


class AsyncOrganizationsApiTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsApiTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsApiTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsApiTeamsClient
        """
        return self._raw_client

    async def get_teams(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetTeamsRequestSortBy] = None,
        order: typing.Optional[GetTeamsRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetTeamsRequestFilterDateField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTeamsResponse:
        """
        Gets teams from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetTeamsRequestSortBy]
            Sort by field

        order : typing.Optional[GetTeamsRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetTeamsRequestFilterDateField]
            Date field to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamsResponse
            Teams retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_teams.get_teams(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_teams(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            request_options=request_options,
        )
        return _response.data

    async def create_team(
        self, organization_id: OrganizationId, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTeamResponse:
        """
        Creates a team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        name : str
            The name of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTeamResponse
            Team created successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_teams.create_team(
                organization_id="organizationId",
                name="My team",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team(organization_id, name=name, request_options=request_options)
        return _response.data

    async def get_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTeamResponse:
        """
        Gets a team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamResponse
            Team retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_teams.get_team(
                organization_id="organizationId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team(organization_id, id, request_options=request_options)
        return _response.data

    async def update_team(
        self,
        organization_id: OrganizationId,
        id: TeamId,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTeamResponse:
        """
        Updates a team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        name : str
            The name of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTeamResponse
            Team updated successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_teams.update_team(
                organization_id="organizationId",
                id="id",
                name="My team",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_team(organization_id, id, name=name, request_options=request_options)
        return _response.data

    async def delete_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTeamResponse:
        """
        Deletes a team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        id : TeamId
            The ID of the team

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTeamResponse
            Team deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_teams.delete_team(
                organization_id="organizationId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_team(organization_id, id, request_options=request_options)
        return _response.data
