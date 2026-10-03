

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.items_result_of_project_group import ItemsResultOfProjectGroup
from ..types.project_group import ProjectGroup
from ..types.sort_direction import SortDirection
from .raw_client import AsyncRawProjectgroupsClient, RawProjectgroupsClient


OMIT = typing.cast(typing.Any, ...)


class ProjectgroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectgroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectgroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectgroupsClient
        """
        return self._raw_client

    def getprojectgroups(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        project_id: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProjectGroup:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        project_id : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProjectGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projectgroups.getprojectgroups()
        """
        _response = self._raw_client.getprojectgroups(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            project_id=project_id,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createprojectgroup(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projectgroups.createprojectgroup()
        """
        _response = self._raw_client.createprojectgroup(
            organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def getprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projectgroups.getprojectgroup(
            id="id",
        )
        """
        _response = self._raw_client.getprojectgroup(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.projectgroups.updateprojectgroup(
            id="id",
        )
        """
        _response = self._raw_client.updateprojectgroup(
            id, organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def deleteprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.projectgroups.deleteprojectgroup(
            id="id",
        )
        """
        _response = self._raw_client.deleteprojectgroup(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data


class AsyncProjectgroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectgroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectgroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectgroupsClient
        """
        return self._raw_client

    async def getprojectgroups(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        project_id: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemsResultOfProjectGroup:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        project_id : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemsResultOfProjectGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projectgroups.getprojectgroups()


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectgroups(
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            project_id=project_id,
            search_string=search_string,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createprojectgroup(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projectgroups.createprojectgroup()


        asyncio.run(main())
        """
        _response = await self._raw_client.createprojectgroup(
            organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def getprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projectgroups.getprojectgroup(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectgroup(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectGroup:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.projectgroups.updateprojectgroup(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateprojectgroup(
            id, organization_id=organization_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def deleteprojectgroup(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.projectgroups.deleteprojectgroup(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteprojectgroup(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data
