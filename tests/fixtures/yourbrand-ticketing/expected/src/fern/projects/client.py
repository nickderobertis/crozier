

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.items_result_of_project import ItemsResultOfProject
from ..types.items_result_of_project_membership import ItemsResultOfProjectMembership
from ..types.project import Project
from ..types.project_membership import ProjectMembership
from ..types.sort_direction import SortDirection
from .raw_client import AsyncRawProjectsClient, RawProjectsClient


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

    def getprojects(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProject:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        user_id : typing.Optional[str]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProject


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.getprojects()
        """
        _response = self._raw_client.getprojects(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            user_id=user_id,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createproject(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.createproject()
        """
        _response = self._raw_client.createproject(
            organization_id=organization_id,
            name=name,
            description=description,
            create_project_organization_id=create_project_organization_id,
            request_options=request_options,
        )
        return _response.data

    def getproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.getproject(
            id=1,
        )
        """
        _response = self._raw_client.getproject(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        update_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        update_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.updateproject(
            id=1,
        )
        """
        _response = self._raw_client.updateproject(
            id,
            organization_id=organization_id,
            name=name,
            description=description,
            update_project_organization_id=update_project_organization_id,
            request_options=request_options,
        )
        return _response.data

    def deleteproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.deleteproject(
            id=1,
        )
        """
        _response = self._raw_client.deleteproject(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def getprojectmemberships(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProjectMembership:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProjectMembership


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.getprojectmemberships(
            id=1,
        )
        """
        _response = self._raw_client.getprojectmemberships(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createprojectmembership(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.createprojectmembership(
            id=1,
        )
        """
        _response = self._raw_client.createprojectmembership(
            id,
            organization_id=organization_id,
            user_id=user_id,
            from_=from_,
            thru=thru,
            request_options=request_options,
        )
        return _response.data

    def getprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.getprojectmembership(
            id=1,
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.getprojectmembership(
            id, membership_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.updateprojectmembership(
            id=1,
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.updateprojectmembership(
            id, membership_id, organization_id=organization_id, from_=from_, thru=thru, request_options=request_options
        )
        return _response.data

    def deleteprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projects.deleteprojectmembership(
            id=1,
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.deleteprojectmembership(
            id, membership_id, organization_id=organization_id, request_options=request_options
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

    async def getprojects(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProject:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        user_id : typing.Optional[str]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProject


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.getprojects()


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojects(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            user_id=user_id,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createproject(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.createproject()


        asyncio.run(main())
        """
        _response = await self._raw_client.createproject(
            organization_id=organization_id,
            name=name,
            description=description,
            create_project_organization_id=create_project_organization_id,
            request_options=request_options,
        )
        return _response.data

    async def getproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.getproject(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getproject(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        update_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        update_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.updateproject(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateproject(
            id,
            organization_id=organization_id,
            name=name,
            description=description,
            update_project_organization_id=update_project_organization_id,
            request_options=request_options,
        )
        return _response.data

    async def deleteproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.deleteproject(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteproject(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def getprojectmemberships(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProjectMembership:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProjectMembership


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.getprojectmemberships(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectmemberships(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createprojectmembership(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.createprojectmembership(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createprojectmembership(
            id,
            organization_id=organization_id,
            user_id=user_id,
            from_=from_,
            thru=thru,
            request_options=request_options,
        )
        return _response.data

    async def getprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.getprojectmembership(
                id=1,
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectmembership(
            id, membership_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectMembership:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMembership


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.updateprojectmembership(
                id=1,
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateprojectmembership(
            id, membership_id, organization_id=organization_id, from_=from_, thru=thru, request_options=request_options
        )
        return _response.data

    async def deleteprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projects.deleteprojectmembership(
                id=1,
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteprojectmembership(
            id, membership_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data
