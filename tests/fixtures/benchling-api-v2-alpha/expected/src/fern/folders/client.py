

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collaborations_paginated_list import CollaborationsPaginatedList
from .raw_client import AsyncRawFoldersClient, RawFoldersClient
from .types.list_folder_collaborations_request_role import ListFolderCollaborationsRequestRole
from .types.list_folder_collaborations_request_sort import ListFolderCollaborationsRequestSort


class FoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFoldersClient
        """
        return self._raw_client

    def list_folder_collaborations(
        self,
        folder_id: str,
        *,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListFolderCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListFolderCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified Folders. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Folders).

        Parameters
        ----------
        folder_id : str
            ID of folder for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListFolderCollaborationsRequestRole]
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

        sort : typing.Optional[ListFolderCollaborationsRequestSort]
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
        client.folders.list_folder_collaborations(
            folder_id="lib_1234",
            user_id="ent_1234",
            app_id="app_1234",
            team_id="team_1234",
            organization_id="ent_1234",
            ids="clb_1234",
        )
        """
        _response = self._raw_client.list_folder_collaborations(
            folder_id,
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


class AsyncFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFoldersClient
        """
        return self._raw_client

    async def list_folder_collaborations(
        self,
        folder_id: str,
        *,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListFolderCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListFolderCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollaborationsPaginatedList:
        """
        Returns information about collaborations on the specified Folders. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Folders).

        Parameters
        ----------
        folder_id : str
            ID of folder for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListFolderCollaborationsRequestRole]
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

        sort : typing.Optional[ListFolderCollaborationsRequestSort]
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
            await client.folders.list_folder_collaborations(
                folder_id="lib_1234",
                user_id="ent_1234",
                app_id="app_1234",
                team_id="team_1234",
                organization_id="ent_1234",
                ids="clb_1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folder_collaborations(
            folder_id,
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
