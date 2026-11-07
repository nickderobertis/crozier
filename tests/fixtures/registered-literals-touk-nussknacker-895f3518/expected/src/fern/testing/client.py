

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.node_data import NodeData
from ..types.parameters_validation_result_dto import ParametersValidationResultDto
from ..types.results_with_counts_dto import ResultsWithCountsDto
from ..types.scenario_test_capabilities import ScenarioTestCapabilities
from ..types.scenario_test_data import ScenarioTestData
from ..types.source_test_capabilities import SourceTestCapabilities
from ..types.test_case import TestCase
from ..types.test_case_result_event import TestCaseResultEvent
from ..types.test_source_parameters import TestSourceParameters
from .raw_client import AsyncRawTestingClient, RawTestingClient


OMIT = typing.cast(typing.Any, ...)


class TestingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestingClient
        """
        return self._raw_client

    def post_api_scenariotesting_scenarioname_performmultipletestcases(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_cases: typing.Sequence[TestCase],
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[TestCaseResultEvent]:
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
        typing.Iterator[TestCaseResultEvent]


        Examples
        --------
        from fern import (
            EnricherMock,
            Expression,
            ExpressionAssertion,
            FernApi,
            TestCase,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.testing.post_api_scenariotesting_scenarioname_performmultipletestcases(
            scenario_name="scenarioName",
            scenario_graph={"key": "value"},
            test_cases=[
                TestCase(
                    id="id",
                    name="name",
                    inputs="inputs",
                    mocks={
                        "key": EnricherMock(
                            expression=Expression(
                                language="language",
                                expression="expression",
                            ),
                            enabled=True,
                        )
                    },
                    assertions={
                        "key": [
                            ExpressionAssertion(
                                expression=Expression(
                                    language="language",
                                    expression="expression",
                                ),
                            )
                        ]
                    },
                )
            ],
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.post_api_scenariotesting_scenarioname_performmultipletestcases(
            scenario_name,
            scenario_graph=scenario_graph,
            test_cases=test_cases,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        ) as r:
            yield from r.data

    def post_api_scenariotesting_scenarioname_capabilities(
        self,
        scenario_name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScenarioTestCapabilities:
        """
        Parameters
        ----------
        scenario_name : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioTestCapabilities


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_capabilities(
            scenario_name="scenarioName",
            request={
                "properties": {
                    "additionalFields": {
                        "properties": {
                            "parallelism": "",
                            "spillStateToDisk": "true",
                            "useAsyncInterpretation": "",
                            "checkpointIntervalInSeconds": "",
                        },
                        "metaDataType": "StreamMetaData",
                        "showDescription": False,
                    }
                }
            },
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_capabilities(
            scenario_name, request=request, request_options=request_options
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_performtestcase(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_case: TestCase,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResultsWithCountsDto:
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
        ResultsWithCountsDto


        Examples
        --------
        from fern import (
            EnricherMock,
            Expression,
            ExpressionAssertion,
            FernApi,
            TestCase,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_performtestcase(
            scenario_name="scenarioName",
            scenario_graph={"key": "value"},
            test_case=TestCase(
                id="id",
                name="name",
                inputs="inputs",
                mocks={
                    "key": EnricherMock(
                        expression=Expression(
                            language="language",
                            expression="expression",
                        ),
                        enabled=True,
                    )
                },
                assertions={
                    "key": [
                        ExpressionAssertion(
                            expression=Expression(
                                language="language",
                                expression="expression",
                            ),
                        )
                    ]
                },
            ),
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_performtestcase(
            scenario_name,
            scenario_graph=scenario_graph,
            test_case=test_case,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_performtest(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResultsWithCountsDto:
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
        ResultsWithCountsDto


        Examples
        --------
        from fern import FernApi, WithLiveData

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_performtest(
            scenario_name="scenarioName",
            scenario_graph={"key": "value"},
            test_data=WithLiveData(
                number_of_samples=1,
            ),
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_performtest(
            scenario_name,
            scenario_graph=scenario_graph,
            test_data=test_data,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_generatedtestdata(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        number_of_samples: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_generatedtestdata(
            scenario_name="scenarioName",
            scenario_graph={"scenarioGraph": {"key": "value"}},
            number_of_samples=1,
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_generatedtestdata(
            scenario_name,
            scenario_graph=scenario_graph,
            number_of_samples=number_of_samples,
            request_options=request_options,
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_validate(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        from fern import Expression, FernApi, TestSourceParameters, WithParameters

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_validate(
            scenario_name="scenarioName",
            scenario_graph={
                "properties": {
                    "additionalFields": {
                        "properties": {
                            "parallelism": "",
                            "spillStateToDisk": "true",
                            "useAsyncInterpretation": "",
                            "checkpointIntervalInSeconds": "",
                        },
                        "metaDataType": "StreamMetaData",
                        "showDescription": False,
                    }
                }
            },
            test_data=WithParameters(
                source_parameters=TestSourceParameters(
                    source_id="source",
                    parameter_expressions={
                        "name": Expression(
                            language="spel",
                            expression="'Amadeus'",
                        )
                    },
                ),
            ),
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_validate(
            scenario_name, scenario_graph=scenario_graph, test_data=test_data, request_options=request_options
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_sourcecapabilities(
        self, scenario_name: str, *, node_data: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceTestCapabilities:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceTestCapabilities


        Examples
        --------
        from fern import (
            Expression,
            FernApi,
            NodeData_Variable,
            VariableOperationSchemaType,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_sourcecapabilities(
            scenario_name="scenarioName",
            node_data=NodeData_Variable(
                id="id",
                operation=VariableOperationSchemaType.SET,
                var_name="varName",
                value=Expression(
                    language="language",
                    expression="expression",
                ),
            ),
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_sourcecapabilities(
            scenario_name, node_data=node_data, request_options=request_options
        )
        return _response.data

    def post_api_scenariotesting_scenarioname_sourcevalidate(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        source_parameters: TestSourceParameters,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        from fern import (
            Expression,
            FernApi,
            NodeData_Variable,
            TestSourceParameters,
            VariableOperationSchemaType,
        )

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.testing.post_api_scenariotesting_scenarioname_sourcevalidate(
            scenario_name="scenarioName",
            node_data=NodeData_Variable(
                id="id",
                operation=VariableOperationSchemaType.SET,
                var_name="varName",
                value=Expression(
                    language="language",
                    expression="expression",
                ),
            ),
            source_parameters=TestSourceParameters(
                source_id="sourceId",
                parameter_expressions={
                    "key": Expression(
                        language="language",
                        expression="expression",
                    )
                },
            ),
        )
        """
        _response = self._raw_client.post_api_scenariotesting_scenarioname_sourcevalidate(
            scenario_name, node_data=node_data, source_parameters=source_parameters, request_options=request_options
        )
        return _response.data


class AsyncTestingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestingClient
        """
        return self._raw_client

    async def post_api_scenariotesting_scenarioname_performmultipletestcases(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_cases: typing.Sequence[TestCase],
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[TestCaseResultEvent]:
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
        typing.AsyncIterator[TestCaseResultEvent]


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EnricherMock,
            Expression,
            ExpressionAssertion,
            TestCase,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.testing.post_api_scenariotesting_scenarioname_performmultipletestcases(
                scenario_name="scenarioName",
                scenario_graph={"key": "value"},
                test_cases=[
                    TestCase(
                        id="id",
                        name="name",
                        inputs="inputs",
                        mocks={
                            "key": EnricherMock(
                                expression=Expression(
                                    language="language",
                                    expression="expression",
                                ),
                                enabled=True,
                            )
                        },
                        assertions={
                            "key": [
                                ExpressionAssertion(
                                    expression=Expression(
                                        language="language",
                                        expression="expression",
                                    ),
                                )
                            ]
                        },
                    )
                ],
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.post_api_scenariotesting_scenarioname_performmultipletestcases(
            scenario_name,
            scenario_graph=scenario_graph,
            test_cases=test_cases,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def post_api_scenariotesting_scenarioname_capabilities(
        self,
        scenario_name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScenarioTestCapabilities:
        """
        Parameters
        ----------
        scenario_name : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioTestCapabilities


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
            await client.testing.post_api_scenariotesting_scenarioname_capabilities(
                scenario_name="scenarioName",
                request={
                    "properties": {
                        "additionalFields": {
                            "properties": {
                                "parallelism": "",
                                "spillStateToDisk": "true",
                                "useAsyncInterpretation": "",
                                "checkpointIntervalInSeconds": "",
                            },
                            "metaDataType": "StreamMetaData",
                            "showDescription": False,
                        }
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_capabilities(
            scenario_name, request=request, request_options=request_options
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_performtestcase(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_case: TestCase,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResultsWithCountsDto:
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
        ResultsWithCountsDto


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EnricherMock,
            Expression,
            ExpressionAssertion,
            TestCase,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.testing.post_api_scenariotesting_scenarioname_performtestcase(
                scenario_name="scenarioName",
                scenario_graph={"key": "value"},
                test_case=TestCase(
                    id="id",
                    name="name",
                    inputs="inputs",
                    mocks={
                        "key": EnricherMock(
                            expression=Expression(
                                language="language",
                                expression="expression",
                            ),
                            enabled=True,
                        )
                    },
                    assertions={
                        "key": [
                            ExpressionAssertion(
                                expression=Expression(
                                    language="language",
                                    expression="expression",
                                ),
                            )
                        ]
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_performtestcase(
            scenario_name,
            scenario_graph=scenario_graph,
            test_case=test_case,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_performtest(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        skip_results_per_node: typing.Optional[bool] = None,
        skip_results_per_transition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResultsWithCountsDto:
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
        ResultsWithCountsDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WithLiveData

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.testing.post_api_scenariotesting_scenarioname_performtest(
                scenario_name="scenarioName",
                scenario_graph={"key": "value"},
                test_data=WithLiveData(
                    number_of_samples=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_performtest(
            scenario_name,
            scenario_graph=scenario_graph,
            test_data=test_data,
            skip_results_per_node=skip_results_per_node,
            skip_results_per_transition=skip_results_per_transition,
            request_options=request_options,
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_generatedtestdata(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        number_of_samples: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str


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
            await client.testing.post_api_scenariotesting_scenarioname_generatedtestdata(
                scenario_name="scenarioName",
                scenario_graph={"scenarioGraph": {"key": "value"}},
                number_of_samples=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_generatedtestdata(
            scenario_name,
            scenario_graph=scenario_graph,
            number_of_samples=number_of_samples,
            request_options=request_options,
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_validate(
        self,
        scenario_name: str,
        *,
        scenario_graph: typing.Dict[str, typing.Any],
        test_data: ScenarioTestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Expression, TestSourceParameters, WithParameters

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.testing.post_api_scenariotesting_scenarioname_validate(
                scenario_name="scenarioName",
                scenario_graph={
                    "properties": {
                        "additionalFields": {
                            "properties": {
                                "parallelism": "",
                                "spillStateToDisk": "true",
                                "useAsyncInterpretation": "",
                                "checkpointIntervalInSeconds": "",
                            },
                            "metaDataType": "StreamMetaData",
                            "showDescription": False,
                        }
                    }
                },
                test_data=WithParameters(
                    source_parameters=TestSourceParameters(
                        source_id="source",
                        parameter_expressions={
                            "name": Expression(
                                language="spel",
                                expression="'Amadeus'",
                            )
                        },
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_validate(
            scenario_name, scenario_graph=scenario_graph, test_data=test_data, request_options=request_options
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_sourcecapabilities(
        self, scenario_name: str, *, node_data: NodeData, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceTestCapabilities:
        """
        Parameters
        ----------
        scenario_name : str

        node_data : NodeData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceTestCapabilities


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Expression,
            NodeData_Variable,
            VariableOperationSchemaType,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.testing.post_api_scenariotesting_scenarioname_sourcecapabilities(
                scenario_name="scenarioName",
                node_data=NodeData_Variable(
                    id="id",
                    operation=VariableOperationSchemaType.SET,
                    var_name="varName",
                    value=Expression(
                        language="language",
                        expression="expression",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_sourcecapabilities(
            scenario_name, node_data=node_data, request_options=request_options
        )
        return _response.data

    async def post_api_scenariotesting_scenarioname_sourcevalidate(
        self,
        scenario_name: str,
        *,
        node_data: NodeData,
        source_parameters: TestSourceParameters,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParametersValidationResultDto:
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
        ParametersValidationResultDto


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Expression,
            NodeData_Variable,
            TestSourceParameters,
            VariableOperationSchemaType,
        )

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.testing.post_api_scenariotesting_scenarioname_sourcevalidate(
                scenario_name="scenarioName",
                node_data=NodeData_Variable(
                    id="id",
                    operation=VariableOperationSchemaType.SET,
                    var_name="varName",
                    value=Expression(
                        language="language",
                        expression="expression",
                    ),
                ),
                source_parameters=TestSourceParameters(
                    source_id="sourceId",
                    parameter_expressions={
                        "key": Expression(
                            language="language",
                            expression="expression",
                        )
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_scenariotesting_scenarioname_sourcevalidate(
            scenario_name, node_data=node_data, source_parameters=source_parameters, request_options=request_options
        )
        return _response.data
