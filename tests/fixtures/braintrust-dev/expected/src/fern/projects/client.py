

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project import Project
from ..types.project_id_param import ProjectIdParam
from ..types.project_name import ProjectName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.get_project_response import GetProjectResponse
from .types.patch_project_settings import PatchProjectSettings


OMIT = typing.cast(typing.Any, ...)


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

    def get_project(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_name: typing.Optional[ProjectName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectResponse:
        """
        List out all projects. The projects are sorted by creation date, with the most recently-created projects coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectResponse
            Returns a list of project objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.get_project()
        """
        _response = self._raw_client.get_project(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_name=project_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_project(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Create a new project. If there is an existing project with the same name as the one specified in the request, will return the existing project unmodified

        Parameters
        ----------
        name : str
            Name of the project

        description : typing.Optional[str]
            Textual description of the project

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the project belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the new project object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.post_project(
            name="name",
        )
        """
        _response = self._raw_client.post_project(
            name=name, description=description, org_name=org_name, request_options=request_options
        )
        return _response.data

    def get_project_id(
        self, project_id: ProjectIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a project object by its id

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the project object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.get_project_id(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_id(project_id, request_options=request_options)
        return _response.data

    def delete_project_id(
        self, project_id: ProjectIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Delete a project object by its id

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the deleted project object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.delete_project_id(
            project_id="project_id",
        )
        """
        _response = self._raw_client.delete_project_id(project_id, request_options=request_options)
        return _response.data

    def patch_project_id(
        self,
        project_id: ProjectIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[PatchProjectSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Partially update a project object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        name : typing.Optional[str]
            Name of the project

        description : typing.Optional[str]

        user_id : typing.Optional[str]

        settings : typing.Optional[PatchProjectSettings]
            Project settings. Patch operations replace all settings, so make sure you include all settings you want to keep.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the project object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.patch_project_id(
            project_id="project_id",
        )
        """
        _response = self._raw_client.patch_project_id(
            project_id,
            name=name,
            description=description,
            user_id=user_id,
            settings=settings,
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

    async def get_project(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_name: typing.Optional[ProjectName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectResponse:
        """
        List out all projects. The projects are sorted by creation date, with the most recently-created projects coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectResponse
            Returns a list of project objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.get_project()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_name=project_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_project(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Create a new project. If there is an existing project with the same name as the one specified in the request, will return the existing project unmodified

        Parameters
        ----------
        name : str
            Name of the project

        description : typing.Optional[str]
            Textual description of the project

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the project belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the new project object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.post_project(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project(
            name=name, description=description, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def get_project_id(
        self, project_id: ProjectIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a project object by its id

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the project object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.get_project_id(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_id(project_id, request_options=request_options)
        return _response.data

    async def delete_project_id(
        self, project_id: ProjectIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Delete a project object by its id

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the deleted project object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.delete_project_id(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_id(project_id, request_options=request_options)
        return _response.data

    async def patch_project_id(
        self,
        project_id: ProjectIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[PatchProjectSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Partially update a project object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        name : typing.Optional[str]
            Name of the project

        description : typing.Optional[str]

        user_id : typing.Optional[str]

        settings : typing.Optional[PatchProjectSettings]
            Project settings. Patch operations replace all settings, so make sure you include all settings you want to keep.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Returns the project object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.patch_project_id(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project_id(
            project_id,
            name=name,
            description=description,
            user_id=user_id,
            settings=settings,
            request_options=request_options,
        )
        return _response.data
