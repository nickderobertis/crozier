

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.function_type_enum_nullish import FunctionTypeEnumNullish
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.prompt import Prompt
from ..types.prompt_data_nullish import PromptDataNullish
from ..types.prompt_environment import PromptEnvironment
from ..types.prompt_id_param import PromptIdParam
from ..types.prompt_name import PromptName
from ..types.prompt_version import PromptVersion
from ..types.slug import Slug
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawPromptsClient, RawPromptsClient
from .types.get_prompt_response import GetPromptResponse


OMIT = typing.cast(typing.Any, ...)


class PromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPromptsClient
        """
        return self._raw_client

    def get_prompt(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        prompt_name: typing.Optional[PromptName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPromptResponse:
        """
        List out all prompts. The prompts are sorted by creation date, with the most recently-created prompts coming first

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

        prompt_name : typing.Optional[PromptName]
            Name of the prompt to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        slug : typing.Optional[Slug]
            Retrieve prompt with a specific slug

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptResponse
            Returns a list of prompt objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.get_prompt()
        """
        _response = self._raw_client.get_prompt(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            prompt_name=prompt_name,
            project_name=project_name,
            project_id=project_id,
            slug=slug,
            version=version,
            environment=environment,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Create a new prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will return the existing prompt unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the new prompt object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.post_prompt(
            project_id="project_id",
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.post_prompt(
            project_id=project_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            request_options=request_options,
        )
        return _response.data

    def put_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Create or replace prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will replace the existing prompt with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the new prompt object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.put_prompt(
            project_id="project_id",
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.put_prompt(
            project_id=project_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            request_options=request_options,
        )
        return _response.data

    def get_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the prompt object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.get_prompt_id(
            prompt_id="prompt_id",
        )
        """
        _response = self._raw_client.get_prompt_id(
            prompt_id, version=version, environment=environment, request_options=request_options
        )
        return _response.data

    def delete_prompt_id(
        self, prompt_id: PromptIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Prompt:
        """
        Delete a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the deleted prompt object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.delete_prompt_id(
            prompt_id="prompt_id",
        )
        """
        _response = self._raw_client.delete_prompt_id(prompt_id, request_options=request_options)
        return _response.data

    def patch_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Partially update a prompt object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        name : typing.Optional[str]
            Name of the prompt

        slug : typing.Optional[str]
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the prompt object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prompts.patch_prompt_id(
            prompt_id="prompt_id",
        )
        """
        _response = self._raw_client.patch_prompt_id(
            prompt_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            request_options=request_options,
        )
        return _response.data


class AsyncPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPromptsClient
        """
        return self._raw_client

    async def get_prompt(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        prompt_name: typing.Optional[PromptName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPromptResponse:
        """
        List out all prompts. The prompts are sorted by creation date, with the most recently-created prompts coming first

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

        prompt_name : typing.Optional[PromptName]
            Name of the prompt to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        slug : typing.Optional[Slug]
            Retrieve prompt with a specific slug

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptResponse
            Returns a list of prompt objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.get_prompt()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prompt(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            prompt_name=prompt_name,
            project_name=project_name,
            project_id=project_id,
            slug=slug,
            version=version,
            environment=environment,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Create a new prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will return the existing prompt unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the new prompt object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.post_prompt(
                project_id="project_id",
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_prompt(
            project_id=project_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            request_options=request_options,
        )
        return _response.data

    async def put_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Create or replace prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will replace the existing prompt with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the new prompt object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.put_prompt(
                project_id="project_id",
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_prompt(
            project_id=project_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            request_options=request_options,
        )
        return _response.data

    async def get_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the prompt object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.get_prompt_id(
                prompt_id="prompt_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prompt_id(
            prompt_id, version=version, environment=environment, request_options=request_options
        )
        return _response.data

    async def delete_prompt_id(
        self, prompt_id: PromptIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Prompt:
        """
        Delete a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the deleted prompt object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.delete_prompt_id(
                prompt_id="prompt_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_prompt_id(prompt_id, request_options=request_options)
        return _response.data

    async def patch_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Partially update a prompt object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        name : typing.Optional[str]
            Name of the prompt

        slug : typing.Optional[str]
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Returns the prompt object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prompts.patch_prompt_id(
                prompt_id="prompt_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_prompt_id(
            prompt_id,
            name=name,
            slug=slug,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            request_options=request_options,
        )
        return _response.data
