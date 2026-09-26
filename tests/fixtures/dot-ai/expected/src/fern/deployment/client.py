

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawDeploymentClient, RawDeploymentClient


OMIT = typing.cast(typing.Any, ...)


class DeploymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeploymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeploymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeploymentClient
        """
        return self._raw_client

    def execute_recommend_tool(
        self,
        *,
        stage: typing.Optional[str] = OMIT,
        intent: typing.Optional[str] = OMIT,
        final: typing.Optional[bool] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        answers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[float] = OMIT,
        repo_url: typing.Optional[str] = OMIT,
        target_path: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        pull_request: typing.Optional[bool] = OMIT,
        commit_message: typing.Optional[str] = OMIT,
        author_name: typing.Optional[str] = OMIT,
        author_email: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Deploy applications, infrastructure, and services using Kubernetes resources with AI recommendations. Supports cloud resources via operators like Crossplane, cluster management via CAPI, and traditional Kubernetes workloads. Describe what you want to deploy. Does NOT handle policy creation, organizational patterns, or resource capabilities - use manageOrgData for those.

        Parameters
        ----------
        stage : typing.Optional[str]
            Deployment workflow stage: "recommend" (default), "chooseSolution", "answerQuestion:required", "answerQuestion:basic", "answerQuestion:advanced", "answerQuestion:open", "generateManifests", "pushToGit", "deployManifests". Defaults to "recommend" if omitted.

        intent : typing.Optional[str]
            What the user wants to deploy, create, setup, install, or run on Kubernetes. Examples: "deploy web application", "create PostgreSQL database", "setup Redis cache", "install Prometheus monitoring", "configure Ingress controller", "provision storage volumes", "launch MongoDB operator", "run Node.js API", "setup CI/CD pipeline", "create load balancer", "install Grafana dashboard", "deploy React frontend"

        final : typing.Optional[bool]
            Set to true to skip intent clarification and proceed directly with recommendations. If false or omitted, the tool will analyze the intent and provide clarification questions to help improve recommendation quality.

        solution_id : typing.Optional[str]
            Solution ID for chooseSolution, answerQuestion, generateManifests, pushToGit, and deployManifests stages

        answers : typing.Optional[typing.Dict[str, typing.Any]]
            User answers for answerQuestion stage

        timeout : typing.Optional[float]
            Deployment timeout in seconds for deployManifests stage

        repo_url : typing.Optional[str]
            Git repository URL for pushToGit stage (HTTPS)

        target_path : typing.Optional[str]
            Path within repository for pushToGit stage (e.g., "apps/postgresql/")

        branch : typing.Optional[str]
            Git branch for pushToGit stage (default: main). With pullRequest: true this is the BASE branch the pull request targets, which is never written to

        pull_request : typing.Optional[bool]
            For pushToGit stage: when true, commit to a server-generated branch and open a pull request against `branch` instead of pushing to it directly. Required for repositories with branch protection. The head branch name is chosen by the server and cannot be supplied

        commit_message : typing.Optional[str]
            Commit message for pushToGit stage (also the pull request title when pullRequest: true)

        author_name : typing.Optional[str]
            Git author name for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)

        author_email : typing.Optional[str]
            Git author email for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)

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
        client.deployment.execute_recommend_tool(
            stage="example stage",
            intent="deploy web application with PostgreSQL database",
            final=False,
            solution_id="example solutionId",
            answers={"key": "value"},
            timeout=30.0,
            repo_url="https://example.com",
            target_path="example targetPath",
            branch="example branch",
            pull_request=False,
            commit_message="example commitMessage",
            author_name="example authorName",
            author_email="user@example.com",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_recommend_tool(
            stage=stage,
            intent=intent,
            final=final,
            solution_id=solution_id,
            answers=answers,
            timeout=timeout,
            repo_url=repo_url,
            target_path=target_path,
            branch=branch,
            pull_request=pull_request,
            commit_message=commit_message,
            author_name=author_name,
            author_email=author_email,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data


class AsyncDeploymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeploymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeploymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeploymentClient
        """
        return self._raw_client

    async def execute_recommend_tool(
        self,
        *,
        stage: typing.Optional[str] = OMIT,
        intent: typing.Optional[str] = OMIT,
        final: typing.Optional[bool] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        answers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[float] = OMIT,
        repo_url: typing.Optional[str] = OMIT,
        target_path: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        pull_request: typing.Optional[bool] = OMIT,
        commit_message: typing.Optional[str] = OMIT,
        author_name: typing.Optional[str] = OMIT,
        author_email: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Deploy applications, infrastructure, and services using Kubernetes resources with AI recommendations. Supports cloud resources via operators like Crossplane, cluster management via CAPI, and traditional Kubernetes workloads. Describe what you want to deploy. Does NOT handle policy creation, organizational patterns, or resource capabilities - use manageOrgData for those.

        Parameters
        ----------
        stage : typing.Optional[str]
            Deployment workflow stage: "recommend" (default), "chooseSolution", "answerQuestion:required", "answerQuestion:basic", "answerQuestion:advanced", "answerQuestion:open", "generateManifests", "pushToGit", "deployManifests". Defaults to "recommend" if omitted.

        intent : typing.Optional[str]
            What the user wants to deploy, create, setup, install, or run on Kubernetes. Examples: "deploy web application", "create PostgreSQL database", "setup Redis cache", "install Prometheus monitoring", "configure Ingress controller", "provision storage volumes", "launch MongoDB operator", "run Node.js API", "setup CI/CD pipeline", "create load balancer", "install Grafana dashboard", "deploy React frontend"

        final : typing.Optional[bool]
            Set to true to skip intent clarification and proceed directly with recommendations. If false or omitted, the tool will analyze the intent and provide clarification questions to help improve recommendation quality.

        solution_id : typing.Optional[str]
            Solution ID for chooseSolution, answerQuestion, generateManifests, pushToGit, and deployManifests stages

        answers : typing.Optional[typing.Dict[str, typing.Any]]
            User answers for answerQuestion stage

        timeout : typing.Optional[float]
            Deployment timeout in seconds for deployManifests stage

        repo_url : typing.Optional[str]
            Git repository URL for pushToGit stage (HTTPS)

        target_path : typing.Optional[str]
            Path within repository for pushToGit stage (e.g., "apps/postgresql/")

        branch : typing.Optional[str]
            Git branch for pushToGit stage (default: main). With pullRequest: true this is the BASE branch the pull request targets, which is never written to

        pull_request : typing.Optional[bool]
            For pushToGit stage: when true, commit to a server-generated branch and open a pull request against `branch` instead of pushing to it directly. Required for repositories with branch protection. The head branch name is chosen by the server and cannot be supplied

        commit_message : typing.Optional[str]
            Commit message for pushToGit stage (also the pull request title when pullRequest: true)

        author_name : typing.Optional[str]
            Git author name for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)

        author_email : typing.Optional[str]
            Git author email for pushToGit stage (ignored when the request carries an authenticated user identity, which is then the commit author)

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
            await client.deployment.execute_recommend_tool(
                stage="example stage",
                intent="deploy web application with PostgreSQL database",
                final=False,
                solution_id="example solutionId",
                answers={"key": "value"},
                timeout=30.0,
                repo_url="https://example.com",
                target_path="example targetPath",
                branch="example branch",
                pull_request=False,
                commit_message="example commitMessage",
                author_name="example authorName",
                author_email="user@example.com",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_recommend_tool(
            stage=stage,
            intent=intent,
            final=final,
            solution_id=solution_id,
            answers=answers,
            timeout=timeout,
            repo_url=repo_url,
            target_path=target_path,
            branch=branch,
            pull_request=pull_request,
            commit_message=commit_message,
            author_name=author_name,
            author_email=author_email,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data
