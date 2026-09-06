

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.project_tag import ProjectTag
from ..types.project_tag_id_param import ProjectTagIdParam
from ..types.project_tag_name import ProjectTagName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawProjectTagsClient, RawProjectTagsClient
from .types.get_project_tag_response import GetProjectTagResponse


OMIT = typing.cast(typing.Any, ...)


class ProjectTagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectTagsClient
        """
        return self._raw_client

    def get_project_tag(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_tag_name: typing.Optional[ProjectTagName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectTagResponse:
        """
        List out all project_tags. The project_tags are sorted by creation date, with the most recently-created project_tags coming first

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

        project_tag_name : typing.Optional[ProjectTagName]
            Name of the project_tag to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectTagResponse
            Returns a list of project_tag objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.get_project_tag()
        """
        _response = self._raw_client.get_project_tag(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_tag_name=project_tag_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the new project_tag object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.post_project_tag(
            project_id="project_id",
            name="name",
        )
        """
        _response = self._raw_client.post_project_tag(
            project_id=project_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data

    def put_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Create or replace project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will replace the existing project_tag with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the new project_tag object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.put_project_tag(
            project_id="project_id",
            name="name",
        )
        """
        _response = self._raw_client.put_project_tag(
            project_id=project_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data

    def get_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectTag:
        """
        Get a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the project_tag object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.get_project_tag_id(
            project_tag_id="project_tag_id",
        )
        """
        _response = self._raw_client.get_project_tag_id(project_tag_id, request_options=request_options)
        return _response.data

    def delete_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectTag:
        """
        Delete a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the deleted project_tag object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.delete_project_tag_id(
            project_tag_id="project_tag_id",
        )
        """
        _response = self._raw_client.delete_project_tag_id(project_tag_id, request_options=request_options)
        return _response.data

    def patch_project_tag_id(
        self,
        project_tag_id: ProjectTagIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Partially update a project_tag object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        name : typing.Optional[str]
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the project_tag object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_tags.patch_project_tag_id(
            project_tag_id="project_tag_id",
        )
        """
        _response = self._raw_client.patch_project_tag_id(
            project_tag_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data


class AsyncProjectTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectTagsClient
        """
        return self._raw_client

    async def get_project_tag(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_tag_name: typing.Optional[ProjectTagName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectTagResponse:
        """
        List out all project_tags. The project_tags are sorted by creation date, with the most recently-created project_tags coming first

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

        project_tag_name : typing.Optional[ProjectTagName]
            Name of the project_tag to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectTagResponse
            Returns a list of project_tag objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.get_project_tag()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_tag(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_tag_name=project_tag_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the new project_tag object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.post_project_tag(
                project_id="project_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_tag(
            project_id=project_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data

    async def put_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Create or replace project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will replace the existing project_tag with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the new project_tag object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.put_project_tag(
                project_id="project_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_project_tag(
            project_id=project_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data

    async def get_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectTag:
        """
        Get a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the project_tag object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.get_project_tag_id(
                project_tag_id="project_tag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_tag_id(project_tag_id, request_options=request_options)
        return _response.data

    async def delete_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectTag:
        """
        Delete a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the deleted project_tag object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.delete_project_tag_id(
                project_tag_id="project_tag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_tag_id(project_tag_id, request_options=request_options)
        return _response.data

    async def patch_project_tag_id(
        self,
        project_tag_id: ProjectTagIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectTag:
        """
        Partially update a project_tag object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        name : typing.Optional[str]
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectTag
            Returns the project_tag object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_tags.patch_project_tag_id(
                project_tag_id="project_tag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project_tag_id(
            project_tag_id, name=name, description=description, color=color, request_options=request_options
        )
        return _response.data
