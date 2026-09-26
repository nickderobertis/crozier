

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
from .types.project_setup_request_step import ProjectSetupRequestStep
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectSetupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ToolExecutionResponse]:
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
        HttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools/projectSetup",
            method="POST",
            json={
                "step": step,
                "sessionId": session_id,
                "existingFiles": existing_files,
                "selectedScopes": selected_scopes,
                "scope": scope,
                "answers": answers,
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


class AsyncRawProjectSetupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ToolExecutionResponse]:
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
        AsyncHttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools/projectSetup",
            method="POST",
            json={
                "step": step,
                "sessionId": session_id,
                "existingFiles": existing_files,
                "selectedScopes": selected_scopes,
                "scope": scope,
                "answers": answers,
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
