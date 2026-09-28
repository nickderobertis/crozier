

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawIntelligenceClient, RawIntelligenceClient


OMIT = typing.cast(typing.Any, ...)


class IntelligenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntelligenceClient
        """
        return self._raw_client

    def execute_impact_analysis_tool(
        self,
        *,
        input: str,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Analyze the blast radius of a proposed Kubernetes operation. Accepts free-text input: kubectl commands (e.g., "kubectl delete pvc data-postgres-0 -n production"), YAML manifests, or plain-English descriptions (e.g., "what happens if I delete the postgres database?"). Returns whether the operation is safe and a detailed dependency analysis with confidence levels.

        Parameters
        ----------
        input : str
            The operation to analyze. Accepts kubectl commands, YAML manifests, or plain-English descriptions.

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.intelligence.execute_impact_analysis_tool(
            input="example input",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_impact_analysis_tool(
            input=input, interaction_id=interaction_id, request_options=request_options
        )
        return _response.data

    def execute_query_tool(
        self,
        *,
        intent: str,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Natural language query interface for Kubernetes cluster intelligence. Ask any questions about your cluster resources, capabilities, and status in plain English. Examples: "What databases are running?", "Describe the nginx deployment", "Show me pods in the kube-system namespace", "What operators are installed?", "Is my-postgres healthy?"

        Parameters
        ----------
        intent : str
            Natural language query about the cluster

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.intelligence.execute_query_tool(
            intent="deploy web application with PostgreSQL database",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_query_tool(
            intent=intent, interaction_id=interaction_id, request_options=request_options
        )
        return _response.data


class AsyncIntelligenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntelligenceClient
        """
        return self._raw_client

    async def execute_impact_analysis_tool(
        self,
        *,
        input: str,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Analyze the blast radius of a proposed Kubernetes operation. Accepts free-text input: kubectl commands (e.g., "kubectl delete pvc data-postgres-0 -n production"), YAML manifests, or plain-English descriptions (e.g., "what happens if I delete the postgres database?"). Returns whether the operation is safe and a detailed dependency analysis with confidence levels.

        Parameters
        ----------
        input : str
            The operation to analyze. Accepts kubectl commands, YAML manifests, or plain-English descriptions.

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.intelligence.execute_impact_analysis_tool(
                input="example input",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_impact_analysis_tool(
            input=input, interaction_id=interaction_id, request_options=request_options
        )
        return _response.data

    async def execute_query_tool(
        self,
        *,
        intent: str,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Natural language query interface for Kubernetes cluster intelligence. Ask any questions about your cluster resources, capabilities, and status in plain English. Examples: "What databases are running?", "Describe the nginx deployment", "Show me pods in the kube-system namespace", "What operators are installed?", "Is my-postgres healthy?"

        Parameters
        ----------
        intent : str
            Natural language query about the cluster

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.intelligence.execute_query_tool(
                intent="deploy web application with PostgreSQL database",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_query_tool(
            intent=intent, interaction_id=interaction_id, request_options=request_options
        )
        return _response.data
