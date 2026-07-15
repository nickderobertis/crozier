

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.membership import Membership
from ..types.membership_list import MembershipList
from ..types.team import Team
from ..types.team_list import TeamList


OMIT = typing.cast(typing.Any, ...)


class RawTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TeamList]:
        """
        Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's teams. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamList]
            Teams List
        """
        _response = self._client_wrapper.httpx_client.request(
            "teams",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamList,
                    parse_obj_as(
                        type_=TeamList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        name: str,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Team]:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

        Parameters
        ----------
        name : str
            Team name. Max length: 128 chars.

        roles : typing.Optional[typing.Sequence[str]]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]
            Team
        """
        _response = self._client_wrapper.httpx_client.request(
            "teams",
            method="POST",
            json={
                "name": name,
                "roles": roles,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Team]:
        """
        Get a team by its unique ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]
            Team
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self, team_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Team]:
        """
        Update a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        name : str
            Team name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]
            Team
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
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
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_memberships(
        self,
        team_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MembershipList]:
        """
        Get a team members by the team unique ID. All team members have read access for this list of resources.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MembershipList]
            Memberships List
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MembershipList,
                    parse_obj_as(
                        type_=MembershipList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_membership(
        self,
        team_id: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Membership]:
        """
        Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member's email address if the member doesn't exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.

        Use the 'URL' parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.

        Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL's are the once from domains you have set when added your platforms in the console interface.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        email : str
            New team member email.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        url : str
            URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        name : typing.Optional[str]
            New team member name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Membership]
            Membership
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships",
            method="POST",
            json={
                "email": email,
                "name": name,
                "roles": roles,
                "url": url,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_membership(
        self, team_id: str, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_membership_roles(
        self,
        team_id: str,
        membership_id: str,
        *,
        roles: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Membership]:
        """


        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Membership]
            Membership
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}",
            method="PATCH",
            json={
                "roles": roles,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_membership_status(
        self,
        team_id: str,
        membership_id: str,
        *,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Membership]:
        """
        Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        secret : str
            Secret key.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Membership]
            Membership
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}/status",
            method="PATCH",
            json={
                "secret": secret,
                "userId": user_id,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TeamList]:
        """
        Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's teams. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamList]
            Teams List
        """
        _response = await self._client_wrapper.httpx_client.request(
            "teams",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamList,
                    parse_obj_as(
                        type_=TeamList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        name: str,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Team]:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

        Parameters
        ----------
        name : str
            Team name. Max length: 128 chars.

        roles : typing.Optional[typing.Sequence[str]]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]
            Team
        """
        _response = await self._client_wrapper.httpx_client.request(
            "teams",
            method="POST",
            json={
                "name": name,
                "roles": roles,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Team]:
        """
        Get a team by its unique ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]
            Team
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self, team_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Team]:
        """
        Update a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        name : str
            Team name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]
            Team
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
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
                    Team,
                    parse_obj_as(
                        type_=Team,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, team_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a team by its unique ID. Only team owners have write access for this resource.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_memberships(
        self,
        team_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MembershipList]:
        """
        Get a team members by the team unique ID. All team members have read access for this list of resources.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MembershipList]
            Memberships List
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MembershipList,
                    parse_obj_as(
                        type_=MembershipList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_membership(
        self,
        team_id: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Membership]:
        """
        Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member's email address if the member doesn't exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.

        Use the 'URL' parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.

        Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL's are the once from domains you have set when added your platforms in the console interface.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        email : str
            New team member email.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        url : str
            URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        name : typing.Optional[str]
            New team member name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Membership]
            Membership
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships",
            method="POST",
            json={
                "email": email,
                "name": name,
                "roles": roles,
                "url": url,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_membership(
        self, team_id: str, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_membership_roles(
        self,
        team_id: str,
        membership_id: str,
        *,
        roles: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Membership]:
        """


        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        roles : typing.Sequence[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Membership]
            Membership
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}",
            method="PATCH",
            json={
                "roles": roles,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_membership_status(
        self,
        team_id: str,
        membership_id: str,
        *,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Membership]:
        """
        Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

        Parameters
        ----------
        team_id : str
            Team unique ID.

        membership_id : str
            Membership ID.

        secret : str
            Secret key.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Membership]
            Membership
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{jsonable_encoder(team_id)}/memberships/{jsonable_encoder(membership_id)}/status",
            method="PATCH",
            json={
                "secret": secret,
                "userId": user_id,
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
                    Membership,
                    parse_obj_as(
                        type_=Membership,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
