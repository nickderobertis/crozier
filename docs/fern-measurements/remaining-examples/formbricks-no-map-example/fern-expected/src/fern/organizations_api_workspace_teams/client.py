

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_id import OrganizationId
from .raw_client import AsyncRawOrganizationsApiWorkspaceTeamsClient, RawOrganizationsApiWorkspaceTeamsClient
from .types.create_workspace_team_request_permission import CreateWorkspaceTeamRequestPermission
from .types.create_workspace_team_response import CreateWorkspaceTeamResponse
from .types.delete_workspace_team_response import DeleteWorkspaceTeamResponse
from .types.get_workspace_teams_request_filter_date_field import GetWorkspaceTeamsRequestFilterDateField
from .types.get_workspace_teams_request_order import GetWorkspaceTeamsRequestOrder
from .types.get_workspace_teams_request_sort_by import GetWorkspaceTeamsRequestSortBy
from .types.get_workspace_teams_response import GetWorkspaceTeamsResponse
from .types.update_workspace_team_request_permission import UpdateWorkspaceTeamRequestPermission
from .types.update_workspace_team_response import UpdateWorkspaceTeamResponse


OMIT = typing.cast(typing.Any, ...)


class OrganizationsApiWorkspaceTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsApiWorkspaceTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsApiWorkspaceTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsApiWorkspaceTeamsClient
        """
        return self._raw_client

    def get_workspace_teams(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetWorkspaceTeamsRequestSortBy] = None,
        order: typing.Optional[GetWorkspaceTeamsRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetWorkspaceTeamsRequestFilterDateField] = None,
        team_id: typing.Optional[str] = None,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWorkspaceTeamsResponse:
        """
        Gets workspace teams from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetWorkspaceTeamsRequestSortBy]
            Sort by field

        order : typing.Optional[GetWorkspaceTeamsRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetWorkspaceTeamsRequestFilterDateField]
            Date field to filter by

        team_id : typing.Optional[str]

        workspace_id : typing.Optional[str]
            The ID of the Workspace to filter by

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceTeamsResponse
            Workspace teams retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_workspace_teams.get_workspace_teams(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_workspace_teams(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            team_id=team_id,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def create_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: CreateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWorkspaceTeamResponse:
        """
        Creates a Workspace team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str
            The ID of the team

        permission : CreateWorkspaceTeamRequestPermission
            Level of access granted to the Workspace

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWorkspaceTeamResponse
            Workspace team created successfully.

        Examples
        --------
        from fern.organizations_api_workspace_teams import (
            CreateWorkspaceTeamRequestPermission,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_workspace_teams.create_workspace_team(
            organization_id="organizationId",
            team_id="teamId",
            permission=CreateWorkspaceTeamRequestPermission.READ,
        )
        """
        _response = self._raw_client.create_workspace_team(
            organization_id,
            team_id=team_id,
            permission=permission,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def update_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: UpdateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWorkspaceTeamResponse:
        """
        Updates a Workspace team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str
            The ID of the team

        permission : UpdateWorkspaceTeamRequestPermission
            Level of access granted to the Workspace

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkspaceTeamResponse
            Workspace team updated successfully.

        Examples
        --------
        from fern.organizations_api_workspace_teams import (
            UpdateWorkspaceTeamRequestPermission,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_workspace_teams.update_workspace_team(
            organization_id="organizationId",
            team_id="teamId",
            permission=UpdateWorkspaceTeamRequestPermission.READ,
        )
        """
        _response = self._raw_client.update_workspace_team(
            organization_id,
            team_id=team_id,
            permission=permission,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def delete_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteWorkspaceTeamResponse:
        """
        Deletes a Workspace team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceTeamResponse
            Workspace team deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations_api_workspace_teams.delete_workspace_team(
            organization_id="organizationId",
            team_id="teamId",
        )
        """
        _response = self._raw_client.delete_workspace_team(
            organization_id,
            team_id=team_id,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data


class AsyncOrganizationsApiWorkspaceTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsApiWorkspaceTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsApiWorkspaceTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsApiWorkspaceTeamsClient
        """
        return self._raw_client

    async def get_workspace_teams(
        self,
        organization_id: OrganizationId,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetWorkspaceTeamsRequestSortBy] = None,
        order: typing.Optional[GetWorkspaceTeamsRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetWorkspaceTeamsRequestFilterDateField] = None,
        team_id: typing.Optional[str] = None,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWorkspaceTeamsResponse:
        """
        Gets workspace teams from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetWorkspaceTeamsRequestSortBy]
            Sort by field

        order : typing.Optional[GetWorkspaceTeamsRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetWorkspaceTeamsRequestFilterDateField]
            Date field to filter by

        team_id : typing.Optional[str]

        workspace_id : typing.Optional[str]
            The ID of the Workspace to filter by

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceTeamsResponse
            Workspace teams retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_workspace_teams.get_workspace_teams(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_teams(
            organization_id,
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            team_id=team_id,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def create_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: CreateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWorkspaceTeamResponse:
        """
        Creates a Workspace team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str
            The ID of the team

        permission : CreateWorkspaceTeamRequestPermission
            Level of access granted to the Workspace

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWorkspaceTeamResponse
            Workspace team created successfully.

        Examples
        --------
        import asyncio

        from fern.organizations_api_workspace_teams import (
            CreateWorkspaceTeamRequestPermission,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_workspace_teams.create_workspace_team(
                organization_id="organizationId",
                team_id="teamId",
                permission=CreateWorkspaceTeamRequestPermission.READ,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace_team(
            organization_id,
            team_id=team_id,
            permission=permission,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def update_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: UpdateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWorkspaceTeamResponse:
        """
        Updates a Workspace team in the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str
            The ID of the team

        permission : UpdateWorkspaceTeamRequestPermission
            Level of access granted to the Workspace

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkspaceTeamResponse
            Workspace team updated successfully.

        Examples
        --------
        import asyncio

        from fern.organizations_api_workspace_teams import (
            UpdateWorkspaceTeamRequestPermission,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_workspace_teams.update_workspace_team(
                organization_id="organizationId",
                team_id="teamId",
                permission=UpdateWorkspaceTeamRequestPermission.READ,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workspace_team(
            organization_id,
            team_id=team_id,
            permission=permission,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteWorkspaceTeamResponse:
        """
        Deletes a Workspace team from the database.

        Parameters
        ----------
        organization_id : OrganizationId
            The ID of the organization

        team_id : str

        workspace_id : typing.Optional[str]
            The ID of the Workspace

        project_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceTeamResponse
            Workspace team deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations_api_workspace_teams.delete_workspace_team(
                organization_id="organizationId",
                team_id="teamId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace_team(
            organization_id,
            team_id=team_id,
            workspace_id=workspace_id,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data
