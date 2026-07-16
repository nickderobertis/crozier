

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.counter import Counter
from ..types.operation_headers import OperationHeaders
from ..types.request_response_pair import RequestResponsePair
from ..types.test_case_result import TestCaseResult
from ..types.test_result import TestResult
from ..types.test_runner_type import TestRunnerType
from ..types.unidirectional_event import UnidirectionalEvent


OMIT = typing.cast(typing.Any, ...)


class RawTestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[TestResult]:
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
        HttpResponse[TestResult]
            Created TestResult (empty shell cause tests are executed asynchronously)
        """
        _response = self._client_wrapper.httpx_client.request(
            "tests",
            method="POST",
            json={
                "filteredOperations": filtered_operations,
                "operationHeaders": convert_and_respect_annotation_metadata(
                    object_=operation_headers, annotation=OperationHeaders, direction="write"
                ),
                "runnerType": runner_type,
                "secretName": secret_name,
                "serviceId": service_id,
                "testEndpoint": test_endpoint,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResult,
                    parse_obj_as(
                        type_=TestResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_test_results_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TestResult]]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TestResult]]
            List of TestResults for the Service having the requested id
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/service/{jsonable_encoder(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResult],
                    parse_obj_as(
                        type_=typing.List[TestResult],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_test_results_by_service_counter(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Counter]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Counter]
            Number of TestResults for this Service in datastore
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/service/{jsonable_encoder(service_id)}/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_test_result(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestResult]:
        """


        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestResult]
            Requested TestResult
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResult,
                    parse_obj_as(
                        type_=TestResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_events_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UnidirectionalEvent]]:
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
        HttpResponse[typing.List[UnidirectionalEvent]]
            List of event messages for this TestCase
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/events/{jsonable_encoder(test_case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UnidirectionalEvent],
                    parse_obj_as(
                        type_=typing.List[UnidirectionalEvent],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_messages_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RequestResponsePair]]:
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
        HttpResponse[typing.List[RequestResponsePair]]
            List of request and response messages for this TestCase
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/messages/{jsonable_encoder(test_case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestResponsePair],
                    parse_obj_as(
                        type_=typing.List[RequestResponsePair],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def report_test_case_result(
        self, id: str, *, operation_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestCaseResult]:
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
        HttpResponse[TestCaseResult]
            TestCaseResult is reported
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/testCaseResult",
            method="POST",
            json={
                "operationName": operation_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestCaseResult,
                    parse_obj_as(
                        type_=TestCaseResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[TestResult]:
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
        AsyncHttpResponse[TestResult]
            Created TestResult (empty shell cause tests are executed asynchronously)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tests",
            method="POST",
            json={
                "filteredOperations": filtered_operations,
                "operationHeaders": convert_and_respect_annotation_metadata(
                    object_=operation_headers, annotation=OperationHeaders, direction="write"
                ),
                "runnerType": runner_type,
                "secretName": secret_name,
                "serviceId": service_id,
                "testEndpoint": test_endpoint,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResult,
                    parse_obj_as(
                        type_=TestResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_test_results_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TestResult]]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TestResult]]
            List of TestResults for the Service having the requested id
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/service/{jsonable_encoder(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResult],
                    parse_obj_as(
                        type_=typing.List[TestResult],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_test_results_by_service_counter(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Counter]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of Service to manage TestResults for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Counter]
            Number of TestResults for this Service in datastore
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/service/{jsonable_encoder(service_id)}/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_test_result(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestResult]:
        """


        Parameters
        ----------
        id : str
            Unique identifier of TestResult to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestResult]
            Requested TestResult
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResult,
                    parse_obj_as(
                        type_=TestResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_events_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UnidirectionalEvent]]:
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
        AsyncHttpResponse[typing.List[UnidirectionalEvent]]
            List of event messages for this TestCase
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/events/{jsonable_encoder(test_case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UnidirectionalEvent],
                    parse_obj_as(
                        type_=typing.List[UnidirectionalEvent],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_messages_by_test_case(
        self, id: str, test_case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RequestResponsePair]]:
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
        AsyncHttpResponse[typing.List[RequestResponsePair]]
            List of request and response messages for this TestCase
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/messages/{jsonable_encoder(test_case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestResponsePair],
                    parse_obj_as(
                        type_=typing.List[RequestResponsePair],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def report_test_case_result(
        self, id: str, *, operation_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestCaseResult]:
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
        AsyncHttpResponse[TestCaseResult]
            TestCaseResult is reported
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tests/{jsonable_encoder(id)}/testCaseResult",
            method="POST",
            json={
                "operationName": operation_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestCaseResult,
                    parse_obj_as(
                        type_=TestCaseResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
