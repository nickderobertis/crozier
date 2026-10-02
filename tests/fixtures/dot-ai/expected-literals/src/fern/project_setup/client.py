

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawProjectSetupClient, RawProjectSetupClient
from .types.project_setup_request_step import ProjectSetupRequestStep


OMIT = typing.cast(typing.Any, ...)


class ProjectSetupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectSetupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectSetupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectSetupClient
        """
        return self._raw_client

    def execute_project_setup_tool(
        self,
        *,
        step: typing.Optional[ProjectSetupRequestStep] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        existing_files: typing.Optional[typing.Sequence[str]] = OMIT,
        selected_scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        answers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Setup project, audit repository, or generate repository files. Use this when user wants to: setup project, audit repo, check missing files, create README, add LICENSE, generate CONTRIBUTING.md, add CI/CD workflows, initialize documentation, setup governance files. Analyzes local repositories and generates missing configuration, documentation, and governance files. Does NOT handle Kubernetes deployments - use recommend for those.

        Parameters
        ----------
        step : typing.Optional[ProjectSetupRequestStep]
            Workflow step: "discover" (default) starts new session and returns file list, "reportScan" analyzes scan results, "generateScope" generates all files in a scope. Defaults to "discover" if omitted.

        session_id : typing.Optional[str]
            Session ID from previous step (required for reportScan and generateScope steps)

        existing_files : typing.Optional[typing.Sequence[str]]
            List of files that exist in the repository (required for first reportScan call, optional for subsequent calls with selectedScopes)

        selected_scopes : typing.Optional[typing.Sequence[str]]
            Scopes user chose to setup (e.g., ["readme", "legal", "github-community"]) (required for reportScan step after initial scan)

        scope : typing.Optional[str]
            Scope to generate (e.g., "github-community") (required for generateScope step)

        answers : typing.Optional[typing.Dict[str, typing.Any]]
            Answers to ALL questions for the scope (required for generateScope step)

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
        client.project_setup.execute_project_setup_tool(
            step="discover",
            session_id="example sessionId",
            existing_files=["example item"],
            selected_scopes=["example item"],
            scope="example scope",
            answers={"key": "value"},
        )
        """
        _response = self._raw_client.execute_project_setup_tool(
            step=step,
            session_id=session_id,
            existing_files=existing_files,
            selected_scopes=selected_scopes,
            scope=scope,
            answers=answers,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectSetupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectSetupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectSetupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectSetupClient
        """
        return self._raw_client

    async def execute_project_setup_tool(
        self,
        *,
        step: typing.Optional[ProjectSetupRequestStep] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        existing_files: typing.Optional[typing.Sequence[str]] = OMIT,
        selected_scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        answers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Setup project, audit repository, or generate repository files. Use this when user wants to: setup project, audit repo, check missing files, create README, add LICENSE, generate CONTRIBUTING.md, add CI/CD workflows, initialize documentation, setup governance files. Analyzes local repositories and generates missing configuration, documentation, and governance files. Does NOT handle Kubernetes deployments - use recommend for those.

        Parameters
        ----------
        step : typing.Optional[ProjectSetupRequestStep]
            Workflow step: "discover" (default) starts new session and returns file list, "reportScan" analyzes scan results, "generateScope" generates all files in a scope. Defaults to "discover" if omitted.

        session_id : typing.Optional[str]
            Session ID from previous step (required for reportScan and generateScope steps)

        existing_files : typing.Optional[typing.Sequence[str]]
            List of files that exist in the repository (required for first reportScan call, optional for subsequent calls with selectedScopes)

        selected_scopes : typing.Optional[typing.Sequence[str]]
            Scopes user chose to setup (e.g., ["readme", "legal", "github-community"]) (required for reportScan step after initial scan)

        scope : typing.Optional[str]
            Scope to generate (e.g., "github-community") (required for generateScope step)

        answers : typing.Optional[typing.Dict[str, typing.Any]]
            Answers to ALL questions for the scope (required for generateScope step)

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
            await client.project_setup.execute_project_setup_tool(
                step="discover",
                session_id="example sessionId",
                existing_files=["example item"],
                selected_scopes=["example item"],
                scope="example scope",
                answers={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_project_setup_tool(
            step=step,
            session_id=session_id,
            existing_files=existing_files,
            selected_scopes=selected_scopes,
            scope=scope,
            answers=answers,
            request_options=request_options,
        )
        return _response.data
