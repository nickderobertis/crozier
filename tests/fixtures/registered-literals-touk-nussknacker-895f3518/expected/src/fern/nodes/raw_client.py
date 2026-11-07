

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.additional_info import AdditionalInfo
from ..types.caret_position2d import CaretPosition2D
from ..types.edge import Edge
from ..types.expression import Expression
from ..types.expression_suggestion_dto import ExpressionSuggestionDto
from ..types.generate_enricher_mock_response_dto import GenerateEnricherMockResponseDto
from ..types.map_map_string_typing_result_in_json import MapMapStringTypingResultInJson
from ..types.map_node_test_case import MapNodeTestCase
from ..types.map_typing_result_in_json import MapTypingResultInJson
from ..types.node_data import NodeData
from ..types.node_validation_result_dto import NodeValidationResultDto
from ..types.parameters_validation_result_dto import ParametersValidationResultDto
from ..types.process_additional_fields import ProcessAdditionalFields
from ..types.test_case_additional_variables_response_dto import TestCaseAdditionalVariablesResponseDto
from ..types.ui_value_parameter_dto import UiValueParameterDto
from .types.generate_enricher_mock_request_dto_enricher import GenerateEnricherMockRequestDtoEnricher
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_nodes_scenarioname_additionalinfo(
        self, scenario_name: str, *, request: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AdditionalInfo]]:
        """
        Parameters
        ----------
        scenario_name : str

        request : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AdditionalInfo]]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/additionalInfo",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=NodeData, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AdditionalInfo],
                    parse_obj_as(
                        type_=typing.Optional[AdditionalInfo],
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

    def post_api_nodes_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        variable_types: MapTypingResultInJson,
        branch_variable_types: typing.Optional[MapMapStringTypingResultInJson] = OMIT,
        outgoing_edges: typing.Optional[typing.Sequence[Edge]] = OMIT,
        test_cases: typing.Optional[MapNodeTestCase] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NodeValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        variable_types : MapTypingResultInJson

        branch_variable_types : typing.Optional[MapMapStringTypingResultInJson]

        outgoing_edges : typing.Optional[typing.Sequence[Edge]]

        test_cases : typing.Optional[MapNodeTestCase]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodeValidationResultDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/validation",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
                ),
                "branchVariableTypes": convert_and_respect_annotation_metadata(
                    object_=branch_variable_types,
                    annotation=typing.Optional[MapMapStringTypingResultInJson],
                    direction="write",
                ),
                "outgoingEdges": convert_and_respect_annotation_metadata(
                    object_=outgoing_edges, annotation=typing.Optional[typing.Sequence[Edge]], direction="write"
                ),
                "testCases": convert_and_respect_annotation_metadata(
                    object_=test_cases, annotation=typing.Optional[MapNodeTestCase], direction="write"
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
                    NodeValidationResultDto,
                    parse_obj_as(
                        type_=NodeValidationResultDto,
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

    def post_api_parameters_processingtype_suggestions(
        self,
        processing_type: str,
        *,
        expression: Expression,
        caret_position2d: CaretPosition2D,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ExpressionSuggestionDto]]:
        """
        Parameters
        ----------
        processing_type : str

        expression : Expression

        caret_position2d : CaretPosition2D

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ExpressionSuggestionDto]]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/suggestions",
            method="POST",
            json={
                "expression": convert_and_respect_annotation_metadata(
                    object_=expression, annotation=Expression, direction="write"
                ),
                "caretPosition2d": convert_and_respect_annotation_metadata(
                    object_=caret_position2d, annotation=CaretPosition2D, direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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
                    typing.List[ExpressionSuggestionDto],
                    parse_obj_as(
                        type_=typing.List[ExpressionSuggestionDto],
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

    def post_api_parameters_processingtype_validate(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        parameters: typing.Optional[typing.Sequence[UiValueParameterDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        parameters : typing.Optional[typing.Sequence[UiValueParameterDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParametersValidationResultDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/validate",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[UiValueParameterDto], direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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

    def post_api_properties_scenarioname_additionalinfo(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AdditionalInfo]]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AdditionalInfo]]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/properties/{encode_path_param(scenario_name)}/additionalInfo",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AdditionalInfo],
                    parse_obj_as(
                        type_=typing.Optional[AdditionalInfo],
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

    def post_api_properties_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        additional_fields: ProcessAdditionalFields,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NodeValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        additional_fields : ProcessAdditionalFields

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodeValidationResultDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/properties/{encode_path_param(scenario_name)}/validation",
            method="POST",
            json={
                "additionalFields": convert_and_respect_annotation_metadata(
                    object_=additional_fields, annotation=ProcessAdditionalFields, direction="write"
                ),
                "name": name,
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
                    NodeValidationResultDto,
                    parse_obj_as(
                        type_=NodeValidationResultDto,
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

    def post_api_nodes_scenarioname_records(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        limit : typing.Optional[int]
            Limit the number of records returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/records",
            method="POST",
            params={
                "limit": limit,
            },
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

    def post_api_parameters_processingtype_testcase_additionalvariables(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TestCaseAdditionalVariablesResponseDto]:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestCaseAdditionalVariablesResponseDto]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/testCase/additionalVariables",
            method="POST",
            json={
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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
                    TestCaseAdditionalVariablesResponseDto,
                    parse_obj_as(
                        type_=TestCaseAdditionalVariablesResponseDto,
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

    def post_api_nodes_scenarioname_testcase_enrichermock(
        self,
        scenario_name: str,
        *,
        variable_types: MapTypingResultInJson,
        enricher: GenerateEnricherMockRequestDtoEnricher,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[GenerateEnricherMockResponseDto]]:
        """
        Parameters
        ----------
        scenario_name : str

        variable_types : MapTypingResultInJson

        enricher : GenerateEnricherMockRequestDtoEnricher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[GenerateEnricherMockResponseDto]]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/testCase/enricherMock",
            method="POST",
            json={
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
                ),
                "enricher": convert_and_respect_annotation_metadata(
                    object_=enricher, annotation=GenerateEnricherMockRequestDtoEnricher, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GenerateEnricherMockResponseDto],
                    parse_obj_as(
                        type_=typing.Optional[GenerateEnricherMockResponseDto],
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


class AsyncRawNodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_nodes_scenarioname_additionalinfo(
        self, scenario_name: str, *, request: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AdditionalInfo]]:
        """
        Parameters
        ----------
        scenario_name : str

        request : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AdditionalInfo]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/additionalInfo",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=NodeData, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AdditionalInfo],
                    parse_obj_as(
                        type_=typing.Optional[AdditionalInfo],
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

    async def post_api_nodes_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        variable_types: MapTypingResultInJson,
        branch_variable_types: typing.Optional[MapMapStringTypingResultInJson] = OMIT,
        outgoing_edges: typing.Optional[typing.Sequence[Edge]] = OMIT,
        test_cases: typing.Optional[MapNodeTestCase] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NodeValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        variable_types : MapTypingResultInJson

        branch_variable_types : typing.Optional[MapMapStringTypingResultInJson]

        outgoing_edges : typing.Optional[typing.Sequence[Edge]]

        test_cases : typing.Optional[MapNodeTestCase]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodeValidationResultDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/validation",
            method="POST",
            json={
                "nodeData": convert_and_respect_annotation_metadata(
                    object_=node_data, annotation=NodeData, direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
                ),
                "branchVariableTypes": convert_and_respect_annotation_metadata(
                    object_=branch_variable_types,
                    annotation=typing.Optional[MapMapStringTypingResultInJson],
                    direction="write",
                ),
                "outgoingEdges": convert_and_respect_annotation_metadata(
                    object_=outgoing_edges, annotation=typing.Optional[typing.Sequence[Edge]], direction="write"
                ),
                "testCases": convert_and_respect_annotation_metadata(
                    object_=test_cases, annotation=typing.Optional[MapNodeTestCase], direction="write"
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
                    NodeValidationResultDto,
                    parse_obj_as(
                        type_=NodeValidationResultDto,
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

    async def post_api_parameters_processingtype_suggestions(
        self,
        processing_type: str,
        *,
        expression: Expression,
        caret_position2d: CaretPosition2D,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ExpressionSuggestionDto]]:
        """
        Parameters
        ----------
        processing_type : str

        expression : Expression

        caret_position2d : CaretPosition2D

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ExpressionSuggestionDto]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/suggestions",
            method="POST",
            json={
                "expression": convert_and_respect_annotation_metadata(
                    object_=expression, annotation=Expression, direction="write"
                ),
                "caretPosition2d": convert_and_respect_annotation_metadata(
                    object_=caret_position2d, annotation=CaretPosition2D, direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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
                    typing.List[ExpressionSuggestionDto],
                    parse_obj_as(
                        type_=typing.List[ExpressionSuggestionDto],
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

    async def post_api_parameters_processingtype_validate(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        parameters: typing.Optional[typing.Sequence[UiValueParameterDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParametersValidationResultDto]:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        parameters : typing.Optional[typing.Sequence[UiValueParameterDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParametersValidationResultDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/validate",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[UiValueParameterDto], direction="write"
                ),
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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

    async def post_api_properties_scenarioname_additionalinfo(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AdditionalInfo]]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AdditionalInfo]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/properties/{encode_path_param(scenario_name)}/additionalInfo",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AdditionalInfo],
                    parse_obj_as(
                        type_=typing.Optional[AdditionalInfo],
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

    async def post_api_properties_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        additional_fields: ProcessAdditionalFields,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NodeValidationResultDto]:
        """
        Parameters
        ----------
        scenario_name : str

        additional_fields : ProcessAdditionalFields

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodeValidationResultDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/properties/{encode_path_param(scenario_name)}/validation",
            method="POST",
            json={
                "additionalFields": convert_and_respect_annotation_metadata(
                    object_=additional_fields, annotation=ProcessAdditionalFields, direction="write"
                ),
                "name": name,
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
                    NodeValidationResultDto,
                    parse_obj_as(
                        type_=NodeValidationResultDto,
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

    async def post_api_nodes_scenarioname_records(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        limit : typing.Optional[int]
            Limit the number of records returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/records",
            method="POST",
            params={
                "limit": limit,
            },
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

    async def post_api_parameters_processingtype_testcase_additionalvariables(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TestCaseAdditionalVariablesResponseDto]:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestCaseAdditionalVariablesResponseDto]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/parameters/{encode_path_param(processing_type)}/testCase/additionalVariables",
            method="POST",
            json={
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
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
                    TestCaseAdditionalVariablesResponseDto,
                    parse_obj_as(
                        type_=TestCaseAdditionalVariablesResponseDto,
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

    async def post_api_nodes_scenarioname_testcase_enrichermock(
        self,
        scenario_name: str,
        *,
        variable_types: MapTypingResultInJson,
        enricher: GenerateEnricherMockRequestDtoEnricher,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[GenerateEnricherMockResponseDto]]:
        """
        Parameters
        ----------
        scenario_name : str

        variable_types : MapTypingResultInJson

        enricher : GenerateEnricherMockRequestDtoEnricher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[GenerateEnricherMockResponseDto]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nodes/{encode_path_param(scenario_name)}/testCase/enricherMock",
            method="POST",
            json={
                "variableTypes": convert_and_respect_annotation_metadata(
                    object_=variable_types, annotation=MapTypingResultInJson, direction="write"
                ),
                "enricher": convert_and_respect_annotation_metadata(
                    object_=enricher, annotation=GenerateEnricherMockRequestDtoEnricher, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GenerateEnricherMockResponseDto],
                    parse_obj_as(
                        type_=typing.Optional[GenerateEnricherMockResponseDto],
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
