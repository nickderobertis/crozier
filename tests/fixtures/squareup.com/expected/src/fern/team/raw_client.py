

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.bulk_create_team_members_response import BulkCreateTeamMembersResponse
from ..types.bulk_update_team_members_response import BulkUpdateTeamMembersResponse
from ..types.create_team_member_request import CreateTeamMemberRequest
from ..types.create_team_member_response import CreateTeamMemberResponse
from ..types.retrieve_team_member_response import RetrieveTeamMemberResponse
from ..types.retrieve_wage_setting_response import RetrieveWageSettingResponse
from ..types.search_team_members_query import SearchTeamMembersQuery
from ..types.search_team_members_response import SearchTeamMembersResponse
from ..types.team_member import TeamMember
from ..types.update_team_member_request import UpdateTeamMemberRequest
from ..types.update_team_member_response import UpdateTeamMemberResponse
from ..types.update_wage_setting_response import UpdateWageSettingResponse
from ..types.wage_setting import WageSetting


OMIT = typing.cast(typing.Any, ...)


class RawTeamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_team_member(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTeamMemberResponse]:
        """
        Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
        You must provide the following values in your request to this endpoint:
        - `given_name`
        - `family_name`

        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            A unique string that identifies this `CreateTeamMember` request.
            Keys can be any valid string, but must be unique for every request.
            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

            The minimum length is 1 and the maximum length is 45.

        team_member : typing.Optional[TeamMember]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTeamMemberResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/team-members",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "team_member": convert_and_respect_annotation_metadata(
                    object_=team_member, annotation=TeamMember, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTeamMemberResponse,
                    parse_obj_as(
                        type_=CreateTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_create_team_members(
        self,
        *,
        team_members: typing.Dict[str, CreateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkCreateTeamMembersResponse]:
        """
        Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
        This process is non-transactional and processes as much of the request as possible. If one of the creates in
        the request cannot be successfully processed, the request is not marked as failed, but the body of the response
        contains explicit error information for the failed create.

        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

        Parameters
        ----------
        team_members : typing.Dict[str, CreateTeamMemberRequest]
            The data used to create the `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkCreateTeamMembersResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/team-members/bulk-create",
            method="POST",
            json={
                "team_members": convert_and_respect_annotation_metadata(
                    object_=team_members, annotation=typing.Dict[str, CreateTeamMemberRequest], direction="write"
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
                    BulkCreateTeamMembersResponse,
                    parse_obj_as(
                        type_=BulkCreateTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_update_team_members(
        self,
        *,
        team_members: typing.Dict[str, UpdateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkUpdateTeamMembersResponse]:
        """
        Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
        This process is non-transactional and processes as much of the request as possible. If one of the updates in
        the request cannot be successfully processed, the request is not marked as failed, but the body of the response
        contains explicit error information for the failed update.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

        Parameters
        ----------
        team_members : typing.Dict[str, UpdateTeamMemberRequest]
            The data used to update the `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkUpdateTeamMembersResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/team-members/bulk-update",
            method="POST",
            json={
                "team_members": convert_and_respect_annotation_metadata(
                    object_=team_members, annotation=typing.Dict[str, UpdateTeamMemberRequest], direction="write"
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
                    BulkUpdateTeamMembersResponse,
                    parse_obj_as(
                        type_=BulkUpdateTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_team_members(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchTeamMembersQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchTeamMembersResponse]:
        """
        Returns a paginated list of `TeamMember` objects for a business.
        The list can be filtered by the following:
        - location IDs
        - `status`

        Parameters
        ----------
        cursor : typing.Optional[str]
            The opaque cursor for fetching the next page. For more information, see
            [pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of `TeamMember` objects in a page (100 by default).

        query : typing.Optional[SearchTeamMembersQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchTeamMembersResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/team-members/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchTeamMembersQuery, direction="write"
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
                    SearchTeamMembersResponse,
                    parse_obj_as(
                        type_=SearchTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_team_member(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveTeamMemberResponse]:
        """
        Retrieves a `TeamMember` object for the given `TeamMember.id`.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveTeamMemberResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTeamMemberResponse,
                    parse_obj_as(
                        type_=RetrieveTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_team_member(
        self,
        team_member_id: str,
        *,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTeamMemberResponse]:
        """
        Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to update.

        team_member : typing.Optional[TeamMember]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateTeamMemberResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}",
            method="PUT",
            json={
                "team_member": convert_and_respect_annotation_metadata(
                    object_=team_member, annotation=TeamMember, direction="write"
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
                    UpdateTeamMemberResponse,
                    parse_obj_as(
                        type_=UpdateTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveWageSettingResponse]:
        """
        Retrieves a `WageSetting` object for a team member specified
        by `TeamMember.id`.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member for which to retrieve the wage setting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveWageSettingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}/wage-setting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveWageSettingResponse,
                    parse_obj_as(
                        type_=RetrieveWageSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_wage_setting(
        self, team_member_id: str, *, wage_setting: WageSetting, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateWageSettingResponse]:
        """
        Creates or updates a `WageSetting` object. The object is created if a
        `WageSetting` with the specified `team_member_id` does not exist. Otherwise,
        it fully replaces the `WageSetting` object for the team member.
        The `WageSetting` is returned on a successful update.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member for which to update the `WageSetting` object.

        wage_setting : WageSetting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateWageSettingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}/wage-setting",
            method="PUT",
            json={
                "wage_setting": convert_and_respect_annotation_metadata(
                    object_=wage_setting, annotation=WageSetting, direction="write"
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
                    UpdateWageSettingResponse,
                    parse_obj_as(
                        type_=UpdateWageSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTeamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_team_member(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTeamMemberResponse]:
        """
        Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
        You must provide the following values in your request to this endpoint:
        - `given_name`
        - `family_name`

        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            A unique string that identifies this `CreateTeamMember` request.
            Keys can be any valid string, but must be unique for every request.
            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

            The minimum length is 1 and the maximum length is 45.

        team_member : typing.Optional[TeamMember]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTeamMemberResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/team-members",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "team_member": convert_and_respect_annotation_metadata(
                    object_=team_member, annotation=TeamMember, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTeamMemberResponse,
                    parse_obj_as(
                        type_=CreateTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_create_team_members(
        self,
        *,
        team_members: typing.Dict[str, CreateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkCreateTeamMembersResponse]:
        """
        Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
        This process is non-transactional and processes as much of the request as possible. If one of the creates in
        the request cannot be successfully processed, the request is not marked as failed, but the body of the response
        contains explicit error information for the failed create.

        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

        Parameters
        ----------
        team_members : typing.Dict[str, CreateTeamMemberRequest]
            The data used to create the `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkCreateTeamMembersResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/team-members/bulk-create",
            method="POST",
            json={
                "team_members": convert_and_respect_annotation_metadata(
                    object_=team_members, annotation=typing.Dict[str, CreateTeamMemberRequest], direction="write"
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
                    BulkCreateTeamMembersResponse,
                    parse_obj_as(
                        type_=BulkCreateTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_update_team_members(
        self,
        *,
        team_members: typing.Dict[str, UpdateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkUpdateTeamMembersResponse]:
        """
        Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
        This process is non-transactional and processes as much of the request as possible. If one of the updates in
        the request cannot be successfully processed, the request is not marked as failed, but the body of the response
        contains explicit error information for the failed update.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

        Parameters
        ----------
        team_members : typing.Dict[str, UpdateTeamMemberRequest]
            The data used to update the `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkUpdateTeamMembersResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/team-members/bulk-update",
            method="POST",
            json={
                "team_members": convert_and_respect_annotation_metadata(
                    object_=team_members, annotation=typing.Dict[str, UpdateTeamMemberRequest], direction="write"
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
                    BulkUpdateTeamMembersResponse,
                    parse_obj_as(
                        type_=BulkUpdateTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_team_members(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchTeamMembersQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchTeamMembersResponse]:
        """
        Returns a paginated list of `TeamMember` objects for a business.
        The list can be filtered by the following:
        - location IDs
        - `status`

        Parameters
        ----------
        cursor : typing.Optional[str]
            The opaque cursor for fetching the next page. For more information, see
            [pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of `TeamMember` objects in a page (100 by default).

        query : typing.Optional[SearchTeamMembersQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchTeamMembersResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/team-members/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchTeamMembersQuery, direction="write"
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
                    SearchTeamMembersResponse,
                    parse_obj_as(
                        type_=SearchTeamMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_team_member(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveTeamMemberResponse]:
        """
        Retrieves a `TeamMember` object for the given `TeamMember.id`.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveTeamMemberResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTeamMemberResponse,
                    parse_obj_as(
                        type_=RetrieveTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_team_member(
        self,
        team_member_id: str,
        *,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTeamMemberResponse]:
        """
        Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to update.

        team_member : typing.Optional[TeamMember]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateTeamMemberResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}",
            method="PUT",
            json={
                "team_member": convert_and_respect_annotation_metadata(
                    object_=team_member, annotation=TeamMember, direction="write"
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
                    UpdateTeamMemberResponse,
                    parse_obj_as(
                        type_=UpdateTeamMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveWageSettingResponse]:
        """
        Retrieves a `WageSetting` object for a team member specified
        by `TeamMember.id`.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member for which to retrieve the wage setting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveWageSettingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}/wage-setting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveWageSettingResponse,
                    parse_obj_as(
                        type_=RetrieveWageSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_wage_setting(
        self, team_member_id: str, *, wage_setting: WageSetting, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateWageSettingResponse]:
        """
        Creates or updates a `WageSetting` object. The object is created if a
        `WageSetting` with the specified `team_member_id` does not exist. Otherwise,
        it fully replaces the `WageSetting` object for the team member.
        The `WageSetting` is returned on a successful update.
        Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

        Parameters
        ----------
        team_member_id : str
            The ID of the team member for which to update the `WageSetting` object.

        wage_setting : WageSetting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateWageSettingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/team-members/{jsonable_encoder(team_member_id)}/wage-setting",
            method="PUT",
            json={
                "wage_setting": convert_and_respect_annotation_metadata(
                    object_=wage_setting, annotation=WageSetting, direction="write"
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
                    UpdateWageSettingResponse,
                    parse_obj_as(
                        type_=UpdateWageSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
