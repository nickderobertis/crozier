

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
from ..types.pipeline_continue_execution_response import PipelineContinueExecutionResponse
from ..types.pipeline_get_all_pipelines_response import PipelineGetAllPipelinesResponse
from ..types.pipeline_get_by_id_response import PipelineGetByIdResponse
from ..types.pipeline_get_by_number_response import PipelineGetByNumberResponse
from ..types.pipeline_get_configuration_by_id_response import PipelineGetConfigurationByIdResponse
from ..types.pipeline_list_recent_pipelines_response import PipelineListRecentPipelinesResponse
from ..types.pipeline_list_user_pipelines_response import PipelineListUserPipelinesResponse
from ..types.pipeline_list_workflows_response import PipelineListWorkflowsResponse
from ..types.pipeline_trigger_new_pipeline_response import PipelineTriggerNewPipelineResponse
from .types.pipeline_continue_execution_request_parameters_value import PipelineContinueExecutionRequestParametersValue
from .types.pipeline_trigger_new_pipeline_request_parameters_value import (
    PipelineTriggerNewPipelineRequestParametersValue,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPipelineClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listrecentpipelines(
        self,
        *,
        org_slug: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineListRecentPipelinesResponse]:
        """
        Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

        Parameters
        ----------
        org_slug : typing.Optional[str]
            Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        mine : typing.Optional[bool]
            Only include entries created by your user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineListRecentPipelinesResponse]
            A sequence of pipelines.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline",
            method="GET",
            params={
                "org-slug": org_slug,
                "page-token": page_token,
                "mine": mine,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListRecentPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineListRecentPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def continueexecution(
        self,
        *,
        continuation_key: str,
        configuration: str,
        parameters: typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineContinueExecutionResponse]:
        """
        Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.

        Parameters
        ----------
        continuation_key : str
            A pipeline continuation key.

        configuration : str
            A configuration string for the pipeline.

        parameters : typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]]
            An object containing pipeline parameters and their values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineContinueExecutionResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline/continue",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, PipelineContinueExecutionRequestParametersValue],
                    direction="write",
                ),
                "continuation-key": continuation_key,
                "configuration": configuration,
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
                    PipelineContinueExecutionResponse,
                    parse_obj_as(
                        type_=PipelineContinueExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelineGetByIdResponse]:
        """
        Returns a pipeline by the pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineGetByIdResponse]
            A pipeline object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetByIdResponse,
                    parse_obj_as(
                        type_=PipelineGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getconfigurationbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelineGetConfigurationByIdResponse]:
        """
        Returns a pipeline's configuration by ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineGetConfigurationByIdResponse]
            The configuration strings for the pipeline.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetConfigurationByIdResponse,
                    parse_obj_as(
                        type_=PipelineGetConfigurationByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listworkflows(
        self,
        pipeline_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineListWorkflowsResponse]:
        """
        Returns a paginated list of workflows by pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineListWorkflowsResponse]
            A paginated list of workflow objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}/workflow",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListWorkflowsResponse,
                    parse_obj_as(
                        type_=PipelineListWorkflowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getallpipelines(
        self,
        project_slug: str,
        *,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineGetAllPipelinesResponse]:
        """
        Returns all pipelines for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        branch : typing.Optional[str]
            The name of a vcs branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineGetAllPipelinesResponse]
            A sequence of pipelines.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline",
            method="GET",
            params={
                "branch": branch,
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetAllPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineGetAllPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def triggernewpipeline(
        self,
        project_slug: str,
        *,
        parameters: typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]] = OMIT,
        branch: typing.Optional[str] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineTriggerNewPipelineResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]]
            An object containing pipeline parameters and their values.

        branch : typing.Optional[str]
            The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).

        tag : typing.Optional[str]
            The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineTriggerNewPipelineResponse]
            The created pipeline.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue],
                    direction="write",
                ),
                "branch": branch,
                "tag": tag,
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
                    PipelineTriggerNewPipelineResponse,
                    parse_obj_as(
                        type_=PipelineTriggerNewPipelineResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listuserpipelines(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelineListUserPipelinesResponse]:
        """
        Returns a sequence of all pipelines for this project triggered by the user.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineListUserPipelinesResponse]
            A sequence of pipelines.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline/mine",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListUserPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineListUserPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbynumber(
        self, project_slug: str, pipeline_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelineGetByNumberResponse]:
        """
        Returns a pipeline by the pipeline number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        pipeline_number : typing.Any
            The number of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelineGetByNumberResponse]
            A pipeline object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline/{encode_path_param(pipeline_number)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetByNumberResponse,
                    parse_obj_as(
                        type_=PipelineGetByNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPipelineClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listrecentpipelines(
        self,
        *,
        org_slug: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineListRecentPipelinesResponse]:
        """
        Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

        Parameters
        ----------
        org_slug : typing.Optional[str]
            Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        mine : typing.Optional[bool]
            Only include entries created by your user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineListRecentPipelinesResponse]
            A sequence of pipelines.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline",
            method="GET",
            params={
                "org-slug": org_slug,
                "page-token": page_token,
                "mine": mine,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListRecentPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineListRecentPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def continueexecution(
        self,
        *,
        continuation_key: str,
        configuration: str,
        parameters: typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineContinueExecutionResponse]:
        """
        Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.

        Parameters
        ----------
        continuation_key : str
            A pipeline continuation key.

        configuration : str
            A configuration string for the pipeline.

        parameters : typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]]
            An object containing pipeline parameters and their values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineContinueExecutionResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline/continue",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, PipelineContinueExecutionRequestParametersValue],
                    direction="write",
                ),
                "continuation-key": continuation_key,
                "configuration": configuration,
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
                    PipelineContinueExecutionResponse,
                    parse_obj_as(
                        type_=PipelineContinueExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelineGetByIdResponse]:
        """
        Returns a pipeline by the pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineGetByIdResponse]
            A pipeline object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetByIdResponse,
                    parse_obj_as(
                        type_=PipelineGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getconfigurationbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelineGetConfigurationByIdResponse]:
        """
        Returns a pipeline's configuration by ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineGetConfigurationByIdResponse]
            The configuration strings for the pipeline.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetConfigurationByIdResponse,
                    parse_obj_as(
                        type_=PipelineGetConfigurationByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listworkflows(
        self,
        pipeline_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineListWorkflowsResponse]:
        """
        Returns a paginated list of workflows by pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineListWorkflowsResponse]
            A paginated list of workflow objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipeline/{encode_path_param(pipeline_id)}/workflow",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListWorkflowsResponse,
                    parse_obj_as(
                        type_=PipelineListWorkflowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getallpipelines(
        self,
        project_slug: str,
        *,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineGetAllPipelinesResponse]:
        """
        Returns all pipelines for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        branch : typing.Optional[str]
            The name of a vcs branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineGetAllPipelinesResponse]
            A sequence of pipelines.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline",
            method="GET",
            params={
                "branch": branch,
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetAllPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineGetAllPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def triggernewpipeline(
        self,
        project_slug: str,
        *,
        parameters: typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]] = OMIT,
        branch: typing.Optional[str] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineTriggerNewPipelineResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]]
            An object containing pipeline parameters and their values.

        branch : typing.Optional[str]
            The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).

        tag : typing.Optional[str]
            The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineTriggerNewPipelineResponse]
            The created pipeline.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline",
            method="POST",
            json={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue],
                    direction="write",
                ),
                "branch": branch,
                "tag": tag,
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
                    PipelineTriggerNewPipelineResponse,
                    parse_obj_as(
                        type_=PipelineTriggerNewPipelineResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listuserpipelines(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelineListUserPipelinesResponse]:
        """
        Returns a sequence of all pipelines for this project triggered by the user.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineListUserPipelinesResponse]
            A sequence of pipelines.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline/mine",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineListUserPipelinesResponse,
                    parse_obj_as(
                        type_=PipelineListUserPipelinesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbynumber(
        self, project_slug: str, pipeline_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelineGetByNumberResponse]:
        """
        Returns a pipeline by the pipeline number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        pipeline_number : typing.Any
            The number of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelineGetByNumberResponse]
            A pipeline object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/pipeline/{encode_path_param(pipeline_number)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelineGetByNumberResponse,
                    parse_obj_as(
                        type_=PipelineGetByNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
