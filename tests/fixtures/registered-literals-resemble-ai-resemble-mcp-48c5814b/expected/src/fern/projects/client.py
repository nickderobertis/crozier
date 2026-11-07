

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.create_project_response import CreateProjectResponse
from .types.delete_project_response import DeleteProjectResponse
from .types.get_project_response import GetProjectResponse
from .types.list_projects_response import ListProjectsResponse
from .types.update_project_response import UpdateProjectResponse


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

    def list_projects(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProjectsResponse:
        """
        List all projects

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectsResponse
            List of projects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.list_projects(
            page=1,
        )
        """
        _response = self._raw_client.list_projects(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def create_project(
        self,
        *,
        name: str,
        description: str,
        is_collaborative: bool,
        is_archived: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Create a new project

        Parameters
        ----------
        name : str

        description : str

        is_collaborative : bool

        is_archived : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Project created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.create_project(
            name="name",
            description="description",
            is_collaborative=True,
            is_archived=True,
        )
        """
        _response = self._raw_client.create_project(
            name=name,
            description=description,
            is_collaborative=is_collaborative,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    def get_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectResponse:
        """
        Get project details

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectResponse
            Project details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.get_project(
            project_uuid="project_uuid",
        )
        """
        _response = self._raw_client.get_project(project_uuid, request_options=request_options)
        return _response.data

    def update_project(
        self,
        project_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_collaborative: typing.Optional[bool] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProjectResponse:
        """
        Update a project

        Parameters
        ----------
        project_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        is_collaborative : typing.Optional[bool]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProjectResponse
            Project updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.update_project(
            project_uuid="project_uuid",
        )
        """
        _response = self._raw_client.update_project(
            project_uuid,
            name=name,
            description=description,
            is_collaborative=is_collaborative,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    def delete_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProjectResponse:
        """
        Delete a project

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProjectResponse
            Project deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.delete_project(
            project_uuid="project_uuid",
        )
        """
        _response = self._raw_client.delete_project(project_uuid, request_options=request_options)
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

    async def list_projects(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProjectsResponse:
        """
        List all projects

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectsResponse
            List of projects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.list_projects(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_projects(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_project(
        self,
        *,
        name: str,
        description: str,
        is_collaborative: bool,
        is_archived: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Create a new project

        Parameters
        ----------
        name : str

        description : str

        is_collaborative : bool

        is_archived : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Project created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.create_project(
                name="name",
                description="description",
                is_collaborative=True,
                is_archived=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project(
            name=name,
            description=description,
            is_collaborative=is_collaborative,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    async def get_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectResponse:
        """
        Get project details

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectResponse
            Project details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.get_project(
                project_uuid="project_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project(project_uuid, request_options=request_options)
        return _response.data

    async def update_project(
        self,
        project_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_collaborative: typing.Optional[bool] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProjectResponse:
        """
        Update a project

        Parameters
        ----------
        project_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        is_collaborative : typing.Optional[bool]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProjectResponse
            Project updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.update_project(
                project_uuid="project_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project(
            project_uuid,
            name=name,
            description=description,
            is_collaborative=is_collaborative,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    async def delete_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProjectResponse:
        """
        Delete a project

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProjectResponse
            Project deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.delete_project(
                project_uuid="project_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project(project_uuid, request_options=request_options)
        return _response.data
