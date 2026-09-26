

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawOperationsClient, RawOperationsClient


OMIT = typing.cast(typing.Any, ...)


class OperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOperationsClient
        """
        return self._raw_client

    def execute_operate_tool(
        self,
        *,
        intent: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        refined_intent: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        AI-powered Kubernetes application operations tool for Day 2 operations. Handles updates, scaling, enhancements, rollbacks, and deletions through natural language intents. Analyzes current state, applies organizational patterns and policies, validates changes via dry-run, and executes approved operations safely.

        Parameters
        ----------
        intent : typing.Optional[str]
            What the operator is asking for, in their own words: "update X to Y", "scale Z", "make W HA", etc. This is the authoritative instruction for the operation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `intent` alone, which behaves exactly as it always has.

        session_id : typing.Optional[str]
            Session ID from previous operate call

        execute_choice : typing.Optional[float]
            Execute approved changes (1=execute)

        refined_intent : typing.Optional[str]
            Clarified intent if user wants to provide more details

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
        client.operations.execute_operate_tool(
            intent="deploy web application with PostgreSQL database",
            evidence="example evidence",
            session_id="example sessionId",
            execute_choice=42.0,
            refined_intent="deploy web application with PostgreSQL database",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_operate_tool(
            intent=intent,
            evidence=evidence,
            session_id=session_id,
            execute_choice=execute_choice,
            refined_intent=refined_intent,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data


class AsyncOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOperationsClient
        """
        return self._raw_client

    async def execute_operate_tool(
        self,
        *,
        intent: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        refined_intent: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        AI-powered Kubernetes application operations tool for Day 2 operations. Handles updates, scaling, enhancements, rollbacks, and deletions through natural language intents. Analyzes current state, applies organizational patterns and policies, validates changes via dry-run, and executes approved operations safely.

        Parameters
        ----------
        intent : typing.Optional[str]
            What the operator is asking for, in their own words: "update X to Y", "scale Z", "make W HA", etc. This is the authoritative instruction for the operation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `intent` alone, which behaves exactly as it always has.

        session_id : typing.Optional[str]
            Session ID from previous operate call

        execute_choice : typing.Optional[float]
            Execute approved changes (1=execute)

        refined_intent : typing.Optional[str]
            Clarified intent if user wants to provide more details

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
            await client.operations.execute_operate_tool(
                intent="deploy web application with PostgreSQL database",
                evidence="example evidence",
                session_id="example sessionId",
                execute_choice=42.0,
                refined_intent="deploy web application with PostgreSQL database",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_operate_tool(
            intent=intent,
            evidence=evidence,
            session_id=session_id,
            execute_choice=execute_choice,
            refined_intent=refined_intent,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data
