

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.node_data import NodeData
from ..types.parameters_validation_result_dto import ParametersValidationResultDto
from ..types.results_with_counts_dto import ResultsWithCountsDto
from ..types.scenario_test_capabilities import ScenarioTestCapabilities
from ..types.scenario_test_data import ScenarioTestData
from ..types.source_test_capabilities import SourceTestCapabilities
from ..types.test_case import TestCase
from ..types.test_case_result_event import TestCaseResultEvent
from ..types.test_source_parameters import TestSourceParameters
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTestingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def post_api_scenariotesting_scenarioname_performmultipletestcases(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_cases: typing.Sequence[TestCase],
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[TestCaseResultEvent]]]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_cases : typing.Sequence[TestCase]

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[TestCaseResultEvent]]]

        """
        with self._client_wrapper.httpx_client.stream(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performMultipleTestCases",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testCases": convert_and_respect_annotation_metadata(
                    object_=test_cases, annotation=typing.Sequence[TestCase], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[TestCaseResultEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        TestCaseResultEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=TestCaseResultEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 501:
                        raise NotImplementedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def post_api_scenariotesting_scenarioname_capabilities(
        self,
        scenario_name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScenarioTestCapabilities]:
        """
        Parameters
        ----------
        scenario_name : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScenarioTestCapabilities]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/capabilities",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScenarioTestCapabilities,
                    parse_obj_as(
                        type_=ScenarioTestCapabilities,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_performtestcase(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_case: TestCase,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_case : TestCase

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResultsWithCountsDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performTestCase",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testCase": convert_and_respect_annotation_metadata(
                    object_=test_case, annotation=TestCase, direction="write"
                ),
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
                    ResultsWithCountsDto,
                    parse_obj_as(
                        type_=ResultsWithCountsDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_performtest(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_data : ScenarioTestData

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResultsWithCountsDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performTest",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testData": convert_and_respect_annotation_metadata(
                    object_=test_data, annotation=ScenarioTestData, direction="write"
                ),
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
                    ResultsWithCountsDto,
                    parse_obj_as(
                        type_=ResultsWithCountsDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_generatedtestdata(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        number_of_samples: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        number_of_samples : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/generatedTestData",
            method="POST",
            json={
                "scenarioGraph": scenario_graph,
                "numberOfSamples": number_of_samples,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_validate(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_data : ScenarioTestData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParametersValidationResultDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/validate",
            method="POST",
            json={
                "scenarioGraph": scenario_graph,
                "testData": convert_and_respect_annotation_metadata(
                    object_=test_data, annotation=ScenarioTestData, direction="write"
                ),
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
                    ParametersValidationResultDto,
                    parse_obj_as(
                        type_=ParametersValidationResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_sourcecapabilities(
        self, scenario_name: str, *, node_data: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SourceTestCapabilities]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceTestCapabilities]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/sourceCapabilities",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
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
                    SourceTestCapabilities,
                    parse_obj_as(
                        type_=SourceTestCapabilities,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_scenariotesting_scenarioname_sourcevalidate(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        source_parameters: TestSourceParameters,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        source_parameters : TestSourceParameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParametersValidationResultDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/sourceValidate",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
                "sourceParameters": convert_and_respect_annotation_metadata(
                    object_=source_parameters, annotation=TestSourceParameters, direction="write"
                ),
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
                    ParametersValidationResultDto,
                    parse_obj_as(
                        type_=ParametersValidationResultDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTestingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def post_api_scenariotesting_scenarioname_performmultipletestcases(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_cases: typing.Sequence[TestCase],
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[TestCaseResultEvent]]]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_cases : typing.Sequence[TestCase]

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[TestCaseResultEvent]]]

        """
        async with self._client_wrapper.httpx_client.stream(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performMultipleTestCases",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testCases": convert_and_respect_annotation_metadata(
                    object_=test_cases, annotation=typing.Sequence[TestCase], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[TestCaseResultEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        TestCaseResultEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=TestCaseResultEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 501:
                        raise NotImplementedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                str,
                                parse_obj_as(
                                    type_=str,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def post_api_scenariotesting_scenarioname_capabilities(
        self,
        scenario_name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScenarioTestCapabilities]:
        """
        Parameters
        ----------
        scenario_name : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScenarioTestCapabilities]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/capabilities",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScenarioTestCapabilities,
                    parse_obj_as(
                        type_=ScenarioTestCapabilities,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_performtestcase(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_case: TestCase,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_case : TestCase

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResultsWithCountsDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performTestCase",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testCase": convert_and_respect_annotation_metadata(
                    object_=test_case, annotation=TestCase, direction="write"
                ),
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
                    ResultsWithCountsDto,
                    parse_obj_as(
                        type_=ResultsWithCountsDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_performtest(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_data : ScenarioTestData

        skip_results_per_node : typing.Optional[bool]

        skip_results_per_transition : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResultsWithCountsDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/performTest",
            method="POST",
            params={
                "skipResultsPerNode": skip_results_per_node,
                "skipResultsPerTransition": skip_results_per_transition,
            },
            json={
                "scenarioGraph": scenario_graph,
                "testData": convert_and_respect_annotation_metadata(
                    object_=test_data, annotation=ScenarioTestData, direction="write"
                ),
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
                    ResultsWithCountsDto,
                    parse_obj_as(
                        type_=ResultsWithCountsDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_generatedtestdata(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        number_of_samples: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        number_of_samples : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/generatedTestData",
            method="POST",
            json={
                "scenarioGraph": scenario_graph,
                "numberOfSamples": number_of_samples,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_validate(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_graph : typing.Dict[str, typing.Any]

        test_data : ScenarioTestData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParametersValidationResultDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/validate",
            method="POST",
            json={
                "scenarioGraph": scenario_graph,
                "testData": convert_and_respect_annotation_metadata(
                    object_=test_data, annotation=ScenarioTestData, direction="write"
                ),
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
                    ParametersValidationResultDto,
                    parse_obj_as(
                        type_=ParametersValidationResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_sourcecapabilities(
        self, scenario_name: str, *, node_data: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SourceTestCapabilities]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceTestCapabilities]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/sourceCapabilities",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
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
                    SourceTestCapabilities,
                    parse_obj_as(
                        type_=SourceTestCapabilities,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_scenariotesting_scenarioname_sourcevalidate(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        source_parameters: TestSourceParameters,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        source_parameters : TestSourceParameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParametersValidationResultDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/scenarioTesting/{encode_path_param(scenario_name)}/sourceValidate",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
                "sourceParameters": convert_and_respect_annotation_metadata(
                    object_=source_parameters, annotation=TestSourceParameters, direction="write"
                ),
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
                    ParametersValidationResultDto,
                    parse_obj_as(
                        type_=ParametersValidationResultDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
