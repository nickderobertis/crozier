

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.not_found_error import NotFoundError
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.artifact import Artifact
from .types.browser_session_response import BrowserSessionResponse
from .types.create_credential_request_credential import CreateCredentialRequestCredential
from .types.credential_response import CredentialResponse
from .types.credential_type import CredentialType
from .types.get_run_response import GetRunResponse
from .types.proxy_location import ProxyLocation
from .types.run_engine import RunEngine
from .types.task_run_request_data_extraction_schema import TaskRunRequestDataExtractionSchema
from .types.task_run_response import TaskRunResponse
from .types.totp_code import TotpCode
from .types.workflow import Workflow
from .types.workflow_create_yaml_request import WorkflowCreateYamlRequest
from .types.workflow_run_response import WorkflowRunResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_task(
        self,
        *,
        prompt: str,
        user_agent: typing.Optional[str] = None,
        url: typing.Optional[str] = OMIT,
        engine: typing.Optional[RunEngine] = OMIT,
        title: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        data_extraction_schema: typing.Optional[TaskRunRequestDataExtractionSchema] = OMIT,
        error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        model: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        publish_workflow: typing.Optional[bool] = OMIT,
        include_action_history_in_verification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskRunResponse]:
        """
        Run a task

        Parameters
        ----------
        prompt : str

            The goal or task description for Skyvern to accomplish

        user_agent : typing.Optional[str]

        url : typing.Optional[str]

            The starting URL for the task. If not provided, Skyvern will attempt to determine an appropriate URL

        engine : typing.Optional[RunEngine]

            The engine that powers the agent task. The default value is `skyvern-2.0`, the latest Skyvern agent that performs pretty well with complex and multi-step tasks. `skyvern-1.0` is good for simple tasks like filling a form, or searching for information on Google. The `openai-cua` engine uses OpenAI's CUA model. The `anthropic-cua` uses Anthropic's Claude Sonnet 3.7 model with the computer use tool.

        title : typing.Optional[str]
            The title for the task

        proxy_location : typing.Optional[ProxyLocation]

            Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

            Available geotargeting options:
            - RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
            - RESIDENTIAL_ES: Spain
            - RESIDENTIAL_IE: Ireland
            - RESIDENTIAL_GB: United Kingdom
            - RESIDENTIAL_IN: India
            - RESIDENTIAL_JP: Japan
            - RESIDENTIAL_FR: France
            - RESIDENTIAL_DE: Germany
            - RESIDENTIAL_NZ: New Zealand
            - RESIDENTIAL_ZA: South Africa
            - RESIDENTIAL_AR: Argentina
            - RESIDENTIAL_ISP: ISP proxy
            - US-CA: California
            - US-NY: New York
            - US-TX: Texas
            - US-FL: Florida
            - US-WA: Washington
            - NONE: No proxy

        data_extraction_schema : typing.Optional[TaskRunRequestDataExtractionSchema]

            The schema for data to be extracted from the webpage. If you're looking for consistent data schema being returned by the agent, it's highly recommended to use https://json-schema.org/.

        error_code_mapping : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Custom mapping of error codes to error messages if Skyvern encounters an error.

        max_steps : typing.Optional[int]

            Maximum number of steps the task can take. Task will fail if it exceeds this number. Cautions: you are charged per step so please set this number to a reasonable value. Contact sales@skyvern.com for custom pricing.

        webhook_url : typing.Optional[str]

            URL to send task status updates to after a run is finished. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        browser_session_id : typing.Optional[str]

            Run the task or workflow in the specific Skyvern browser session. Having a browser session can persist the real-time state of the browser, so that the next run can continue from where the previous run left off.

        model : typing.Optional[typing.Dict[str, typing.Any]]

            Optional model configuration.

        publish_workflow : typing.Optional[bool]
            Whether to publish this task as a reusable workflow. Only available for skyvern-2.0.

        include_action_history_in_verification : typing.Optional[bool]
            Whether to include action history when verifying that the task is complete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskRunResponse]
            Successfully run task
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/run/tasks",
            method="POST",
            json={
                "prompt": prompt,
                "url": url,
                "engine": engine,
                "title": title,
                "proxy_location": proxy_location,
                "data_extraction_schema": convert_and_respect_annotation_metadata(
                    object_=data_extraction_schema,
                    annotation=typing.Optional[TaskRunRequestDataExtractionSchema],
                    direction="write",
                ),
                "error_code_mapping": error_code_mapping,
                "max_steps": max_steps,
                "webhook_url": webhook_url,
                "totp_identifier": totp_identifier,
                "totp_url": totp_url,
                "browser_session_id": browser_session_id,
                "model": model,
                "publish_workflow": publish_workflow,
                "include_action_history_in_verification": include_action_history_in_verification,
            },
            headers={
                "content-type": "application/json",
                "x-user-agent": str(user_agent) if user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskRunResponse,
                    parse_obj_as(
                        type_=TaskRunResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def run_workflow(
        self,
        *,
        workflow_id: str,
        template: typing.Optional[bool] = None,
        max_steps_override: typing.Optional[int] = None,
        user_agent: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        title: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowRunResponse]:
        """
        Run a workflow

        Parameters
        ----------
        workflow_id : str
            ID of the workflow to run. Workflow ID starts with `wpid_`.

        template : typing.Optional[bool]

        max_steps_override : typing.Optional[int]

        user_agent : typing.Optional[str]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Parameters to pass to the workflow

        title : typing.Optional[str]
            The title for this workflow run

        proxy_location : typing.Optional[ProxyLocation]

            Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

            Available geotargeting options:
            - RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
            - RESIDENTIAL_ES: Spain
            - RESIDENTIAL_IE: Ireland
            - RESIDENTIAL_GB: United Kingdom
            - RESIDENTIAL_IN: India
            - RESIDENTIAL_JP: Japan
            - RESIDENTIAL_FR: France
            - RESIDENTIAL_DE: Germany
            - RESIDENTIAL_NZ: New Zealand
            - RESIDENTIAL_ZA: South Africa
            - RESIDENTIAL_AR: Argentina
            - RESIDENTIAL_ISP: ISP proxy
            - US-CA: California
            - US-NY: New York
            - US-TX: Texas
            - US-FL: Florida
            - US-WA: Washington
            - NONE: No proxy

        webhook_url : typing.Optional[str]
            URL to send workflow status updates to after a run is finished. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for webhook questions.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        browser_session_id : typing.Optional[str]
            ID of a Skyvern browser session to reuse, having it continue from the current screen state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowRunResponse]
            Successfully run workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/run/workflows",
            method="POST",
            params={
                "template": template,
            },
            json={
                "workflow_id": workflow_id,
                "parameters": parameters,
                "title": title,
                "proxy_location": proxy_location,
                "webhook_url": webhook_url,
                "totp_url": totp_url,
                "totp_identifier": totp_identifier,
                "browser_session_id": browser_session_id,
            },
            headers={
                "content-type": "application/json",
                "x-max-steps-override": str(max_steps_override) if max_steps_override is not None else None,
                "x-user-agent": str(user_agent) if user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowRunResponse,
                    parse_obj_as(
                        type_=WorkflowRunResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRunResponse]:
        """
        Get run information (task run, workflow run)

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRunResponse]
            Successfully got run
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRunResponse,
                    parse_obj_as(
                        type_=GetRunResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def cancel_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Cancel a run (task or workflow)

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_workflows(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        only_saved_tasks: typing.Optional[bool] = None,
        only_workflows: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        template: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Workflow]]:
        """
        Get all workflows with the latest version for the organization.

        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        only_saved_tasks : typing.Optional[bool]

        only_workflows : typing.Optional[bool]

        title : typing.Optional[str]

        template : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Workflow]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "only_saved_tasks": only_saved_tasks,
                "only_workflows": only_workflows,
                "title": title,
                "template": template,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Workflow],
                    parse_obj_as(
                        type_=typing.List[Workflow],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def create_workflow(
        self,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Workflow]:
        """
        Create a new workflow

        Parameters
        ----------
        json_definition : typing.Optional[WorkflowCreateYamlRequest]
            Workflow definition in JSON format

        yaml_definition : typing.Optional[str]
            Workflow definition in YAML format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Workflow]
            Successfully created workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="POST",
            json={
                "json_definition": convert_and_respect_annotation_metadata(
                    object_=json_definition, annotation=typing.Optional[WorkflowCreateYamlRequest], direction="write"
                ),
                "yaml_definition": yaml_definition,
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
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def update_workflow(
        self,
        workflow_id: str,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Workflow]:
        """
        Update a workflow

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow to update. Workflow ID starts with `wpid_`.

        json_definition : typing.Optional[WorkflowCreateYamlRequest]
            Workflow definition in JSON format

        yaml_definition : typing.Optional[str]
            Workflow definition in YAML format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Workflow]
            Successfully updated workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}",
            method="POST",
            json={
                "json_definition": convert_and_respect_annotation_metadata(
                    object_=json_definition, annotation=typing.Optional[WorkflowCreateYamlRequest], direction="write"
                ),
                "yaml_definition": yaml_definition,
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
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_workflow(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a workflow

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow to delete. Workflow ID starts with `wpid_`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successfully deleted workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Artifact]:
        """
        Get an artifact

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Artifact]
            Successfully retrieved artifact
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artifacts/{encode_path_param(artifact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Artifact,
                    parse_obj_as(
                        type_=Artifact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def retry_run_webhook(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Retry sending the webhook for a run

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/retry_webhook",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_browser_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[BrowserSessionResponse]]:
        """
        Get all active browser sessions for the organization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BrowserSessionResponse]]
            Successfully retrieved all active browser sessions
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/browser_sessions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BrowserSessionResponse],
                    parse_obj_as(
                        type_=typing.List[BrowserSessionResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def create_browser_session(
        self, *, timeout: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BrowserSessionResponse]:
        """
        Create a new browser session

        Parameters
        ----------
        timeout : typing.Optional[int]
            Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 10080. Defaults to 60.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BrowserSessionResponse]
            Successfully created browser session
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/browser_sessions",
            method="POST",
            json={
                "timeout": timeout,
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
                    BrowserSessionResponse,
                    parse_obj_as(
                        type_=BrowserSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def close_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Close a browser session

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session to close. completed_at will be set when the browser session is closed. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successfully closed browser session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/browser_sessions/{encode_path_param(browser_session_id)}/close",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BrowserSessionResponse]:
        """
        Get details about a specific browser session by ID

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BrowserSessionResponse]
            Successfully retrieved browser session details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/browser_sessions/{encode_path_param(browser_session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserSessionResponse,
                    parse_obj_as(
                        type_=BrowserSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def send_totp_code(
        self,
        *,
        totp_identifier: str,
        content: str,
        task_id: typing.Optional[str] = OMIT,
        workflow_id: typing.Optional[str] = OMIT,
        workflow_run_id: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        expired_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TotpCode]:
        """
        Forward a TOTP (2FA, MFA) email or sms message containing the code to Skyvern. This endpoint stores the code in database so that Skyvern can use it while running tasks/workflows.

        Parameters
        ----------
        totp_identifier : str
            The identifier of the TOTP code. It can be the email address, phone number, or the identifier of the user.

        content : str
            The content of the TOTP code. It can be the email content that contains the TOTP code, or the sms message that contains the TOTP code. Skyvern will automatically extract the TOTP code from the content.

        task_id : typing.Optional[str]
            The task_id the totp code is for. It can be the task_id of the task that the TOTP code is for.

        workflow_id : typing.Optional[str]
            The workflow ID the TOTP code is for. It can be the workflow ID of the workflow that the TOTP code is for.

        workflow_run_id : typing.Optional[str]
            The workflow run id that the TOTP code is for. It can be the workflow run id of the workflow run that the TOTP code is for.

        source : typing.Optional[str]
            An optional field. The source of the TOTP code. e.g. email, sms, etc.

        expired_at : typing.Optional[dt.datetime]
            The timestamp when the TOTP code expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TotpCode]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/credentials/totp",
            method="POST",
            json={
                "totp_identifier": totp_identifier,
                "task_id": task_id,
                "workflow_id": workflow_id,
                "workflow_run_id": workflow_run_id,
                "source": source,
                "content": content,
                "expired_at": expired_at,
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
                    TotpCode,
                    parse_obj_as(
                        type_=TotpCode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_credentials(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CredentialResponse]]:
        """
        Retrieves a paginated list of credentials for the current organization

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CredentialResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/credentials",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CredentialResponse],
                    parse_obj_as(
                        type_=typing.List[CredentialResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def create_credential(
        self,
        *,
        name: str,
        credential_type: CredentialType,
        credential: CreateCredentialRequestCredential,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CredentialResponse]:
        """
        Creates a new credential for the current organization

        Parameters
        ----------
        name : str
            Name of the credential

        credential_type : CredentialType
            Type of credential to create

        credential : CreateCredentialRequestCredential
            The credential data to store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/credentials",
            method="POST",
            json={
                "name": name,
                "credential_type": credential_type,
                "credential": convert_and_respect_annotation_metadata(
                    object_=credential, annotation=CreateCredentialRequestCredential, direction="write"
                ),
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a specific credential by its ID

        Parameters
        ----------
        credential_id : str
            The unique identifier of the credential to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/credentials/{encode_path_param(credential_id)}/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CredentialResponse]:
        """
        Retrieves a specific credential by its ID

        Parameters
        ----------
        credential_id : str
            The unique identifier of the credential

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/credentials/{encode_path_param(credential_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_task(
        self,
        *,
        prompt: str,
        user_agent: typing.Optional[str] = None,
        url: typing.Optional[str] = OMIT,
        engine: typing.Optional[RunEngine] = OMIT,
        title: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        data_extraction_schema: typing.Optional[TaskRunRequestDataExtractionSchema] = OMIT,
        error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        model: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        publish_workflow: typing.Optional[bool] = OMIT,
        include_action_history_in_verification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskRunResponse]:
        """
        Run a task

        Parameters
        ----------
        prompt : str

            The goal or task description for Skyvern to accomplish

        user_agent : typing.Optional[str]

        url : typing.Optional[str]

            The starting URL for the task. If not provided, Skyvern will attempt to determine an appropriate URL

        engine : typing.Optional[RunEngine]

            The engine that powers the agent task. The default value is `skyvern-2.0`, the latest Skyvern agent that performs pretty well with complex and multi-step tasks. `skyvern-1.0` is good for simple tasks like filling a form, or searching for information on Google. The `openai-cua` engine uses OpenAI's CUA model. The `anthropic-cua` uses Anthropic's Claude Sonnet 3.7 model with the computer use tool.

        title : typing.Optional[str]
            The title for the task

        proxy_location : typing.Optional[ProxyLocation]

            Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

            Available geotargeting options:
            - RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
            - RESIDENTIAL_ES: Spain
            - RESIDENTIAL_IE: Ireland
            - RESIDENTIAL_GB: United Kingdom
            - RESIDENTIAL_IN: India
            - RESIDENTIAL_JP: Japan
            - RESIDENTIAL_FR: France
            - RESIDENTIAL_DE: Germany
            - RESIDENTIAL_NZ: New Zealand
            - RESIDENTIAL_ZA: South Africa
            - RESIDENTIAL_AR: Argentina
            - RESIDENTIAL_ISP: ISP proxy
            - US-CA: California
            - US-NY: New York
            - US-TX: Texas
            - US-FL: Florida
            - US-WA: Washington
            - NONE: No proxy

        data_extraction_schema : typing.Optional[TaskRunRequestDataExtractionSchema]

            The schema for data to be extracted from the webpage. If you're looking for consistent data schema being returned by the agent, it's highly recommended to use https://json-schema.org/.

        error_code_mapping : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Custom mapping of error codes to error messages if Skyvern encounters an error.

        max_steps : typing.Optional[int]

            Maximum number of steps the task can take. Task will fail if it exceeds this number. Cautions: you are charged per step so please set this number to a reasonable value. Contact sales@skyvern.com for custom pricing.

        webhook_url : typing.Optional[str]

            URL to send task status updates to after a run is finished. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        browser_session_id : typing.Optional[str]

            Run the task or workflow in the specific Skyvern browser session. Having a browser session can persist the real-time state of the browser, so that the next run can continue from where the previous run left off.

        model : typing.Optional[typing.Dict[str, typing.Any]]

            Optional model configuration.

        publish_workflow : typing.Optional[bool]
            Whether to publish this task as a reusable workflow. Only available for skyvern-2.0.

        include_action_history_in_verification : typing.Optional[bool]
            Whether to include action history when verifying that the task is complete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskRunResponse]
            Successfully run task
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/run/tasks",
            method="POST",
            json={
                "prompt": prompt,
                "url": url,
                "engine": engine,
                "title": title,
                "proxy_location": proxy_location,
                "data_extraction_schema": convert_and_respect_annotation_metadata(
                    object_=data_extraction_schema,
                    annotation=typing.Optional[TaskRunRequestDataExtractionSchema],
                    direction="write",
                ),
                "error_code_mapping": error_code_mapping,
                "max_steps": max_steps,
                "webhook_url": webhook_url,
                "totp_identifier": totp_identifier,
                "totp_url": totp_url,
                "browser_session_id": browser_session_id,
                "model": model,
                "publish_workflow": publish_workflow,
                "include_action_history_in_verification": include_action_history_in_verification,
            },
            headers={
                "content-type": "application/json",
                "x-user-agent": str(user_agent) if user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskRunResponse,
                    parse_obj_as(
                        type_=TaskRunResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def run_workflow(
        self,
        *,
        workflow_id: str,
        template: typing.Optional[bool] = None,
        max_steps_override: typing.Optional[int] = None,
        user_agent: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        title: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowRunResponse]:
        """
        Run a workflow

        Parameters
        ----------
        workflow_id : str
            ID of the workflow to run. Workflow ID starts with `wpid_`.

        template : typing.Optional[bool]

        max_steps_override : typing.Optional[int]

        user_agent : typing.Optional[str]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Parameters to pass to the workflow

        title : typing.Optional[str]
            The title for this workflow run

        proxy_location : typing.Optional[ProxyLocation]

            Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

            Available geotargeting options:
            - RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
            - RESIDENTIAL_ES: Spain
            - RESIDENTIAL_IE: Ireland
            - RESIDENTIAL_GB: United Kingdom
            - RESIDENTIAL_IN: India
            - RESIDENTIAL_JP: Japan
            - RESIDENTIAL_FR: France
            - RESIDENTIAL_DE: Germany
            - RESIDENTIAL_NZ: New Zealand
            - RESIDENTIAL_ZA: South Africa
            - RESIDENTIAL_AR: Argentina
            - RESIDENTIAL_ISP: ISP proxy
            - US-CA: California
            - US-NY: New York
            - US-TX: Texas
            - US-FL: Florida
            - US-WA: Washington
            - NONE: No proxy

        webhook_url : typing.Optional[str]
            URL to send workflow status updates to after a run is finished. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for webhook questions.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        browser_session_id : typing.Optional[str]
            ID of a Skyvern browser session to reuse, having it continue from the current screen state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowRunResponse]
            Successfully run workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/run/workflows",
            method="POST",
            params={
                "template": template,
            },
            json={
                "workflow_id": workflow_id,
                "parameters": parameters,
                "title": title,
                "proxy_location": proxy_location,
                "webhook_url": webhook_url,
                "totp_url": totp_url,
                "totp_identifier": totp_identifier,
                "browser_session_id": browser_session_id,
            },
            headers={
                "content-type": "application/json",
                "x-max-steps-override": str(max_steps_override) if max_steps_override is not None else None,
                "x-user-agent": str(user_agent) if user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowRunResponse,
                    parse_obj_as(
                        type_=WorkflowRunResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRunResponse]:
        """
        Get run information (task run, workflow run)

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRunResponse]
            Successfully got run
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRunResponse,
                    parse_obj_as(
                        type_=GetRunResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def cancel_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Cancel a run (task or workflow)

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_workflows(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        only_saved_tasks: typing.Optional[bool] = None,
        only_workflows: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        template: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Workflow]]:
        """
        Get all workflows with the latest version for the organization.

        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        only_saved_tasks : typing.Optional[bool]

        only_workflows : typing.Optional[bool]

        title : typing.Optional[str]

        template : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Workflow]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "only_saved_tasks": only_saved_tasks,
                "only_workflows": only_workflows,
                "title": title,
                "template": template,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Workflow],
                    parse_obj_as(
                        type_=typing.List[Workflow],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def create_workflow(
        self,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Workflow]:
        """
        Create a new workflow

        Parameters
        ----------
        json_definition : typing.Optional[WorkflowCreateYamlRequest]
            Workflow definition in JSON format

        yaml_definition : typing.Optional[str]
            Workflow definition in YAML format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Workflow]
            Successfully created workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="POST",
            json={
                "json_definition": convert_and_respect_annotation_metadata(
                    object_=json_definition, annotation=typing.Optional[WorkflowCreateYamlRequest], direction="write"
                ),
                "yaml_definition": yaml_definition,
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
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def update_workflow(
        self,
        workflow_id: str,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Workflow]:
        """
        Update a workflow

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow to update. Workflow ID starts with `wpid_`.

        json_definition : typing.Optional[WorkflowCreateYamlRequest]
            Workflow definition in JSON format

        yaml_definition : typing.Optional[str]
            Workflow definition in YAML format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Workflow]
            Successfully updated workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}",
            method="POST",
            json={
                "json_definition": convert_and_respect_annotation_metadata(
                    object_=json_definition, annotation=typing.Optional[WorkflowCreateYamlRequest], direction="write"
                ),
                "yaml_definition": yaml_definition,
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
                    Workflow,
                    parse_obj_as(
                        type_=Workflow,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_workflow(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a workflow

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow to delete. Workflow ID starts with `wpid_`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successfully deleted workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Artifact]:
        """
        Get an artifact

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Artifact]
            Successfully retrieved artifact
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artifacts/{encode_path_param(artifact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Artifact,
                    parse_obj_as(
                        type_=Artifact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def retry_run_webhook(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Retry sending the webhook for a run

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/retry_webhook",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_browser_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[BrowserSessionResponse]]:
        """
        Get all active browser sessions for the organization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BrowserSessionResponse]]
            Successfully retrieved all active browser sessions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/browser_sessions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BrowserSessionResponse],
                    parse_obj_as(
                        type_=typing.List[BrowserSessionResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def create_browser_session(
        self, *, timeout: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BrowserSessionResponse]:
        """
        Create a new browser session

        Parameters
        ----------
        timeout : typing.Optional[int]
            Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 10080. Defaults to 60.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BrowserSessionResponse]
            Successfully created browser session
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/browser_sessions",
            method="POST",
            json={
                "timeout": timeout,
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
                    BrowserSessionResponse,
                    parse_obj_as(
                        type_=BrowserSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def close_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Close a browser session

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session to close. completed_at will be set when the browser session is closed. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successfully closed browser session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/browser_sessions/{encode_path_param(browser_session_id)}/close",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BrowserSessionResponse]:
        """
        Get details about a specific browser session by ID

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BrowserSessionResponse]
            Successfully retrieved browser session details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/browser_sessions/{encode_path_param(browser_session_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserSessionResponse,
                    parse_obj_as(
                        type_=BrowserSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def send_totp_code(
        self,
        *,
        totp_identifier: str,
        content: str,
        task_id: typing.Optional[str] = OMIT,
        workflow_id: typing.Optional[str] = OMIT,
        workflow_run_id: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        expired_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TotpCode]:
        """
        Forward a TOTP (2FA, MFA) email or sms message containing the code to Skyvern. This endpoint stores the code in database so that Skyvern can use it while running tasks/workflows.

        Parameters
        ----------
        totp_identifier : str
            The identifier of the TOTP code. It can be the email address, phone number, or the identifier of the user.

        content : str
            The content of the TOTP code. It can be the email content that contains the TOTP code, or the sms message that contains the TOTP code. Skyvern will automatically extract the TOTP code from the content.

        task_id : typing.Optional[str]
            The task_id the totp code is for. It can be the task_id of the task that the TOTP code is for.

        workflow_id : typing.Optional[str]
            The workflow ID the TOTP code is for. It can be the workflow ID of the workflow that the TOTP code is for.

        workflow_run_id : typing.Optional[str]
            The workflow run id that the TOTP code is for. It can be the workflow run id of the workflow run that the TOTP code is for.

        source : typing.Optional[str]
            An optional field. The source of the TOTP code. e.g. email, sms, etc.

        expired_at : typing.Optional[dt.datetime]
            The timestamp when the TOTP code expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TotpCode]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/credentials/totp",
            method="POST",
            json={
                "totp_identifier": totp_identifier,
                "task_id": task_id,
                "workflow_id": workflow_id,
                "workflow_run_id": workflow_run_id,
                "source": source,
                "content": content,
                "expired_at": expired_at,
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
                    TotpCode,
                    parse_obj_as(
                        type_=TotpCode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_credentials(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CredentialResponse]]:
        """
        Retrieves a paginated list of credentials for the current organization

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CredentialResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/credentials",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CredentialResponse],
                    parse_obj_as(
                        type_=typing.List[CredentialResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def create_credential(
        self,
        *,
        name: str,
        credential_type: CredentialType,
        credential: CreateCredentialRequestCredential,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CredentialResponse]:
        """
        Creates a new credential for the current organization

        Parameters
        ----------
        name : str
            Name of the credential

        credential_type : CredentialType
            Type of credential to create

        credential : CreateCredentialRequestCredential
            The credential data to store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/credentials",
            method="POST",
            json={
                "name": name,
                "credential_type": credential_type,
                "credential": convert_and_respect_annotation_metadata(
                    object_=credential, annotation=CreateCredentialRequestCredential, direction="write"
                ),
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a specific credential by its ID

        Parameters
        ----------
        credential_id : str
            The unique identifier of the credential to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/credentials/{encode_path_param(credential_id)}/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CredentialResponse]:
        """
        Retrieves a specific credential by its ID

        Parameters
        ----------
        credential_id : str
            The unique identifier of the credential

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/credentials/{encode_path_param(credential_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
