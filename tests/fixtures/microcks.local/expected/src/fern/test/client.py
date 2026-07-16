

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.counter import Counter
from ..types.operation_headers import OperationHeaders
from ..types.request_response_pair import RequestResponsePair
from ..types.test_case_result import TestCaseResult
from ..types.test_result import TestResult
from ..types.test_runner_type import TestRunnerType
from ..types.unidirectional_event import UnidirectionalEvent
from .raw_client import AsyncRawTestClient, RawTestClient


OMIT = typing.cast(typing.Any, ...)


class TestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestClient
        """
        return self._raw_client

    def create_test(
        self,
        *,
        runner_type: TestRunnerType,
        service_id: str,
        test_endpoint: str,
        timeout: int,
        filtered_operations: typing.Optional[typing.Sequence[str]] = OMIT,
        operation_headers: typing.Optional[OperationHeaders] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResult:
        """
        Parameters
        ----------
        runner_type : TestRunnerType
            Runner used for this test

        service_id : str
            Unique identifier of service to test

        test_endpoint : str
            Endpoint to test for this service

        timeout : int
            The maximum time (in milliseconds) to wait for this test ends

        filtered_operations : typing.Optional[typing.Sequence[str]]
            A restriction on service operations to test

        operation_headers : typing.Optional[OperationHeaders]
            This test operations headers override

        secret_name : typing.Optional[str]
            The name of Secret to use for connecting the test endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResult
            Created TestResult (empty shell cause tests are executed asynchronously)

        Examples
        --------
        from fern import FernApi, TestRunnerType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.create_test(
            runner_type=TestRunnerType.HTTP,
            service_id="serviceId",
            test_endpoint="testEndpoint",
            timeout=1,
        )
        """
        _response = self._raw_client.create_test(
            runner_type=runner_type,
            service_id=service_id,
            test_endpoint=test_endpoint,
            timeout=timeout,
            filtered_operations=filtered_operations,
            operation_headers=operation_headers,
            secret_name=secret_name,
            request_options=request_options,
        )
        return _response.data

    def get_test_results_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResult]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResult]
            List of TestResults for the Service having the requested id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.get_test_results_by_service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_test_results_by_service(service_id, request_options=request_options)
        return _response.data

    def get_test_results_by_service_counter(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Counter:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of TestResults for this Service in datastore

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.get_test_results_by_service_counter(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_test_results_by_service_counter(service_id, request_options=request_options)
        return _response.data

    def get_test_result(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TestResult:
        """


        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResult
            Requested TestResult

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.get_test_result(
            id="id",
        )
        """
        _response = self._raw_client.get_test_result(id, request_options=request_options)
        return _response.data

    def get_events_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UnidirectionalEvent]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        test_case_id : str
            Unique identifier of TetsCaseResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UnidirectionalEvent]
            List of event messages for this TestCase

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.get_events_by_test_case(
            id="id",
            test_case_id="testCaseId",
        )
        """
        _response = self._raw_client.get_events_by_test_case(id, test_case_id, request_options=request_options)
        return _response.data

    def get_messages_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestResponsePair]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        test_case_id : str
            Unique identifier of TetsCaseResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestResponsePair]
            List of request and response messages for this TestCase

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.get_messages_by_test_case(
            id="id",
            test_case_id="testCaseId",
        )
        """
        _response = self._raw_client.get_messages_by_test_case(id, test_case_id, request_options=request_options)
        return _response.data

    def report_test_case_result(
        self, id: str, *, operation_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TestCaseResult:
        """
        Report a TestCaseResult (typically used by a Test runner)

        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        operation_name : str
            Name of related operation for this TestCase

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestCaseResult
            TestCaseResult is reported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.test.report_test_case_result(
            id="id",
            operation_name="operationName",
        )
        """
        _response = self._raw_client.report_test_case_result(
            id, operation_name=operation_name, request_options=request_options
        )
        return _response.data


class AsyncTestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestClient
        """
        return self._raw_client

    async def create_test(
        self,
        *,
        runner_type: TestRunnerType,
        service_id: str,
        test_endpoint: str,
        timeout: int,
        filtered_operations: typing.Optional[typing.Sequence[str]] = OMIT,
        operation_headers: typing.Optional[OperationHeaders] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResult:
        """
        Parameters
        ----------
        runner_type : TestRunnerType
            Runner used for this test

        service_id : str
            Unique identifier of service to test

        test_endpoint : str
            Endpoint to test for this service

        timeout : int
            The maximum time (in milliseconds) to wait for this test ends

        filtered_operations : typing.Optional[typing.Sequence[str]]
            A restriction on service operations to test

        operation_headers : typing.Optional[OperationHeaders]
            This test operations headers override

        secret_name : typing.Optional[str]
            The name of Secret to use for connecting the test endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResult
            Created TestResult (empty shell cause tests are executed asynchronously)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestRunnerType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.create_test(
                runner_type=TestRunnerType.HTTP,
                service_id="serviceId",
                test_endpoint="testEndpoint",
                timeout=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_test(
            runner_type=runner_type,
            service_id=service_id,
            test_endpoint=test_endpoint,
            timeout=timeout,
            filtered_operations=filtered_operations,
            operation_headers=operation_headers,
            secret_name=secret_name,
            request_options=request_options,
        )
        return _response.data

    async def get_test_results_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResult]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResult]
            List of TestResults for the Service having the requested id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.get_test_results_by_service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_results_by_service(service_id, request_options=request_options)
        return _response.data

    async def get_test_results_by_service_counter(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Counter:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of TestResults for this Service in datastore

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.get_test_results_by_service_counter(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_results_by_service_counter(
            service_id, request_options=request_options
        )
        return _response.data

    async def get_test_result(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TestResult:
        """


        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResult
            Requested TestResult

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.get_test_result(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_result(id, request_options=request_options)
        return _response.data

    async def get_events_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UnidirectionalEvent]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        test_case_id : str
            Unique identifier of TetsCaseResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UnidirectionalEvent]
            List of event messages for this TestCase

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.get_events_by_test_case(
                id="id",
                test_case_id="testCaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events_by_test_case(id, test_case_id, request_options=request_options)
        return _response.data

    async def get_messages_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestResponsePair]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        test_case_id : str
            Unique identifier of TetsCaseResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestResponsePair]
            List of request and response messages for this TestCase

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.get_messages_by_test_case(
                id="id",
                test_case_id="testCaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_messages_by_test_case(id, test_case_id, request_options=request_options)
        return _response.data

    async def report_test_case_result(
        self, id: str, *, operation_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TestCaseResult:
        """
        Report a TestCaseResult (typically used by a Test runner)

        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        operation_name : str
            Name of related operation for this TestCase

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestCaseResult
            TestCaseResult is reported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test.report_test_case_result(
                id="id",
                operation_name="operationName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_test_case_result(
            id, operation_name=operation_name, request_options=request_options
        )
        return _response.data
