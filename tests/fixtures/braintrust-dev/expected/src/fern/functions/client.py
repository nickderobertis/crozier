

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.chat_completion_message_param import ChatCompletionMessageParam
from ..types.create_function_function_schema import CreateFunctionFunctionSchema
from ..types.create_function_origin import CreateFunctionOrigin
from ..types.ending_before import EndingBefore
from ..types.function import Function
from ..types.function_data import FunctionData
from ..types.function_data_nullish import FunctionDataNullish
from ..types.function_id_param import FunctionIdParam
from ..types.function_name import FunctionName
from ..types.function_type_enum_nullish import FunctionTypeEnumNullish
from ..types.ids import Ids
from ..types.invoke_parent import InvokeParent
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.prompt_data_nullish import PromptDataNullish
from ..types.prompt_environment import PromptEnvironment
from ..types.prompt_version import PromptVersion
from ..types.slug import Slug
from ..types.starting_after import StartingAfter
from ..types.streaming_mode import StreamingMode
from .raw_client import AsyncRawFunctionsClient, RawFunctionsClient
from .types.get_function_response import GetFunctionResponse
from .types.invoke_api_mcp_auth_value import InvokeApiMcpAuthValue


OMIT = typing.cast(typing.Any, ...)


class FunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFunctionsClient
        """
        return self._raw_client

    def get_function(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        function_name: typing.Optional[FunctionName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFunctionResponse:
        """
        List out all functions. The functions are sorted by creation date, with the most recently-created functions coming first

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

        function_name : typing.Optional[FunctionName]
            Name of the function to search for

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
        GetFunctionResponse
            Returns a list of function objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.get_function()
        """
        _response = self._raw_client.get_function(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            function_name=function_name,
            project_name=project_name,
            project_id=project_id,
            slug=slug,
            version=version,
            environment=environment,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create a new function. If there is an existing function in the project with the same slug as the one specified in the request, will return the existing function unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the new function object

        Examples
        --------
        from fern import FernApi, FunctionDataZero, FunctionDataZeroType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.post_function(
            project_id="project_id",
            name="name",
            slug="slug",
            function_data=FunctionDataZero(
                type=FunctionDataZeroType.PROMPT,
            ),
        )
        """
        _response = self._raw_client.post_function(
            project_id=project_id,
            name=name,
            slug=slug,
            function_data=function_data,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            origin=origin,
            function_schema=function_schema,
            request_options=request_options,
        )
        return _response.data

    def put_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the new function object

        Examples
        --------
        from fern import FernApi, FunctionDataZero, FunctionDataZeroType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.put_function(
            project_id="project_id",
            name="name",
            slug="slug",
            function_data=FunctionDataZero(
                type=FunctionDataZeroType.PROMPT,
            ),
        )
        """
        _response = self._raw_client.put_function(
            project_id=project_id,
            name=name,
            slug=slug,
            function_data=function_data,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            origin=origin,
            function_schema=function_schema,
            request_options=request_options,
        )
        return _response.data

    def get_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Get a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

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
        Function
            Returns the function object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.get_function_id(
            function_id="function_id",
        )
        """
        _response = self._raw_client.get_function_id(
            function_id, version=version, environment=environment, request_options=request_options
        )
        return _response.data

    def delete_function_id(
        self, function_id: FunctionIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Delete a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the deleted function object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.delete_function_id(
            function_id="function_id",
        )
        """
        _response = self._raw_client.delete_function_id(function_id, request_options=request_options)
        return _response.data

    def patch_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        function_data: typing.Optional[FunctionDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Partially update a function object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        name : typing.Optional[str]
            Name of the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        function_data : typing.Optional[FunctionDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the function object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.patch_function_id(
            function_id="function_id",
        )
        """
        _response = self._raw_client.patch_function_id(
            function_id,
            name=name,
            description=description,
            prompt_data=prompt_data,
            function_data=function_data,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def post_function_id_invoke(
        self,
        function_id: FunctionIdParam,
        *,
        input: typing.Optional[typing.Any] = OMIT,
        expected: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatCompletionMessageParam]] = OMIT,
        parent: typing.Optional[InvokeParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        mode: typing.Optional[StreamingMode] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]] = OMIT,
        overrides: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Invoke a function.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        input : typing.Optional[typing.Any]
            Argument to the function, which can be any JSON serializable value

        expected : typing.Optional[typing.Any]
            The expected output of the function

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Any relevant metadata. This will be logged and available as the `metadata` argument.

        tags : typing.Optional[typing.Sequence[str]]
            Any relevant tags to log on the span.

        messages : typing.Optional[typing.Sequence[ChatCompletionMessageParam]]
            If the function is an LLM, additional messages to pass along to it

        parent : typing.Optional[InvokeParent]

        stream : typing.Optional[bool]
            Whether to stream the response. If true, results will be returned in the Braintrust SSE format.

        mode : typing.Optional[StreamingMode]

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        mcp_auth : typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]]
            Map of MCP server URL to auth credentials

        overrides : typing.Optional[typing.Dict[str, typing.Any]]
            Partial function definition to merge with the function being invoked. Fields are validated against the function type's schema at runtime. For facets: { preprocessor?, prompt?, model? }. For prompts: { model?, ... }.

        version : typing.Optional[str]
            The version of the function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Function invocation response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.functions.post_function_id_invoke(
            function_id="function_id",
        )
        """
        _response = self._raw_client.post_function_id_invoke(
            function_id,
            input=input,
            expected=expected,
            metadata=metadata,
            tags=tags,
            messages=messages,
            parent=parent,
            stream=stream,
            mode=mode,
            strict=strict,
            mcp_auth=mcp_auth,
            overrides=overrides,
            version=version,
            request_options=request_options,
        )
        return _response.data


class AsyncFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFunctionsClient
        """
        return self._raw_client

    async def get_function(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        function_name: typing.Optional[FunctionName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFunctionResponse:
        """
        List out all functions. The functions are sorted by creation date, with the most recently-created functions coming first

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

        function_name : typing.Optional[FunctionName]
            Name of the function to search for

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
        GetFunctionResponse
            Returns a list of function objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.get_function()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_function(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            function_name=function_name,
            project_name=project_name,
            project_id=project_id,
            slug=slug,
            version=version,
            environment=environment,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create a new function. If there is an existing function in the project with the same slug as the one specified in the request, will return the existing function unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the new function object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FunctionDataZero, FunctionDataZeroType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.post_function(
                project_id="project_id",
                name="name",
                slug="slug",
                function_data=FunctionDataZero(
                    type=FunctionDataZeroType.PROMPT,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_function(
            project_id=project_id,
            name=name,
            slug=slug,
            function_data=function_data,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            origin=origin,
            function_schema=function_schema,
            request_options=request_options,
        )
        return _response.data

    async def put_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the new function object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FunctionDataZero, FunctionDataZeroType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.put_function(
                project_id="project_id",
                name="name",
                slug="slug",
                function_data=FunctionDataZero(
                    type=FunctionDataZeroType.PROMPT,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_function(
            project_id=project_id,
            name=name,
            slug=slug,
            function_data=function_data,
            description=description,
            prompt_data=prompt_data,
            tags=tags,
            function_type=function_type,
            origin=origin,
            function_schema=function_schema,
            request_options=request_options,
        )
        return _response.data

    async def get_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Get a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

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
        Function
            Returns the function object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.get_function_id(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_function_id(
            function_id, version=version, environment=environment, request_options=request_options
        )
        return _response.data

    async def delete_function_id(
        self, function_id: FunctionIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Delete a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the deleted function object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.delete_function_id(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_function_id(function_id, request_options=request_options)
        return _response.data

    async def patch_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        function_data: typing.Optional[FunctionDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Partially update a function object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        name : typing.Optional[str]
            Name of the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        function_data : typing.Optional[FunctionDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Returns the function object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.patch_function_id(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_function_id(
            function_id,
            name=name,
            description=description,
            prompt_data=prompt_data,
            function_data=function_data,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def post_function_id_invoke(
        self,
        function_id: FunctionIdParam,
        *,
        input: typing.Optional[typing.Any] = OMIT,
        expected: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatCompletionMessageParam]] = OMIT,
        parent: typing.Optional[InvokeParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        mode: typing.Optional[StreamingMode] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]] = OMIT,
        overrides: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Invoke a function.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        input : typing.Optional[typing.Any]
            Argument to the function, which can be any JSON serializable value

        expected : typing.Optional[typing.Any]
            The expected output of the function

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Any relevant metadata. This will be logged and available as the `metadata` argument.

        tags : typing.Optional[typing.Sequence[str]]
            Any relevant tags to log on the span.

        messages : typing.Optional[typing.Sequence[ChatCompletionMessageParam]]
            If the function is an LLM, additional messages to pass along to it

        parent : typing.Optional[InvokeParent]

        stream : typing.Optional[bool]
            Whether to stream the response. If true, results will be returned in the Braintrust SSE format.

        mode : typing.Optional[StreamingMode]

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        mcp_auth : typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]]
            Map of MCP server URL to auth credentials

        overrides : typing.Optional[typing.Dict[str, typing.Any]]
            Partial function definition to merge with the function being invoked. Fields are validated against the function type's schema at runtime. For facets: { preprocessor?, prompt?, model? }. For prompts: { model?, ... }.

        version : typing.Optional[str]
            The version of the function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Function invocation response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.functions.post_function_id_invoke(
                function_id="function_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_function_id_invoke(
            function_id,
            input=input,
            expected=expected,
            metadata=metadata,
            tags=tags,
            messages=messages,
            parent=parent,
            stream=stream,
            mode=mode,
            strict=strict,
            mcp_auth=mcp_auth,
            overrides=overrides,
            version=version,
            request_options=request_options,
        )
        return _response.data
