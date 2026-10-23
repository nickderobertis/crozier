

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.organization_id import OrganizationId
from .types.create_workspace_team_request_permission import CreateWorkspaceTeamRequestPermission
from .types.create_workspace_team_response import CreateWorkspaceTeamResponse
from .types.delete_workspace_team_response import DeleteWorkspaceTeamResponse
from .types.get_workspace_teams_request_filter_date_field import GetWorkspaceTeamsRequestFilterDateField
from .types.get_workspace_teams_request_order import GetWorkspaceTeamsRequestOrder
from .types.get_workspace_teams_request_sort_by import GetWorkspaceTeamsRequestSortBy
from .types.get_workspace_teams_response import GetWorkspaceTeamsResponse
from .types.update_workspace_team_request_permission import UpdateWorkspaceTeamRequestPermission
from .types.update_workspace_team_response import UpdateWorkspaceTeamResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOrganizationsApiWorkspaceTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetWorkspaceTeamsResponse]:
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
        HttpResponse[GetWorkspaceTeamsResponse]
            Workspace teams retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWorkspaceTeamsResponse,
                    parse_obj_as(
                        type_=GetWorkspaceTeamsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: CreateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateWorkspaceTeamResponse]:
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
        HttpResponse[CreateWorkspaceTeamResponse]
            Workspace team created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="POST",
            json={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
                "permission": permission,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=CreateWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: UpdateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWorkspaceTeamResponse]:
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
        HttpResponse[UpdateWorkspaceTeamResponse]
            Workspace team updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="PUT",
            json={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
                "permission": permission,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=UpdateWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteWorkspaceTeamResponse]:
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
        HttpResponse[DeleteWorkspaceTeamResponse]
            Workspace team deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="DELETE",
            params={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=DeleteWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOrganizationsApiWorkspaceTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetWorkspaceTeamsResponse]:
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
        AsyncHttpResponse[GetWorkspaceTeamsResponse]
            Workspace teams retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWorkspaceTeamsResponse,
                    parse_obj_as(
                        type_=GetWorkspaceTeamsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: CreateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateWorkspaceTeamResponse]:
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
        AsyncHttpResponse[CreateWorkspaceTeamResponse]
            Workspace team created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="POST",
            json={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
                "permission": permission,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=CreateWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        permission: UpdateWorkspaceTeamRequestPermission,
        workspace_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateWorkspaceTeamResponse]:
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
        AsyncHttpResponse[UpdateWorkspaceTeamResponse]
            Workspace team updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="PUT",
            json={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
                "permission": permission,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=UpdateWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_workspace_team(
        self,
        organization_id: OrganizationId,
        *,
        team_id: str,
        workspace_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteWorkspaceTeamResponse]:
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
        AsyncHttpResponse[DeleteWorkspaceTeamResponse]
            Workspace team deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/workspace-teams",
            method="DELETE",
            params={
                "teamId": team_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteWorkspaceTeamResponse,
                    parse_obj_as(
                        type_=DeleteWorkspaceTeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
