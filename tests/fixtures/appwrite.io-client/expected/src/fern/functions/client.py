

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.execution import Execution
from ..types.execution_list import ExecutionList
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
