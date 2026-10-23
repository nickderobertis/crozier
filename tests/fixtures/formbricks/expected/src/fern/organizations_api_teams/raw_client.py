

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
from ..types.team_id import TeamId
from .types.create_team_response import CreateTeamResponse
from .types.delete_team_response import DeleteTeamResponse
from .types.get_team_response import GetTeamResponse
from .types.get_teams_request_filter_date_field import GetTeamsRequestFilterDateField
from .types.get_teams_request_order import GetTeamsRequestOrder
from .types.get_teams_request_sort_by import GetTeamsRequestSortBy
from .types.get_teams_response import GetTeamsResponse
from .types.update_team_response import UpdateTeamResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOrganizationsApiTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetTeamsResponse]:
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
        HttpResponse[GetTeamsResponse]
            Teams retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamsResponse,
                    parse_obj_as(
                        type_=GetTeamsResponse,
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

    def create_team(
        self, organization_id: OrganizationId, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateTeamResponse]:
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
        HttpResponse[CreateTeamResponse]
            Team created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams",
            method="POST",
            json={
                "name": name,
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
                    CreateTeamResponse,
                    parse_obj_as(
                        type_=CreateTeamResponse,
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

    def get_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTeamResponse]:
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
        HttpResponse[GetTeamResponse]
            Team retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamResponse,
                    parse_obj_as(
                        type_=GetTeamResponse,
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

    def update_team(
        self,
        organization_id: OrganizationId,
        id: TeamId,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTeamResponse]:
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
        HttpResponse[UpdateTeamResponse]
            Team updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
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
                    UpdateTeamResponse,
                    parse_obj_as(
                        type_=UpdateTeamResponse,
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

    def delete_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteTeamResponse]:
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
        HttpResponse[DeleteTeamResponse]
            Team deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTeamResponse,
                    parse_obj_as(
                        type_=DeleteTeamResponse,
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


class AsyncRawOrganizationsApiTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetTeamsResponse]:
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
        AsyncHttpResponse[GetTeamsResponse]
            Teams retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamsResponse,
                    parse_obj_as(
                        type_=GetTeamsResponse,
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

    async def create_team(
        self, organization_id: OrganizationId, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateTeamResponse]:
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
        AsyncHttpResponse[CreateTeamResponse]
            Team created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams",
            method="POST",
            json={
                "name": name,
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
                    CreateTeamResponse,
                    parse_obj_as(
                        type_=CreateTeamResponse,
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

    async def get_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTeamResponse]:
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
        AsyncHttpResponse[GetTeamResponse]
            Team retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamResponse,
                    parse_obj_as(
                        type_=GetTeamResponse,
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

    async def update_team(
        self,
        organization_id: OrganizationId,
        id: TeamId,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTeamResponse]:
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
        AsyncHttpResponse[UpdateTeamResponse]
            Team updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
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
                    UpdateTeamResponse,
                    parse_obj_as(
                        type_=UpdateTeamResponse,
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

    async def delete_team(
        self, organization_id: OrganizationId, id: TeamId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteTeamResponse]:
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
        AsyncHttpResponse[DeleteTeamResponse]
            Team deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"organizations/{encode_path_param(organization_id)}/teams/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTeamResponse,
                    parse_obj_as(
                        type_=DeleteTeamResponse,
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
