

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawTeamClient, RawTeamClient


OMIT = typing.cast(typing.Any, ...)


class TeamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeamClient
        """
        return self._raw_client

    def create_team_member(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTeamMemberResponse:
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
        CreateTeamMemberResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.create_team_member()
        """
        _response = self._raw_client.create_team_member(
            idempotency_key=idempotency_key, team_member=team_member, request_options=request_options
        )
        return _response.data

    def bulk_create_team_members(
        self,
        *,
        team_members: typing.Dict[str, CreateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkCreateTeamMembersResponse:
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
        BulkCreateTeamMembersResponse
            Success

        Examples
        --------
        from fern import CreateTeamMemberRequest, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.bulk_create_team_members(
            team_members={"key": CreateTeamMemberRequest()},
        )
        """
        _response = self._raw_client.bulk_create_team_members(
            team_members=team_members, request_options=request_options
        )
        return _response.data

    def bulk_update_team_members(
        self,
        *,
        team_members: typing.Dict[str, UpdateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkUpdateTeamMembersResponse:
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
        BulkUpdateTeamMembersResponse
            Success

        Examples
        --------
        from fern import FernApi, UpdateTeamMemberRequest

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.bulk_update_team_members(
            team_members={"key": UpdateTeamMemberRequest()},
        )
        """
        _response = self._raw_client.bulk_update_team_members(
            team_members=team_members, request_options=request_options
        )
        return _response.data

    def search_team_members(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchTeamMembersQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTeamMembersResponse:
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
        SearchTeamMembersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.search_team_members()
        """
        _response = self._raw_client.search_team_members(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def retrieve_team_member(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTeamMemberResponse:
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
        RetrieveTeamMemberResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.retrieve_team_member(
            team_member_id="team_member_id",
        )
        """
        _response = self._raw_client.retrieve_team_member(team_member_id, request_options=request_options)
        return _response.data

    def update_team_member(
        self,
        team_member_id: str,
        *,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTeamMemberResponse:
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
        UpdateTeamMemberResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.update_team_member(
            team_member_id="team_member_id",
        )
        """
        _response = self._raw_client.update_team_member(
            team_member_id, team_member=team_member, request_options=request_options
        )
        return _response.data

    def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveWageSettingResponse:
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
        RetrieveWageSettingResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.retrieve_wage_setting(
            team_member_id="team_member_id",
        )
        """
        _response = self._raw_client.retrieve_wage_setting(team_member_id, request_options=request_options)
        return _response.data

    def update_wage_setting(
        self, team_member_id: str, *, wage_setting: WageSetting, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWageSettingResponse:
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
        UpdateWageSettingResponse
            Success

        Examples
        --------
        from fern import FernApi, WageSetting

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.team.update_wage_setting(
            team_member_id="team_member_id",
            wage_setting=WageSetting(),
        )
        """
        _response = self._raw_client.update_wage_setting(
            team_member_id, wage_setting=wage_setting, request_options=request_options
        )
        return _response.data


class AsyncTeamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeamClient
        """
        return self._raw_client

    async def create_team_member(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTeamMemberResponse:
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
        CreateTeamMemberResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.create_team_member()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_team_member(
            idempotency_key=idempotency_key, team_member=team_member, request_options=request_options
        )
        return _response.data

    async def bulk_create_team_members(
        self,
        *,
        team_members: typing.Dict[str, CreateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkCreateTeamMembersResponse:
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
        BulkCreateTeamMembersResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateTeamMemberRequest

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.bulk_create_team_members(
                team_members={"key": CreateTeamMemberRequest()},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_team_members(
            team_members=team_members, request_options=request_options
        )
        return _response.data

    async def bulk_update_team_members(
        self,
        *,
        team_members: typing.Dict[str, UpdateTeamMemberRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkUpdateTeamMembersResponse:
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
        BulkUpdateTeamMembersResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateTeamMemberRequest

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.bulk_update_team_members(
                team_members={"key": UpdateTeamMemberRequest()},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_team_members(
            team_members=team_members, request_options=request_options
        )
        return _response.data

    async def search_team_members(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchTeamMembersQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTeamMembersResponse:
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
        SearchTeamMembersResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.search_team_members()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_team_members(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def retrieve_team_member(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTeamMemberResponse:
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
        RetrieveTeamMemberResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.retrieve_team_member(
                team_member_id="team_member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_team_member(team_member_id, request_options=request_options)
        return _response.data

    async def update_team_member(
        self,
        team_member_id: str,
        *,
        team_member: typing.Optional[TeamMember] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTeamMemberResponse:
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
        UpdateTeamMemberResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.update_team_member(
                team_member_id="team_member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_team_member(
            team_member_id, team_member=team_member, request_options=request_options
        )
        return _response.data

    async def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveWageSettingResponse:
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
        RetrieveWageSettingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.retrieve_wage_setting(
                team_member_id="team_member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_wage_setting(team_member_id, request_options=request_options)
        return _response.data

    async def update_wage_setting(
        self, team_member_id: str, *, wage_setting: WageSetting, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWageSettingResponse:
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
        UpdateWageSettingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WageSetting

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.team.update_wage_setting(
                team_member_id="team_member_id",
                wage_setting=WageSetting(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_wage_setting(
            team_member_id, wage_setting=wage_setting, request_options=request_options
        )
        return _response.data
