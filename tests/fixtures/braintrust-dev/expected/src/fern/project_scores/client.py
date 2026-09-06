

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.get_project_score_request_score_type import GetProjectScoreRequestScoreType
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.project_score import ProjectScore
from ..types.project_score_categories import ProjectScoreCategories
from ..types.project_score_config import ProjectScoreConfig
from ..types.project_score_id_param import ProjectScoreIdParam
from ..types.project_score_name import ProjectScoreName
from ..types.project_score_type import ProjectScoreType
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawProjectScoresClient, RawProjectScoresClient
from .types.get_project_score_response import GetProjectScoreResponse


OMIT = typing.cast(typing.Any, ...)


class ProjectScoresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectScoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectScoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectScoresClient
        """
        return self._raw_client

    def get_project_score(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_score_name: typing.Optional[ProjectScoreName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        score_type: typing.Optional[GetProjectScoreRequestScoreType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectScoreResponse:
        """
        List out all project_scores. The project_scores are sorted by creation date, with the most recently-created project_scores coming first

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

        project_score_name : typing.Optional[ProjectScoreName]
            Name of the project_score to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        score_type : typing.Optional[GetProjectScoreRequestScoreType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectScoreResponse
            Returns a list of project_score objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.get_project_score()
        """
        _response = self._raw_client.get_project_score(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_score_name=project_score_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            score_type=score_type,
            request_options=request_options,
        )
        return _response.data

    def post_project_score(
        self,
        *,
        project_id: str,
        name: str,
        score_type: ProjectScoreType,
        description: typing.Optional[str] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Create a new project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will return the existing project_score unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project score belongs under

        name : str
            Name of the project score

        score_type : ProjectScoreType

        description : typing.Optional[str]
            Textual description of the project score

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the new project_score object

        Examples
        --------
        from fern import FernApi, ProjectScoreType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.post_project_score(
            project_id="project_id",
            name="name",
            score_type=ProjectScoreType.SLIDER,
        )
        """
        _response = self._raw_client.post_project_score(
            project_id=project_id,
            name=name,
            score_type=score_type,
            description=description,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def put_project_score(
        self,
        *,
        project_id: str,
        name: str,
        score_type: ProjectScoreType,
        description: typing.Optional[str] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Create or replace project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will replace the existing project_score with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project score belongs under

        name : str
            Name of the project score

        score_type : ProjectScoreType

        description : typing.Optional[str]
            Textual description of the project score

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the new project_score object

        Examples
        --------
        from fern import FernApi, ProjectScoreType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.put_project_score(
            project_id="project_id",
            name="name",
            score_type=ProjectScoreType.SLIDER,
        )
        """
        _response = self._raw_client.put_project_score(
            project_id=project_id,
            name=name,
            score_type=score_type,
            description=description,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def get_project_score_id(
        self, project_score_id: ProjectScoreIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectScore:
        """
        Get a project_score object by its id

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the project_score object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.get_project_score_id(
            project_score_id="project_score_id",
        )
        """
        _response = self._raw_client.get_project_score_id(project_score_id, request_options=request_options)
        return _response.data

    def delete_project_score_id(
        self, project_score_id: ProjectScoreIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectScore:
        """
        Delete a project_score object by its id

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the deleted project_score object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.delete_project_score_id(
            project_score_id="project_score_id",
        )
        """
        _response = self._raw_client.delete_project_score_id(project_score_id, request_options=request_options)
        return _response.data

    def patch_project_score_id(
        self,
        project_score_id: ProjectScoreIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        score_type: typing.Optional[ProjectScoreType] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Partially update a project_score object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        name : typing.Optional[str]
            Name of the project score

        description : typing.Optional[str]
            Textual description of the project score

        score_type : typing.Optional[ProjectScoreType]

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the project_score object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project_scores.patch_project_score_id(
            project_score_id="project_score_id",
        )
        """
        _response = self._raw_client.patch_project_score_id(
            project_score_id,
            name=name,
            description=description,
            score_type=score_type,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectScoresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectScoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectScoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectScoresClient
        """
        return self._raw_client

    async def get_project_score(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_score_name: typing.Optional[ProjectScoreName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        score_type: typing.Optional[GetProjectScoreRequestScoreType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectScoreResponse:
        """
        List out all project_scores. The project_scores are sorted by creation date, with the most recently-created project_scores coming first

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

        project_score_name : typing.Optional[ProjectScoreName]
            Name of the project_score to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        score_type : typing.Optional[GetProjectScoreRequestScoreType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectScoreResponse
            Returns a list of project_score objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.get_project_score()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_score(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            project_score_name=project_score_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            score_type=score_type,
            request_options=request_options,
        )
        return _response.data

    async def post_project_score(
        self,
        *,
        project_id: str,
        name: str,
        score_type: ProjectScoreType,
        description: typing.Optional[str] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Create a new project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will return the existing project_score unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project score belongs under

        name : str
            Name of the project score

        score_type : ProjectScoreType

        description : typing.Optional[str]
            Textual description of the project score

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the new project_score object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProjectScoreType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.post_project_score(
                project_id="project_id",
                name="name",
                score_type=ProjectScoreType.SLIDER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_score(
            project_id=project_id,
            name=name,
            score_type=score_type,
            description=description,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def put_project_score(
        self,
        *,
        project_id: str,
        name: str,
        score_type: ProjectScoreType,
        description: typing.Optional[str] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Create or replace project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will replace the existing project_score with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project score belongs under

        name : str
            Name of the project score

        score_type : ProjectScoreType

        description : typing.Optional[str]
            Textual description of the project score

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the new project_score object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProjectScoreType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.put_project_score(
                project_id="project_id",
                name="name",
                score_type=ProjectScoreType.SLIDER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_project_score(
            project_id=project_id,
            name=name,
            score_type=score_type,
            description=description,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def get_project_score_id(
        self, project_score_id: ProjectScoreIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectScore:
        """
        Get a project_score object by its id

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the project_score object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.get_project_score_id(
                project_score_id="project_score_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_score_id(project_score_id, request_options=request_options)
        return _response.data

    async def delete_project_score_id(
        self, project_score_id: ProjectScoreIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectScore:
        """
        Delete a project_score object by its id

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the deleted project_score object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.delete_project_score_id(
                project_score_id="project_score_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_score_id(project_score_id, request_options=request_options)
        return _response.data

    async def patch_project_score_id(
        self,
        project_score_id: ProjectScoreIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        score_type: typing.Optional[ProjectScoreType] = OMIT,
        categories: typing.Optional[ProjectScoreCategories] = OMIT,
        config: typing.Optional[ProjectScoreConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectScore:
        """
        Partially update a project_score object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_score_id : ProjectScoreIdParam
            ProjectScore id

        name : typing.Optional[str]
            Name of the project score

        description : typing.Optional[str]
            Textual description of the project score

        score_type : typing.Optional[ProjectScoreType]

        categories : typing.Optional[ProjectScoreCategories]

        config : typing.Optional[ProjectScoreConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectScore
            Returns the project_score object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project_scores.patch_project_score_id(
                project_score_id="project_score_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_project_score_id(
            project_score_id,
            name=name,
            description=description,
            score_type=score_type,
            categories=categories,
            config=config,
            request_options=request_options,
        )
        return _response.data
