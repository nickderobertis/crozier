

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1project import V1Project
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.list_projects_request_filter import ListProjectsRequestFilter
from .types.list_projects_request_relation import ListProjectsRequestRelation
from .types.list_projects_request_state import ListProjectsRequestState
from .types.v1projects_create_project import V1ProjectsCreateProject
from .types.v1projects_update_project import V1ProjectsUpdateProject


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
        account_id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListProjectsRequestFilter] = None,
        state: typing.Optional[ListProjectsRequestState] = None,
        relation: typing.Optional[ListProjectsRequestRelation] = None,
        updated_after: typing.Optional[str] = None,
        project_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        external_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Project]:
        """
        List all projects in the Timely account. The projects will be returned in a paginated format.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        offset : typing.Optional[int]
            Retrieve projects from offset

        limit : typing.Optional[int]
            Retrieve number of projects

        order : typing.Optional[str]
            Sorting order - desc, asc (Default desc)

        filter : typing.Optional[ListProjectsRequestFilter]
            Deprecated: Filter projects - mine, active, archived, all (Default mine, ignored if state or relation parameter present)

        state : typing.Optional[ListProjectsRequestState]
            Filter projects - active, archived, all

        relation : typing.Optional[ListProjectsRequestRelation]
            Filter projects - assigned, created, all

        updated_after : typing.Optional[str]
            Retrieve records updated after a certain timestamp

        project_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects

        external_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects by external ID reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Project]
            Project Details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.list_projects(
            account_id=1,
        )
        """
        _response = self._raw_client.list_projects(
            account_id,
            offset=offset,
            limit=limit,
            order=order,
            filter=filter,
            state=state,
            relation=relation,
            updated_after=updated_after,
            project_ids=project_ids,
            external_ids=external_ids,
            request_options=request_options,
        )
        return _response.data

    def create_project(
        self,
        account_id: int,
        *,
        project: V1ProjectsCreateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Project:
        """
        Create a new project in the Timely account. The project will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Workspace id

        project : V1ProjectsCreateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            project created

        Examples
        --------
        from fern.projects import (
            V1ProjectsCreateProject,
            V1ProjectsCreateProjectRateType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.create_project(
            account_id=1,
            project=V1ProjectsCreateProject(
                name="New Sideproject 2",
                color="d0915a",
                new_company="Timely Solo",
                hour_rate=20.0,
                rate_type=V1ProjectsCreateProjectRateType.PROJECT,
                label_ids=[1, 2],
                required_label_ids=[1],
            ),
        )
        """
        _response = self._raw_client.create_project(account_id, project=project, request_options=request_options)
        return _response.data

    def show_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Project:
        """
        Retrieve details for a specific project.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            Project details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.show_project(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.show_project(account_id, id, request_options=request_options)
        return _response.data

    def update_project(
        self,
        account_id: int,
        id: int,
        *,
        project: V1ProjectsUpdateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Project:
        """
        Update an existing project. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        project : V1ProjectsUpdateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            Project updated

        Examples
        --------
        from fern.projects import V1ProjectsUpdateProject

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.update_project(
            account_id=1,
            id=1,
            project=V1ProjectsUpdateProject(
                name="Updated Project Name",
                color="ff5733",
                description="Updated description",
            ),
        )
        """
        _response = self._raw_client.update_project(account_id, id, project=project, request_options=request_options)
        return _response.data

    def delete_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a project. This will permanently remove the project from the account.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Project deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.delete_project(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_project(account_id, id, request_options=request_options)
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
        account_id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListProjectsRequestFilter] = None,
        state: typing.Optional[ListProjectsRequestState] = None,
        relation: typing.Optional[ListProjectsRequestRelation] = None,
        updated_after: typing.Optional[str] = None,
        project_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        external_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Project]:
        """
        List all projects in the Timely account. The projects will be returned in a paginated format.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        offset : typing.Optional[int]
            Retrieve projects from offset

        limit : typing.Optional[int]
            Retrieve number of projects

        order : typing.Optional[str]
            Sorting order - desc, asc (Default desc)

        filter : typing.Optional[ListProjectsRequestFilter]
            Deprecated: Filter projects - mine, active, archived, all (Default mine, ignored if state or relation parameter present)

        state : typing.Optional[ListProjectsRequestState]
            Filter projects - active, archived, all

        relation : typing.Optional[ListProjectsRequestRelation]
            Filter projects - assigned, created, all

        updated_after : typing.Optional[str]
            Retrieve records updated after a certain timestamp

        project_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects

        external_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects by external ID reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Project]
            Project Details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.list_projects(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_projects(
            account_id,
            offset=offset,
            limit=limit,
            order=order,
            filter=filter,
            state=state,
            relation=relation,
            updated_after=updated_after,
            project_ids=project_ids,
            external_ids=external_ids,
            request_options=request_options,
        )
        return _response.data

    async def create_project(
        self,
        account_id: int,
        *,
        project: V1ProjectsCreateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Project:
        """
        Create a new project in the Timely account. The project will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Workspace id

        project : V1ProjectsCreateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            project created

        Examples
        --------
        import asyncio

        from fern.projects import (
            V1ProjectsCreateProject,
            V1ProjectsCreateProjectRateType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.create_project(
                account_id=1,
                project=V1ProjectsCreateProject(
                    name="New Sideproject 2",
                    color="d0915a",
                    new_company="Timely Solo",
                    hour_rate=20.0,
                    rate_type=V1ProjectsCreateProjectRateType.PROJECT,
                    label_ids=[1, 2],
                    required_label_ids=[1],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project(account_id, project=project, request_options=request_options)
        return _response.data

    async def show_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Project:
        """
        Retrieve details for a specific project.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            Project details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.show_project(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_project(account_id, id, request_options=request_options)
        return _response.data

    async def update_project(
        self,
        account_id: int,
        id: int,
        *,
        project: V1ProjectsUpdateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Project:
        """
        Update an existing project. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        project : V1ProjectsUpdateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Project
            Project updated

        Examples
        --------
        import asyncio

        from fern.projects import V1ProjectsUpdateProject

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.update_project(
                account_id=1,
                id=1,
                project=V1ProjectsUpdateProject(
                    name="Updated Project Name",
                    color="ff5733",
                    description="Updated description",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project(
            account_id, id, project=project, request_options=request_options
        )
        return _response.data

    async def delete_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a project. This will permanently remove the project from the account.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project(account_id, id, request_options=request_options)
        return _response.data
