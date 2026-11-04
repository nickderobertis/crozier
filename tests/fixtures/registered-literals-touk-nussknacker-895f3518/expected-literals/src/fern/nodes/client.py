

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawNodesClient, RawNodesClient
from .types.generate_enricher_mock_request_dto_enricher import GenerateEnricherMockRequestDtoEnricher


OMIT = typing.cast(typing.Any, ...)


class NodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodesClient
        """
        return self._raw_client

    def post_api_nodes_scenarioname_additionalinfo(
        self, scenario_name: str, *, request: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AdditionalInfo]:
        """
        Parameters
        ----------
        scenario_name : str

        request : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AdditionalInfo]


        Examples
        --------
        from fern import Expression, FernApi, NodeData_Enricher, Parameter, ServiceRef

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_nodes_scenarioname_additionalinfo(
            scenario_name="scenarioName",
            request=NodeData_Enricher(
                id="99ae6a31-a55d-4d52-89af-58f471e7143d",
                output="out",
                service=ServiceRef(
                    id="paramService",
                    parameters=[
                        Parameter(
                            name="id",
                            expression=Expression(
                                language="spel",
                                expression="'a'",
                            ),
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.post_api_nodes_scenarioname_additionalinfo(
            scenario_name, request=request, request_options=request_options
        )
        return _response.data

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
    ) -> NodeValidationResultDto:
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
        NodeValidationResultDto


        Examples
        --------
        from fern import (
            Expression,
            FernApi,
            MapTypingResultInJsonValue_TypedClass,
            NodeData_Filter,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_nodes_scenarioname_validation(
            scenario_name="scenarioName",
            node_data=NodeData_Filter(
                expression=Expression(
                    language="spel",
                    expression="#longValue > 1",
                ),
                id="99ae6a31-a55d-4d52-89af-58f471e7143d",
            ),
            variable_types={
                "existButString": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
                "longValue": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
            },
        )
        """
        _response = self._raw_client.post_api_nodes_scenarioname_validation(
            scenario_name,
            node_data=node_data,
            variable_types=variable_types,
            branch_variable_types=branch_variable_types,
            outgoing_edges=outgoing_edges,
            test_cases=test_cases,
            request_options=request_options,
        )
        return _response.data

    def post_api_parameters_processingtype_suggestions(
        self,
        processing_type: str,
        *,
        expression: Expression,
        caret_position2d: CaretPosition2D,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExpressionSuggestionDto]:
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
        typing.List[ExpressionSuggestionDto]


        Examples
        --------
        from fern import (
            CaretPosition2D,
            Expression,
            FernApi,
            MapTypingResultInJsonValue_TypedObjectTypingResult,
            TypingResult_TypedClass,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_parameters_processingtype_suggestions(
            processing_type="processingType",
            expression=Expression(
                language="spel",
                expression="#inpu",
            ),
            caret_position2d=CaretPosition2D(
                row=0,
                column=5,
            ),
            variable_types={
                "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
                    fields={
                        "key": TypingResult_TypedClass(
                            ref_clazz_name="refClazzName",
                        )
                    },
                    ref_clazz_name="refClazzName",
                )
            },
        )
        """
        _response = self._raw_client.post_api_parameters_processingtype_suggestions(
            processing_type,
            expression=expression,
            caret_position2d=caret_position2d,
            variable_types=variable_types,
            request_options=request_options,
        )
        return _response.data

    def post_api_parameters_processingtype_validate(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        parameters: typing.Optional[typing.Sequence[UiValueParameterDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        from fern import (
            Expression,
            FernApi,
            MapTypingResultInJsonValue_TypedObjectTypingResult,
            TypingResult_TypedClass,
            UiValueParameterDto,
            UiValueParameterDtoTyp_TypedClass,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_parameters_processingtype_validate(
            processing_type="processingType",
            parameters=[
                UiValueParameterDto(
                    name="condition",
                    typ=UiValueParameterDtoTyp_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                    expression=Expression(
                        language="spel",
                        expression="#input.amount > 2",
                    ),
                )
            ],
            variable_types={
                "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
                    fields={
                        "key": TypingResult_TypedClass(
                            ref_clazz_name="refClazzName",
                        )
                    },
                    ref_clazz_name="refClazzName",
                )
            },
        )
        """
        _response = self._raw_client.post_api_parameters_processingtype_validate(
            processing_type, variable_types=variable_types, parameters=parameters, request_options=request_options
        )
        return _response.data

    def post_api_properties_scenarioname_additionalinfo(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AdditionalInfo]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AdditionalInfo]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_properties_scenarioname_additionalinfo(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.post_api_properties_scenarioname_additionalinfo(
            scenario_name, request_options=request_options
        )
        return _response.data

    def post_api_properties_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        additional_fields: ProcessAdditionalFields,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodeValidationResultDto:
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
        NodeValidationResultDto


        Examples
        --------
        from fern import FernApi, ProcessAdditionalFields

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_properties_scenarioname_validation(
            scenario_name="scenarioName",
            additional_fields=ProcessAdditionalFields(
                properties={
                    "parallelism": "",
                    "checkpointIntervalInSeconds": "",
                    "numberOfThreads": "2",
                    "spillStateToDisk": "true",
                    "environment": "test",
                    "useAsyncInterpretation": "",
                },
                meta_data_type="StreamMetaData",
                show_description=False,
            ),
            name="test",
        )
        """
        _response = self._raw_client.post_api_properties_scenarioname_validation(
            scenario_name, additional_fields=additional_fields, name=name, request_options=request_options
        )
        return _response.data

    def post_api_nodes_scenarioname_records(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str


        Examples
        --------
        from fern import Expression, FernApi, NodeData_Variable

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_nodes_scenarioname_records(
            scenario_name="scenarioName",
            node_data=NodeData_Variable(
                id="id",
                operation="SET",
                var_name="varName",
                value=Expression(
                    language="language",
                    expression="expression",
                ),
            ),
        )
        """
        _response = self._raw_client.post_api_nodes_scenarioname_records(
            scenario_name, node_data=node_data, limit=limit, request_options=request_options
        )
        return _response.data

    def post_api_parameters_processingtype_testcase_additionalvariables(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestCaseAdditionalVariablesResponseDto:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestCaseAdditionalVariablesResponseDto


        Examples
        --------
        from fern import FernApi, MapTypingResultInJsonValue_TypedClass

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_parameters_processingtype_testcase_additionalvariables(
            processing_type="processingType",
            variable_types={
                "amount": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
                "name": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
            },
        )
        """
        _response = self._raw_client.post_api_parameters_processingtype_testcase_additionalvariables(
            processing_type, variable_types=variable_types, request_options=request_options
        )
        return _response.data

    def post_api_nodes_scenarioname_testcase_enrichermock(
        self,
        scenario_name: str,
        *,
        variable_types: MapTypingResultInJson,
        enricher: GenerateEnricherMockRequestDtoEnricher,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GenerateEnricherMockResponseDto]:
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
        typing.Optional[GenerateEnricherMockResponseDto]


        Examples
        --------
        from fern.nodes import GenerateEnricherMockRequestDtoEnricher

        from fern import (
            Expression,
            FernApi,
            MapTypingResultInJsonValue_TypedClass,
            Parameter,
            ServiceRef,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.nodes.post_api_nodes_scenarioname_testcase_enrichermock(
            scenario_name="scenarioName",
            variable_types={
                "amount": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
                "name": MapTypingResultInJsonValue_TypedClass(
                    ref_clazz_name="refClazzName",
                ),
            },
            enricher=GenerateEnricherMockRequestDtoEnricher(
                id="99ae6a31-a55d-4d52-89af-58f471e7143d",
                output="out",
                service=ServiceRef(
                    id="paramService",
                    parameters=[
                        Parameter(
                            name="param",
                            expression=Expression(
                                language="spel",
                                expression="#input.id",
                            ),
                        )
                    ],
                ),
                type="Enricher",
            ),
        )
        """
        _response = self._raw_client.post_api_nodes_scenarioname_testcase_enrichermock(
            scenario_name, variable_types=variable_types, enricher=enricher, request_options=request_options
        )
        return _response.data


class AsyncNodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodesClient
        """
        return self._raw_client

    async def post_api_nodes_scenarioname_additionalinfo(
        self, scenario_name: str, *, request: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AdditionalInfo]:
        """
        Parameters
        ----------
        scenario_name : str

        request : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AdditionalInfo]


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Expression,
            NodeData_Enricher,
            Parameter,
            ServiceRef,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_nodes_scenarioname_additionalinfo(
                scenario_name="scenarioName",
                request=NodeData_Enricher(
                    id="99ae6a31-a55d-4d52-89af-58f471e7143d",
                    output="out",
                    service=ServiceRef(
                        id="paramService",
                        parameters=[
                            Parameter(
                                name="id",
                                expression=Expression(
                                    language="spel",
                                    expression="'a'",
                                ),
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_nodes_scenarioname_additionalinfo(
            scenario_name, request=request, request_options=request_options
        )
        return _response.data

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
    ) -> NodeValidationResultDto:
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
        NodeValidationResultDto


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Expression,
            MapTypingResultInJsonValue_TypedClass,
            NodeData_Filter,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_nodes_scenarioname_validation(
                scenario_name="scenarioName",
                node_data=NodeData_Filter(
                    expression=Expression(
                        language="spel",
                        expression="#longValue > 1",
                    ),
                    id="99ae6a31-a55d-4d52-89af-58f471e7143d",
                ),
                variable_types={
                    "existButString": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                    "longValue": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_nodes_scenarioname_validation(
            scenario_name,
            node_data=node_data,
            variable_types=variable_types,
            branch_variable_types=branch_variable_types,
            outgoing_edges=outgoing_edges,
            test_cases=test_cases,
            request_options=request_options,
        )
        return _response.data

    async def post_api_parameters_processingtype_suggestions(
        self,
        processing_type: str,
        *,
        expression: Expression,
        caret_position2d: CaretPosition2D,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ExpressionSuggestionDto]:
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
        typing.List[ExpressionSuggestionDto]


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CaretPosition2D,
            Expression,
            MapTypingResultInJsonValue_TypedObjectTypingResult,
            TypingResult_TypedClass,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_parameters_processingtype_suggestions(
                processing_type="processingType",
                expression=Expression(
                    language="spel",
                    expression="#inpu",
                ),
                caret_position2d=CaretPosition2D(
                    row=0,
                    column=5,
                ),
                variable_types={
                    "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
                        fields={
                            "key": TypingResult_TypedClass(
                                ref_clazz_name="refClazzName",
                            )
                        },
                        ref_clazz_name="refClazzName",
                    )
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_parameters_processingtype_suggestions(
            processing_type,
            expression=expression,
            caret_position2d=caret_position2d,
            variable_types=variable_types,
            request_options=request_options,
        )
        return _response.data

    async def post_api_parameters_processingtype_validate(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        parameters: typing.Optional[typing.Sequence[UiValueParameterDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Expression,
            MapTypingResultInJsonValue_TypedObjectTypingResult,
            TypingResult_TypedClass,
            UiValueParameterDto,
            UiValueParameterDtoTyp_TypedClass,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_parameters_processingtype_validate(
                processing_type="processingType",
                parameters=[
                    UiValueParameterDto(
                        name="condition",
                        typ=UiValueParameterDtoTyp_TypedClass(
                            ref_clazz_name="refClazzName",
                        ),
                        expression=Expression(
                            language="spel",
                            expression="#input.amount > 2",
                        ),
                    )
                ],
                variable_types={
                    "input": MapTypingResultInJsonValue_TypedObjectTypingResult(
                        fields={
                            "key": TypingResult_TypedClass(
                                ref_clazz_name="refClazzName",
                            )
                        },
                        ref_clazz_name="refClazzName",
                    )
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_parameters_processingtype_validate(
            processing_type, variable_types=variable_types, parameters=parameters, request_options=request_options
        )
        return _response.data

    async def post_api_properties_scenarioname_additionalinfo(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AdditionalInfo]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AdditionalInfo]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_properties_scenarioname_additionalinfo(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_properties_scenarioname_additionalinfo(
            scenario_name, request_options=request_options
        )
        return _response.data

    async def post_api_properties_scenarioname_validation(
        self,
        scenario_name: str,
        *,
        additional_fields: ProcessAdditionalFields,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodeValidationResultDto:
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
        NodeValidationResultDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProcessAdditionalFields

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_properties_scenarioname_validation(
                scenario_name="scenarioName",
                additional_fields=ProcessAdditionalFields(
                    properties={
                        "parallelism": "",
                        "checkpointIntervalInSeconds": "",
                        "numberOfThreads": "2",
                        "spillStateToDisk": "true",
                        "environment": "test",
                        "useAsyncInterpretation": "",
                    },
                    meta_data_type="StreamMetaData",
                    show_description=False,
                ),
                name="test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_properties_scenarioname_validation(
            scenario_name, additional_fields=additional_fields, name=name, request_options=request_options
        )
        return _response.data

    async def post_api_nodes_scenarioname_records(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Expression, NodeData_Variable

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_nodes_scenarioname_records(
                scenario_name="scenarioName",
                node_data=NodeData_Variable(
                    id="id",
                    operation="SET",
                    var_name="varName",
                    value=Expression(
                        language="language",
                        expression="expression",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_nodes_scenarioname_records(
            scenario_name, node_data=node_data, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_api_parameters_processingtype_testcase_additionalvariables(
        self,
        processing_type: str,
        *,
        variable_types: MapTypingResultInJson,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestCaseAdditionalVariablesResponseDto:
        """
        Parameters
        ----------
        processing_type : str

        variable_types : MapTypingResultInJson

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestCaseAdditionalVariablesResponseDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MapTypingResultInJsonValue_TypedClass

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_parameters_processingtype_testcase_additionalvariables(
                processing_type="processingType",
                variable_types={
                    "amount": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                    "name": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_parameters_processingtype_testcase_additionalvariables(
            processing_type, variable_types=variable_types, request_options=request_options
        )
        return _response.data

    async def post_api_nodes_scenarioname_testcase_enrichermock(
        self,
        scenario_name: str,
        *,
        variable_types: MapTypingResultInJson,
        enricher: GenerateEnricherMockRequestDtoEnricher,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GenerateEnricherMockResponseDto]:
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
        typing.Optional[GenerateEnricherMockResponseDto]


        Examples
        --------
        import asyncio

        from fern.nodes import GenerateEnricherMockRequestDtoEnricher

        from fern import (
            AsyncFernApi,
            Expression,
            MapTypingResultInJsonValue_TypedClass,
            Parameter,
            ServiceRef,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nodes.post_api_nodes_scenarioname_testcase_enrichermock(
                scenario_name="scenarioName",
                variable_types={
                    "amount": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                    "name": MapTypingResultInJsonValue_TypedClass(
                        ref_clazz_name="refClazzName",
                    ),
                },
                enricher=GenerateEnricherMockRequestDtoEnricher(
                    id="99ae6a31-a55d-4d52-89af-58f471e7143d",
                    output="out",
                    service=ServiceRef(
                        id="paramService",
                        parameters=[
                            Parameter(
                                name="param",
                                expression=Expression(
                                    language="spel",
                                    expression="#input.id",
                                ),
                            )
                        ],
                    ),
                    type="Enricher",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_nodes_scenarioname_testcase_enrichermock(
            scenario_name, variable_types=variable_types, enricher=enricher, request_options=request_options
        )
        return _response.data
