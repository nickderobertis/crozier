

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.v1team import V1Team
from .types.delete11account_id_teams_id_response import Delete11AccountIdTeamsIdResponse
from .types.v1teams_create_team import V1TeamsCreateTeam
from .types.v1teams_patch_team import V1TeamsPatchTeam
from .types.v1teams_update_team import V1TeamsUpdateTeam
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_teams(
        self,
        account_id: int,
        *,
        q: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Team]]:
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
        HttpResponse[typing.List[V1Team]]
            Teams found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/search",
            method="GET",
            params={
                "q": q,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Team],
                    parse_obj_as(
                        type_=typing.List[V1Team],
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

    def list_all_teams_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Team]]:
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
        HttpResponse[typing.List[V1Team]]
            Team details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "offset": offset,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Team],
                    parse_obj_as(
                        type_=typing.List[V1Team],
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
        self, account_id: int, *, team: V1TeamsCreateTeam, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Team]:
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
        HttpResponse[V1Team]
            Team
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams",
            method="POST",
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsCreateTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def team_details(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Team]:
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
        HttpResponse[V1Team]
            Team details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def team_update(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsUpdateTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Team]:
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
        HttpResponse[V1Team]
            Team details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="PUT",
            params={
                "add_users_to_team_projects": add_users_to_team_projects,
                "delete_users_from_team_projects": delete_users_from_team_projects,
            },
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsUpdateTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def team_delete(
        self,
        account_id: int,
        id: int,
        *,
        delete_project_users: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Delete11AccountIdTeamsIdResponse]:
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
        HttpResponse[Delete11AccountIdTeamsIdResponse]
            Team deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="DELETE",
            params={
                "delete_project_users": delete_project_users,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Delete11AccountIdTeamsIdResponse,
                    parse_obj_as(
                        type_=Delete11AccountIdTeamsIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def team_patch(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsPatchTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Team]:
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
        HttpResponse[V1Team]
            Team details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="PATCH",
            params={
                "add_users_to_team_projects": add_users_to_team_projects,
                "delete_users_from_team_projects": delete_users_from_team_projects,
            },
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsPatchTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_teams(
        self,
        account_id: int,
        *,
        q: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Team]]:
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
        AsyncHttpResponse[typing.List[V1Team]]
            Teams found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/search",
            method="GET",
            params={
                "q": q,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Team],
                    parse_obj_as(
                        type_=typing.List[V1Team],
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

    async def list_all_teams_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Team]]:
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
        AsyncHttpResponse[typing.List[V1Team]]
            Team details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "offset": offset,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Team],
                    parse_obj_as(
                        type_=typing.List[V1Team],
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
        self, account_id: int, *, team: V1TeamsCreateTeam, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Team]:
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
        AsyncHttpResponse[V1Team]
            Team
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams",
            method="POST",
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsCreateTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def team_details(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Team]:
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
        AsyncHttpResponse[V1Team]
            Team details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def team_update(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsUpdateTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Team]:
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
        AsyncHttpResponse[V1Team]
            Team details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="PUT",
            params={
                "add_users_to_team_projects": add_users_to_team_projects,
                "delete_users_from_team_projects": delete_users_from_team_projects,
            },
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsUpdateTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def team_delete(
        self,
        account_id: int,
        id: int,
        *,
        delete_project_users: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Delete11AccountIdTeamsIdResponse]:
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
        AsyncHttpResponse[Delete11AccountIdTeamsIdResponse]
            Team deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="DELETE",
            params={
                "delete_project_users": delete_project_users,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Delete11AccountIdTeamsIdResponse,
                    parse_obj_as(
                        type_=Delete11AccountIdTeamsIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def team_patch(
        self,
        account_id: int,
        id: int,
        *,
        team: V1TeamsPatchTeam,
        add_users_to_team_projects: typing.Optional[bool] = None,
        delete_users_from_team_projects: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Team]:
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
        AsyncHttpResponse[V1Team]
            Team details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/teams/{encode_path_param(id)}",
            method="PATCH",
            params={
                "add_users_to_team_projects": add_users_to_team_projects,
                "delete_users_from_team_projects": delete_users_from_team_projects,
            },
            json={
                "team": convert_and_respect_annotation_metadata(
                    object_=team, annotation=V1TeamsPatchTeam, direction="write"
                ),
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
                    V1Team,
                    parse_obj_as(
                        type_=V1Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
