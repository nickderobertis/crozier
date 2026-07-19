

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.projects_list_projects_request_offset import ProjectsListProjectsRequestOffset
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.projects_create_project_response import ProjectsCreateProjectResponse
from .types.projects_delete_project_response import ProjectsDeleteProjectResponse
from .types.projects_list_projects_response import ProjectsListProjectsResponse


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

    def listprojects(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[ProjectsListProjectsRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectsListProjectsResponse:
        """
        List all projects

        Parameters
        ----------
        name : typing.Optional[str]

        offset : typing.Optional[ProjectsListProjectsRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsListProjectsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.listprojects()
        """
        _response = self._raw_client.listprojects(
            name=name, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def createproject(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectsCreateProjectResponse:
        """
        Create a new project

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsCreateProjectResponse
            201

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.createproject(
            name="name",
        )
        """
        _response = self._raw_client.createproject(name=name, request_options=request_options)
        return _response.data

    def deleteproject(
        self,
        project_id: str,
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectsDeleteProjectResponse:
        """
        Delete a project by ID

        Parameters
        ----------
        project_id : str

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsDeleteProjectResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.deleteproject(
            project_id="projectId",
        )
        """
        _response = self._raw_client.deleteproject(project_id, request=request, request_options=request_options)
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

    async def listprojects(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[ProjectsListProjectsRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectsListProjectsResponse:
        """
        List all projects

        Parameters
        ----------
        name : typing.Optional[str]

        offset : typing.Optional[ProjectsListProjectsRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsListProjectsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.listprojects()


        asyncio.run(main())
        """
        _response = await self._raw_client.listprojects(
            name=name, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def createproject(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectsCreateProjectResponse:
        """
        Create a new project

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsCreateProjectResponse
            201

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.createproject(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createproject(name=name, request_options=request_options)
        return _response.data

    async def deleteproject(
        self,
        project_id: str,
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectsDeleteProjectResponse:
        """
        Delete a project by ID

        Parameters
        ----------
        project_id : str

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectsDeleteProjectResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.deleteproject(
                project_id="projectId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteproject(project_id, request=request, request_options=request_options)
        return _response.data
