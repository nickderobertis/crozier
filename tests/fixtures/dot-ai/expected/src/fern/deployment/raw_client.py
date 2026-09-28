

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.tool_execution_response import ToolExecutionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeploymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ToolExecutionResponse]:
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
        HttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools/recommend",
            method="POST",
            json={
                "stage": stage,
                "intent": intent,
                "final": final,
                "solutionId": solution_id,
                "answers": answers,
                "timeout": timeout,
                "repoUrl": repo_url,
                "targetPath": target_path,
                "branch": branch,
                "pullRequest": pull_request,
                "commitMessage": commit_message,
                "authorName": author_name,
                "authorEmail": author_email,
                "interaction_id": interaction_id,
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
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawDeploymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ToolExecutionResponse]:
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
        AsyncHttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools/recommend",
            method="POST",
            json={
                "stage": stage,
                "intent": intent,
                "final": final,
                "solutionId": solution_id,
                "answers": answers,
                "timeout": timeout,
                "repoUrl": repo_url,
                "targetPath": target_path,
                "branch": branch,
                "pullRequest": pull_request,
                "commitMessage": commit_message,
                "authorName": author_name,
                "authorEmail": author_email,
                "interaction_id": interaction_id,
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
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
