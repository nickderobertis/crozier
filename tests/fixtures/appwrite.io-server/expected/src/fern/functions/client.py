

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.execution import Execution
from ..types.execution_list import ExecutionList
from ..types.function import Function
from ..types.function_list import FunctionList
from ..types.tag import Tag
from ..types.tag_list import TagList
from .raw_client import AsyncRawFunctionsClient, RawFunctionsClient


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

    def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionList:
        """
        Get a list of all the project's functions. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionList
            Functions List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.list()
        """
        _response = self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        execute: typing.Sequence[str],
        name: str,
        runtime: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

        Parameters
        ----------
        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        runtime : str
            Execution runtime.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.create(
            execute=["execute"],
            name="name",
            runtime="runtime",
        )
        """
        _response = self._raw_client.create(
            execute=execute,
            name=name,
            runtime=runtime,
            events=events,
            schedule=schedule,
            timeout=timeout,
            vars=vars,
            request_options=request_options,
        )
        return _response.data

    def get(self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Function:
        """
        Get a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.get(
            function_id="functionId",
        )
        """
        _response = self._raw_client.get(function_id, request_options=request_options)
        return _response.data

    def update(
        self,
        function_id: str,
        *,
        execute: typing.Sequence[str],
        name: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Update function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.update(
            function_id="functionId",
            execute=["execute"],
            name="name",
        )
        """
        _response = self._raw_client.update(
            function_id,
            execute=execute,
            name=name,
            events=events,
            schedule=schedule,
            timeout=timeout,
            vars=vars,
            request_options=request_options,
        )
        return _response.data

    def delete(self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.delete(
            function_id="functionId",
        )
        """
        _response = self._raw_client.delete(function_id, request_options=request_options)
        return _response.data

    def list_executions(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionList:
        """
        Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's executions. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionList
            Executions List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.list_executions(
            function_id="functionId",
        )
        """
        _response = self._raw_client.list_executions(
            function_id,
            search=search,
            limit=limit,
            offset=offset,
            order_type=order_type,
            request_options=request_options,
        )
        return _response.data

    def create_execution(
        self,
        function_id: str,
        *,
        data: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Execution:
        """
        Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        data : typing.Optional[str]
            String of custom data to send to function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Execution
            Execution

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.create_execution(
            function_id="functionId",
        )
        """
        _response = self._raw_client.create_execution(function_id, data=data, request_options=request_options)
        return _response.data

    def get_execution(
        self, function_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Execution:
        """
        Get a function execution log by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execution_id : str
            Execution unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Execution
            Execution

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.get_execution(
            function_id="functionId",
            execution_id="executionId",
        )
        """
        _response = self._raw_client.get_execution(function_id, execution_id, request_options=request_options)
        return _response.data

    def update_tag(
        self, function_id: str, *, tag: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.update_tag(
            function_id="functionId",
            tag="tag",
        )
        """
        _response = self._raw_client.update_tag(function_id, tag=tag, request_options=request_options)
        return _response.data

    def list_tags(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagList:
        """
        Get a list of all the project's code tags. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagList
            Tags List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.list_tags(
            function_id="functionId",
        )
        """
        _response = self._raw_client.list_tags(
            function_id,
            search=search,
            limit=limit,
            offset=offset,
            order_type=order_type,
            request_options=request_options,
        )
        return _response.data

    def create_tag(
        self, function_id: str, *, code: str, command: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's tag to use your new tag UID.

        This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).

        Use the "command" param to set the entry point used to execute your code.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        code : str
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

        command : str
            Code execution command.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.create_tag(
            function_id="functionId",
            code="code",
            command="command",
        )
        """
        _response = self._raw_client.create_tag(
            function_id, code=code, command=command, request_options=request_options
        )
        return _response.data

    def get_tag(self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tag:
        """
        Get a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.get_tag(
            function_id="functionId",
            tag_id="tagId",
        )
        """
        _response = self._raw_client.get_tag(function_id, tag_id, request_options=request_options)
        return _response.data

    def delete_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.functions.delete_tag(
            function_id="functionId",
            tag_id="tagId",
        )
        """
        _response = self._raw_client.delete_tag(function_id, tag_id, request_options=request_options)
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

    async def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionList:
        """
        Get a list of all the project's functions. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionList
            Functions List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        execute: typing.Sequence[str],
        name: str,
        runtime: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

        Parameters
        ----------
        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        runtime : str
            Execution runtime.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.create(
                execute=["execute"],
                name="name",
                runtime="runtime",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            execute=execute,
            name=name,
            runtime=runtime,
            events=events,
            schedule=schedule,
            timeout=timeout,
            vars=vars,
            request_options=request_options,
        )
        return _response.data

    async def get(self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Function:
        """
        Get a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.get(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(function_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        function_id: str,
        *,
        execute: typing.Sequence[str],
        name: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Update function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.update(
                function_id="functionId",
                execute=["execute"],
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            function_id,
            execute=execute,
            name=name,
            events=events,
            schedule=schedule,
            timeout=timeout,
            vars=vars,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.delete(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(function_id, request_options=request_options)
        return _response.data

    async def list_executions(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionList:
        """
        Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's executions. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionList
            Executions List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.list_executions(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_executions(
            function_id,
            search=search,
            limit=limit,
            offset=offset,
            order_type=order_type,
            request_options=request_options,
        )
        return _response.data

    async def create_execution(
        self,
        function_id: str,
        *,
        data: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Execution:
        """
        Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        data : typing.Optional[str]
            String of custom data to send to function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Execution
            Execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.create_execution(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_execution(function_id, data=data, request_options=request_options)
        return _response.data

    async def get_execution(
        self, function_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Execution:
        """
        Get a function execution log by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execution_id : str
            Execution unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Execution
            Execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.get_execution(
                function_id="functionId",
                execution_id="executionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_execution(function_id, execution_id, request_options=request_options)
        return _response.data

    async def update_tag(
        self, function_id: str, *, tag: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Function

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.update_tag(
                function_id="functionId",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag(function_id, tag=tag, request_options=request_options)
        return _response.data

    async def list_tags(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagList:
        """
        Get a list of all the project's code tags. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagList
            Tags List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.list_tags(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(
            function_id,
            search=search,
            limit=limit,
            offset=offset,
            order_type=order_type,
            request_options=request_options,
        )
        return _response.data

    async def create_tag(
        self, function_id: str, *, code: str, command: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's tag to use your new tag UID.

        This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).

        Use the "command" param to set the entry point used to execute your code.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        code : str
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

        command : str
            Code execution command.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.create_tag(
                function_id="functionId",
                code="code",
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag(
            function_id, code=code, command=command, request_options=request_options
        )
        return _response.data

    async def get_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Get a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.get_tag(
                function_id="functionId",
                tag_id="tagId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag(function_id, tag_id, request_options=request_options)
        return _response.data

    async def delete_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.delete_tag(
                function_id="functionId",
                tag_id="tagId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(function_id, tag_id, request_options=request_options)
        return _response.data
