

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawTroubleshootingClient, RawTroubleshootingClient
from .types.remediate_request_max_risk_level import RemediateRequestMaxRiskLevel
from .types.remediate_request_mode import RemediateRequestMode


OMIT = typing.cast(typing.Any, ...)


class TroubleshootingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTroubleshootingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTroubleshootingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTroubleshootingClient
        """
        return self._raw_client

    def execute_remediate_tool(
        self,
        *,
        mode: RemediateRequestMode,
        confidence_threshold: float,
        max_risk_level: RemediateRequestMaxRiskLevel,
        issue: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        executed_commands: typing.Optional[typing.Sequence[str]] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        AI-powered Kubernetes issue analysis that provides root cause identification and actionable remediation steps. Unlike basic kubectl commands, this tool performs multi-step investigation, correlates cluster data, and generates intelligent solutions. Use when users want to understand WHY something is broken, not just see raw status. Ideal for: troubleshooting failures, diagnosing performance issues, analyzing pod problems, investigating networking/storage issues, or any "what's wrong" questions.

        Parameters
        ----------
        mode : RemediateRequestMode
            Execution mode: manual requires user approval, automatic executes based on thresholds

        confidence_threshold : float
            For automatic mode: minimum confidence required for execution (default: 0.8)

        max_risk_level : RemediateRequestMaxRiskLevel
            For automatic mode: maximum risk level allowed for execution (default: low)

        issue : typing.Optional[str]
            What the operator is asking for, in their own words. This is the authoritative instruction for the investigation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `issue` alone, which behaves exactly as it always has.

        execute_choice : typing.Optional[float]
            Execute a previously generated choice (1=Execute via MCP, 2=Execute via agent)

        session_id : typing.Optional[str]
            Session ID from previous remediate call when executing a choice

        executed_commands : typing.Optional[typing.Sequence[str]]
            Commands that were executed to remediate the issue

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
        client.troubleshooting.execute_remediate_tool(
            issue="example issue",
            evidence="example evidence",
            mode="manual",
            confidence_threshold=42.0,
            max_risk_level="low",
            execute_choice=42.0,
            session_id="example sessionId",
            executed_commands=["example item"],
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_remediate_tool(
            mode=mode,
            confidence_threshold=confidence_threshold,
            max_risk_level=max_risk_level,
            issue=issue,
            evidence=evidence,
            execute_choice=execute_choice,
            session_id=session_id,
            executed_commands=executed_commands,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data


class AsyncTroubleshootingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTroubleshootingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTroubleshootingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTroubleshootingClient
        """
        return self._raw_client

    async def execute_remediate_tool(
        self,
        *,
        mode: RemediateRequestMode,
        confidence_threshold: float,
        max_risk_level: RemediateRequestMaxRiskLevel,
        issue: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        executed_commands: typing.Optional[typing.Sequence[str]] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        AI-powered Kubernetes issue analysis that provides root cause identification and actionable remediation steps. Unlike basic kubectl commands, this tool performs multi-step investigation, correlates cluster data, and generates intelligent solutions. Use when users want to understand WHY something is broken, not just see raw status. Ideal for: troubleshooting failures, diagnosing performance issues, analyzing pod problems, investigating networking/storage issues, or any "what's wrong" questions.

        Parameters
        ----------
        mode : RemediateRequestMode
            Execution mode: manual requires user approval, automatic executes based on thresholds

        confidence_threshold : float
            For automatic mode: minimum confidence required for execution (default: 0.8)

        max_risk_level : RemediateRequestMaxRiskLevel
            For automatic mode: maximum risk level allowed for execution (default: low)

        issue : typing.Optional[str]
            What the operator is asking for, in their own words. This is the authoritative instruction for the investigation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `issue` alone, which behaves exactly as it always has.

        execute_choice : typing.Optional[float]
            Execute a previously generated choice (1=Execute via MCP, 2=Execute via agent)

        session_id : typing.Optional[str]
            Session ID from previous remediate call when executing a choice

        executed_commands : typing.Optional[typing.Sequence[str]]
            Commands that were executed to remediate the issue

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
            await client.troubleshooting.execute_remediate_tool(
                issue="example issue",
                evidence="example evidence",
                mode="manual",
                confidence_threshold=42.0,
                max_risk_level="low",
                execute_choice=42.0,
                session_id="example sessionId",
                executed_commands=["example item"],
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_remediate_tool(
            mode=mode,
            confidence_threshold=confidence_threshold,
            max_risk_level=max_risk_level,
            issue=issue,
            evidence=evidence,
            execute_choice=execute_choice,
            session_id=session_id,
            executed_commands=executed_commands,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data
