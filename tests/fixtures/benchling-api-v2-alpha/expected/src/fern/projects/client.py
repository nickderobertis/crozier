

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collaborations_paginated_list import CollaborationsPaginatedList
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.list_project_collaborations_request_role import ListProjectCollaborationsRequestRole
from .types.list_project_collaborations_request_sort import ListProjectCollaborationsRequestSort


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

    def list_project_collaborations(
        self,
        project_id: str,
        *,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListProjectCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListProjectCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified project. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Projects).

        Parameters
        ----------
        project_id : str
            ID of project for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListProjectCollaborationsRequestRole]
            Organization or team membership role for which to retrieve collaborations.

        ids : typing.Optional[str]
            Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        page_size : typing.Optional[int]
            Number of collaborations to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListProjectCollaborationsRequestSort]
            Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollaborationsPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.projects.list_project_collaborations(
            project_id="src_1234",
            user_id="ent_1234",
            app_id="app_1234",
            team_id="team_1234",
            organization_id="ent_1234",
            ids="clb_1234",
        )
        """
        _response = self._raw_client.list_project_collaborations(
            project_id,
            user_id=user_id,
            app_id=app_id,
            team_id=team_id,
            organization_id=organization_id,
            role=role,
            ids=ids,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

    async def list_project_collaborations(
        self,
        project_id: str,
        *,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListProjectCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListProjectCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified project. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Projects).

        Parameters
        ----------
        project_id : str
            ID of project for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListProjectCollaborationsRequestRole]
            Organization or team membership role for which to retrieve collaborations.

        ids : typing.Optional[str]
            Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        page_size : typing.Optional[int]
            Number of collaborations to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListProjectCollaborationsRequestSort]
            Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollaborationsPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.projects.list_project_collaborations(
                project_id="src_1234",
                user_id="ent_1234",
                app_id="app_1234",
                team_id="team_1234",
                organization_id="ent_1234",
                ids="clb_1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_collaborations(
            project_id,
            user_id=user_id,
            app_id=app_id,
            team_id=team_id,
            organization_id=organization_id,
            role=role,
            ids=ids,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            request_options=request_options,
        )
        return _response.data
