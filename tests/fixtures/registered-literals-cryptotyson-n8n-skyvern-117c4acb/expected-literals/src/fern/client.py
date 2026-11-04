

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.artifact import Artifact
from .types.artifact_type import ArtifactType
from .types.browser_session_response import BrowserSessionResponse
from .types.create_credential_request_credential import CreateCredentialRequestCredential
from .types.create_project_response import CreateProjectResponse
from .types.credential_response import CredentialResponse
from .types.get_run_response import GetRunResponse
from .types.project import Project
from .types.project_file import ProjectFile
from .types.proxy_location import ProxyLocation
from .types.run_engine import RunEngine
from .types.skyvern_forge_sdk_schemas_credentials_credential_type import SkyvernForgeSdkSchemasCredentialsCredentialType
from .types.skyvern_schemas_run_blocks_credential_type import SkyvernSchemasRunBlocksCredentialType
from .types.task_run_request_data_extraction_schema import TaskRunRequestDataExtractionSchema
from .types.task_run_response import TaskRunResponse
from .types.totp_code import TotpCode
from .types.workflow import Workflow
from .types.workflow_create_yaml_request import WorkflowCreateYamlRequest
from .types.workflow_run_response import WorkflowRunResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

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
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        publish_workflow: typing.Optional[bool] = OMIT,
        include_action_history_in_verification: typing.Optional[bool] = OMIT,
        max_screenshot_scrolls: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskRunResponse:
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
            - RESIDENTIAL_AU: Australia
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

            After a run is finished, send an update to this URL. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        browser_session_id : typing.Optional[str]

            Run the task or workflow in the specific Skyvern browser session. Having a browser session can persist the real-time state of the browser, so that the next run can continue from where the previous run left off.

        model : typing.Optional[typing.Dict[str, typing.Any]]

            Optional model configuration.

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The extra HTTP headers for the requests in browser.

        publish_workflow : typing.Optional[bool]
            Whether to publish this task as a reusable workflow. Only available for skyvern-2.0.

        include_action_history_in_verification : typing.Optional[bool]
            Whether to include action history when verifying that the task is complete

        max_screenshot_scrolls : typing.Optional[int]
            The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskRunResponse
            Successfully run task

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.run_task(
            prompt="Find the top 3 posts on Hacker News.",
        )
        """
        _response = self._raw_client.run_task(
            prompt=prompt,
            user_agent=user_agent,
            url=url,
            engine=engine,
            title=title,
            proxy_location=proxy_location,
            data_extraction_schema=data_extraction_schema,
            error_code_mapping=error_code_mapping,
            max_steps=max_steps,
            webhook_url=webhook_url,
            totp_identifier=totp_identifier,
            totp_url=totp_url,
            browser_session_id=browser_session_id,
            model=model,
            extra_http_headers=extra_http_headers,
            publish_workflow=publish_workflow,
            include_action_history_in_verification=include_action_history_in_verification,
            max_screenshot_scrolls=max_screenshot_scrolls,
            request_options=request_options,
        )
        return _response.data

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
        max_screenshot_scrolls: typing.Optional[int] = OMIT,
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
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
            - RESIDENTIAL_AU: Australia
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

        max_screenshot_scrolls : typing.Optional[int]
            The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The extra HTTP headers for the requests in browser.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse
            Successfully run workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.run_workflow(
            workflow_id="wpid_123",
        )
        """
        _response = self._raw_client.run_workflow(
            workflow_id=workflow_id,
            template=template,
            max_steps_override=max_steps_override,
            user_agent=user_agent,
            parameters=parameters,
            title=title,
            proxy_location=proxy_location,
            webhook_url=webhook_url,
            totp_url=totp_url,
            totp_identifier=totp_identifier,
            browser_session_id=browser_session_id,
            max_screenshot_scrolls=max_screenshot_scrolls,
            extra_http_headers=extra_http_headers,
            request_options=request_options,
        )
        return _response.data

    def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetRunResponse:
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
        GetRunResponse
            Successfully got run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_run(
            run_id="tsk_123",
        )
        """
        _response = self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    def cancel_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.cancel_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.cancel_run(run_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[Workflow]:
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
        typing.List[Workflow]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_workflows()
        """
        _response = self._raw_client.get_workflows(
            page=page,
            page_size=page_size,
            only_saved_tasks=only_saved_tasks,
            only_workflows=only_workflows,
            title=title,
            template=template,
            request_options=request_options,
        )
        return _response.data

    def create_workflow(
        self,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
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
        Workflow
            Successfully created workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_workflow()
        """
        _response = self._raw_client.create_workflow(
            json_definition=json_definition, yaml_definition=yaml_definition, request_options=request_options
        )
        return _response.data

    def update_workflow(
        self,
        workflow_id: str,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
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
        Workflow
            Successfully updated workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_workflow(
            workflow_id="wpid_123",
        )
        """
        _response = self._raw_client.update_workflow(
            workflow_id,
            json_definition=json_definition,
            yaml_definition=yaml_definition,
            request_options=request_options,
        )
        return _response.data

    def delete_workflow(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successfully deleted workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_workflow(
            workflow_id="wpid_123",
        )
        """
        _response = self._raw_client.delete_workflow(workflow_id, request_options=request_options)
        return _response.data

    def get_artifact(self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Artifact:
        """
        Get an artifact

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Successfully retrieved artifact

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_artifact(
            artifact_id="artifact_id",
        )
        """
        _response = self._raw_client.get_artifact(artifact_id, request_options=request_options)
        return _response.data

    def get_run_artifacts(
        self,
        run_id: str,
        *,
        artifact_type: typing.Optional[typing.Sequence[ArtifactType]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Get artifacts for a run

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        artifact_type : typing.Optional[typing.Sequence[ArtifactType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_run_artifacts(
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run_artifacts(
            run_id, artifact_type=artifact_type, request_options=request_options
        )
        return _response.data

    def retry_run_webhook(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.retry_run_webhook(
            run_id="tsk_123",
        )
        """
        _response = self._raw_client.retry_run_webhook(run_id, request_options=request_options)
        return _response.data

    def get_browser_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BrowserSessionResponse]:
        """
        Get all active browser sessions for the organization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BrowserSessionResponse]
            Successfully retrieved all active browser sessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_browser_sessions()
        """
        _response = self._raw_client.get_browser_sessions(request_options=request_options)
        return _response.data

    def create_browser_session(
        self, *, timeout: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> BrowserSessionResponse:
        """
        Create a browser session that persists across multiple runs

        Parameters
        ----------
        timeout : typing.Optional[int]
            Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 240. Defaults to 60.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserSessionResponse
            Successfully created browser session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_browser_session()
        """
        _response = self._raw_client.create_browser_session(timeout=timeout, request_options=request_options)
        return _response.data

    def close_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Close a session. Once closed, the session cannot be used again.

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session to close. completed_at will be set when the browser session is closed. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successfully closed browser session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.close_browser_session(
            browser_session_id="pbs_123456",
        )
        """
        _response = self._raw_client.close_browser_session(browser_session_id, request_options=request_options)
        return _response.data

    def get_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BrowserSessionResponse:
        """
        Get details about a specific browser session, including the browser address for cdp connection.

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserSessionResponse
            Successfully retrieved browser session details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_browser_session(
            browser_session_id="pbs_123456",
        )
        """
        _response = self._raw_client.get_browser_session(browser_session_id, request_options=request_options)
        return _response.data

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
    ) -> TotpCode:
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
        TotpCode
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.send_totp_code(
            totp_identifier="john.doe@example.com",
            content="Hello, your verification code is 123456",
        )
        """
        _response = self._raw_client.send_totp_code(
            totp_identifier=totp_identifier,
            content=content,
            task_id=task_id,
            workflow_id=workflow_id,
            workflow_run_id=workflow_run_id,
            source=source,
            expired_at=expired_at,
            request_options=request_options,
        )
        return _response.data

    def get_credentials(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CredentialResponse]:
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
        typing.List[CredentialResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_credentials(
            page=1,
            page_size=10,
        )
        """
        _response = self._raw_client.get_credentials(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def create_credential(
        self,
        *,
        name: str,
        credential_type: SkyvernForgeSdkSchemasCredentialsCredentialType,
        credential: CreateCredentialRequestCredential,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CredentialResponse:
        """
        Creates a new credential for the current organization

        Parameters
        ----------
        name : str
            Name of the credential

        credential_type : SkyvernForgeSdkSchemasCredentialsCredentialType
            Type of credential to create

        credential : CreateCredentialRequestCredential
            The credential data to store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, NonEmptyPasswordCredential

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_credential(
            name="My Credential",
            credential_type="password",
            credential=NonEmptyPasswordCredential(
                password="securepassword123",
                username="user@example.com",
                totp="JBSWY3DPEHPK3PXP",
            ),
        )
        """
        _response = self._raw_client.create_credential(
            name=name, credential_type=credential_type, credential=credential, request_options=request_options
        )
        return _response.data

    def delete_credential(self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_credential(
            credential_id="cred_1234567890",
        )
        """
        _response = self._raw_client.delete_credential(credential_id, request_options=request_options)
        return _response.data

    def get_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialResponse:
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
        CredentialResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_credential(
            credential_id="cred_1234567890",
        )
        """
        _response = self._raw_client.get_credential(credential_id, request_options=request_options)
        return _response.data

    def get_projects(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Project]:
        """
        Retrieves a paginated list of projects for the current organization

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
        typing.List[Project]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_projects(
            page=1,
            page_size=10,
        )
        """
        _response = self._raw_client.get_projects(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def create_project(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Sequence[ProjectFile]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Create a new project with optional files and metadata

        Parameters
        ----------
        workflow_id : typing.Optional[str]
            Associated workflow ID

        run_id : typing.Optional[str]
            Associated run ID

        files : typing.Optional[typing.Sequence[ProjectFile]]
            Array of files to include in the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_project()
        """
        _response = self._raw_client.create_project(
            workflow_id=workflow_id, run_id=run_id, files=files, request_options=request_options
        )
        return _response.data

    def get_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Project:
        """
        Retrieves a specific project by its ID

        Parameters
        ----------
        project_id : str
            The unique identifier of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_project(
            project_id="proj_abc123",
        )
        """
        _response = self._raw_client.get_project(project_id, request_options=request_options)
        return _response.data

    def deploy_project(
        self,
        project_id: str,
        *,
        files: typing.Sequence[ProjectFile],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Deploy a project with updated files, creating a new version

        Parameters
        ----------
        project_id : str
            The unique identifier of the project

        files : typing.Sequence[ProjectFile]
            Array of files to include in the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, ProjectFile

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deploy_project(
            project_id="proj_abc123",
            files=[
                ProjectFile(
                    path="src/main.py",
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.deploy_project(project_id, files=files, request_options=request_options)
        return _response.data

    def login(
        self,
        *,
        credential_type: SkyvernSchemasRunBlocksCredentialType,
        url: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        max_screenshot_scrolling_times: typing.Optional[int] = OMIT,
        credential_id: typing.Optional[str] = OMIT,
        bitwarden_collection_id: typing.Optional[str] = OMIT,
        bitwarden_item_id: typing.Optional[str] = OMIT,
        onepassword_vault_id: typing.Optional[str] = OMIT,
        onepassword_item_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
        """
        Log in to a website using either credential stored in Skyvern, Bitwarden or 1Password

        Parameters
        ----------
        credential_type : SkyvernSchemasRunBlocksCredentialType
            Where to get the credential from

        url : typing.Optional[str]
            Website url

        prompt : typing.Optional[str]
            Login instructions. Skyvern has default prompt/instruction for login if this field is not provided.

        webhook_url : typing.Optional[str]
            Webhook URL to send login status updates

        proxy_location : typing.Optional[ProxyLocation]
            Proxy location to use

        totp_identifier : typing.Optional[str]
            Identifier for TOTP (Time-based One-Time Password) if required

        totp_url : typing.Optional[str]
            TOTP URL to fetch one-time passwords

        browser_session_id : typing.Optional[str]
            ID of the browser session to use, which is prefixed by `pbs_` e.g. `pbs_123456`

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Additional HTTP headers to include in requests

        max_screenshot_scrolling_times : typing.Optional[int]
            Maximum number of times to scroll for screenshots

        credential_id : typing.Optional[str]
            ID of the Skyvern credential to use for login.

        bitwarden_collection_id : typing.Optional[str]
            Bitwarden collection ID. You can find it in the Bitwarden collection URL. e.g. `https://vault.bitwarden.com/vaults/collection_id/items`

        bitwarden_item_id : typing.Optional[str]
            Bitwarden item ID

        onepassword_vault_id : typing.Optional[str]
            1Password vault ID

        onepassword_item_id : typing.Optional[str]
            1Password item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.login(
            credential_type="skyvern",
        )
        """
        _response = self._raw_client.login(
            credential_type=credential_type,
            url=url,
            prompt=prompt,
            webhook_url=webhook_url,
            proxy_location=proxy_location,
            totp_identifier=totp_identifier,
            totp_url=totp_url,
            browser_session_id=browser_session_id,
            extra_http_headers=extra_http_headers,
            max_screenshot_scrolling_times=max_screenshot_scrolling_times,
            credential_id=credential_id,
            bitwarden_collection_id=bitwarden_collection_id,
            bitwarden_item_id=bitwarden_item_id,
            onepassword_vault_id=onepassword_vault_id,
            onepassword_item_id=onepassword_item_id,
            request_options=request_options,
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

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
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        publish_workflow: typing.Optional[bool] = OMIT,
        include_action_history_in_verification: typing.Optional[bool] = OMIT,
        max_screenshot_scrolls: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskRunResponse:
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
            - RESIDENTIAL_AU: Australia
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

            After a run is finished, send an update to this URL. Refer to https://docs.skyvern.com/running-tasks/webhooks-faq for more details.

        totp_identifier : typing.Optional[str]

            Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://docs.skyvern.com/credentials/totp#option-3-push-code-to-skyvern for more details.

        totp_url : typing.Optional[str]

            URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://docs.skyvern.com/credentials/totp#option-2-get-code-from-your-endpoint for more details.

        browser_session_id : typing.Optional[str]

            Run the task or workflow in the specific Skyvern browser session. Having a browser session can persist the real-time state of the browser, so that the next run can continue from where the previous run left off.

        model : typing.Optional[typing.Dict[str, typing.Any]]

            Optional model configuration.

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The extra HTTP headers for the requests in browser.

        publish_workflow : typing.Optional[bool]
            Whether to publish this task as a reusable workflow. Only available for skyvern-2.0.

        include_action_history_in_verification : typing.Optional[bool]
            Whether to include action history when verifying that the task is complete

        max_screenshot_scrolls : typing.Optional[int]
            The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskRunResponse
            Successfully run task

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.run_task(
                prompt="Find the top 3 posts on Hacker News.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_task(
            prompt=prompt,
            user_agent=user_agent,
            url=url,
            engine=engine,
            title=title,
            proxy_location=proxy_location,
            data_extraction_schema=data_extraction_schema,
            error_code_mapping=error_code_mapping,
            max_steps=max_steps,
            webhook_url=webhook_url,
            totp_identifier=totp_identifier,
            totp_url=totp_url,
            browser_session_id=browser_session_id,
            model=model,
            extra_http_headers=extra_http_headers,
            publish_workflow=publish_workflow,
            include_action_history_in_verification=include_action_history_in_verification,
            max_screenshot_scrolls=max_screenshot_scrolls,
            request_options=request_options,
        )
        return _response.data

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
        max_screenshot_scrolls: typing.Optional[int] = OMIT,
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
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
            - RESIDENTIAL_AU: Australia
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

        max_screenshot_scrolls : typing.Optional[int]
            The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The extra HTTP headers for the requests in browser.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse
            Successfully run workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.run_workflow(
                workflow_id="wpid_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_workflow(
            workflow_id=workflow_id,
            template=template,
            max_steps_override=max_steps_override,
            user_agent=user_agent,
            parameters=parameters,
            title=title,
            proxy_location=proxy_location,
            webhook_url=webhook_url,
            totp_url=totp_url,
            totp_identifier=totp_identifier,
            browser_session_id=browser_session_id,
            max_screenshot_scrolls=max_screenshot_scrolls,
            extra_http_headers=extra_http_headers,
            request_options=request_options,
        )
        return _response.data

    async def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetRunResponse:
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
        GetRunResponse
            Successfully got run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_run(
                run_id="tsk_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    async def cancel_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.cancel_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_run(run_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[Workflow]:
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
        typing.List[Workflow]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_workflows()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflows(
            page=page,
            page_size=page_size,
            only_saved_tasks=only_saved_tasks,
            only_workflows=only_workflows,
            title=title,
            template=template,
            request_options=request_options,
        )
        return _response.data

    async def create_workflow(
        self,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
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
        Workflow
            Successfully created workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_workflow()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workflow(
            json_definition=json_definition, yaml_definition=yaml_definition, request_options=request_options
        )
        return _response.data

    async def update_workflow(
        self,
        workflow_id: str,
        *,
        json_definition: typing.Optional[WorkflowCreateYamlRequest] = OMIT,
        yaml_definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
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
        Workflow
            Successfully updated workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_workflow(
                workflow_id="wpid_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workflow(
            workflow_id,
            json_definition=json_definition,
            yaml_definition=yaml_definition,
            request_options=request_options,
        )
        return _response.data

    async def delete_workflow(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successfully deleted workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_workflow(
                workflow_id="wpid_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workflow(workflow_id, request_options=request_options)
        return _response.data

    async def get_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Artifact:
        """
        Get an artifact

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Successfully retrieved artifact

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_artifact(
                artifact_id="artifact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact(artifact_id, request_options=request_options)
        return _response.data

    async def get_run_artifacts(
        self,
        run_id: str,
        *,
        artifact_type: typing.Optional[typing.Sequence[ArtifactType]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Get artifacts for a run

        Parameters
        ----------
        run_id : str
            The id of the task run or the workflow run.

        artifact_type : typing.Optional[typing.Sequence[ArtifactType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_run_artifacts(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run_artifacts(
            run_id, artifact_type=artifact_type, request_options=request_options
        )
        return _response.data

    async def retry_run_webhook(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.retry_run_webhook(
                run_id="tsk_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_run_webhook(run_id, request_options=request_options)
        return _response.data

    async def get_browser_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BrowserSessionResponse]:
        """
        Get all active browser sessions for the organization

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BrowserSessionResponse]
            Successfully retrieved all active browser sessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_browser_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_browser_sessions(request_options=request_options)
        return _response.data

    async def create_browser_session(
        self, *, timeout: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> BrowserSessionResponse:
        """
        Create a browser session that persists across multiple runs

        Parameters
        ----------
        timeout : typing.Optional[int]
            Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 240. Defaults to 60.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserSessionResponse
            Successfully created browser session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_browser_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_browser_session(timeout=timeout, request_options=request_options)
        return _response.data

    async def close_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Close a session. Once closed, the session cannot be used again.

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session to close. completed_at will be set when the browser session is closed. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successfully closed browser session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.close_browser_session(
                browser_session_id="pbs_123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.close_browser_session(browser_session_id, request_options=request_options)
        return _response.data

    async def get_browser_session(
        self, browser_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BrowserSessionResponse:
        """
        Get details about a specific browser session, including the browser address for cdp connection.

        Parameters
        ----------
        browser_session_id : str
            The ID of the browser session. browser_session_id starts with `pbs_`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserSessionResponse
            Successfully retrieved browser session details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_browser_session(
                browser_session_id="pbs_123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_browser_session(browser_session_id, request_options=request_options)
        return _response.data

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
    ) -> TotpCode:
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
        TotpCode
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.send_totp_code(
                totp_identifier="john.doe@example.com",
                content="Hello, your verification code is 123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_totp_code(
            totp_identifier=totp_identifier,
            content=content,
            task_id=task_id,
            workflow_id=workflow_id,
            workflow_run_id=workflow_run_id,
            source=source,
            expired_at=expired_at,
            request_options=request_options,
        )
        return _response.data

    async def get_credentials(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CredentialResponse]:
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
        typing.List[CredentialResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_credentials(
                page=1,
                page_size=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_credentials(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_credential(
        self,
        *,
        name: str,
        credential_type: SkyvernForgeSdkSchemasCredentialsCredentialType,
        credential: CreateCredentialRequestCredential,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CredentialResponse:
        """
        Creates a new credential for the current organization

        Parameters
        ----------
        name : str
            Name of the credential

        credential_type : SkyvernForgeSdkSchemasCredentialsCredentialType
            Type of credential to create

        credential : CreateCredentialRequestCredential
            The credential data to store

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, NonEmptyPasswordCredential

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_credential(
                name="My Credential",
                credential_type="password",
                credential=NonEmptyPasswordCredential(
                    password="securepassword123",
                    username="user@example.com",
                    totp="JBSWY3DPEHPK3PXP",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_credential(
            name=name, credential_type=credential_type, credential=credential, request_options=request_options
        )
        return _response.data

    async def delete_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_credential(
                credential_id="cred_1234567890",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_credential(credential_id, request_options=request_options)
        return _response.data

    async def get_credential(
        self, credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialResponse:
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
        CredentialResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_credential(
                credential_id="cred_1234567890",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_credential(credential_id, request_options=request_options)
        return _response.data

    async def get_projects(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Project]:
        """
        Retrieves a paginated list of projects for the current organization

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
        typing.List[Project]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_projects(
                page=1,
                page_size=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_projects(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    async def create_project(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Sequence[ProjectFile]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Create a new project with optional files and metadata

        Parameters
        ----------
        workflow_id : typing.Optional[str]
            Associated workflow ID

        run_id : typing.Optional[str]
            Associated run ID

        files : typing.Optional[typing.Sequence[ProjectFile]]
            Array of files to include in the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_project()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project(
            workflow_id=workflow_id, run_id=run_id, files=files, request_options=request_options
        )
        return _response.data

    async def get_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Project:
        """
        Retrieves a specific project by its ID

        Parameters
        ----------
        project_id : str
            The unique identifier of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_project(
                project_id="proj_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project(project_id, request_options=request_options)
        return _response.data

    async def deploy_project(
        self,
        project_id: str,
        *,
        files: typing.Sequence[ProjectFile],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProjectResponse:
        """
        Deploy a project with updated files, creating a new version

        Parameters
        ----------
        project_id : str
            The unique identifier of the project

        files : typing.Sequence[ProjectFile]
            Array of files to include in the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProjectFile

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deploy_project(
                project_id="proj_abc123",
                files=[
                    ProjectFile(
                        path="src/main.py",
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deploy_project(project_id, files=files, request_options=request_options)
        return _response.data

    async def login(
        self,
        *,
        credential_type: SkyvernSchemasRunBlocksCredentialType,
        url: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        proxy_location: typing.Optional[ProxyLocation] = OMIT,
        totp_identifier: typing.Optional[str] = OMIT,
        totp_url: typing.Optional[str] = OMIT,
        browser_session_id: typing.Optional[str] = OMIT,
        extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        max_screenshot_scrolling_times: typing.Optional[int] = OMIT,
        credential_id: typing.Optional[str] = OMIT,
        bitwarden_collection_id: typing.Optional[str] = OMIT,
        bitwarden_item_id: typing.Optional[str] = OMIT,
        onepassword_vault_id: typing.Optional[str] = OMIT,
        onepassword_item_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
        """
        Log in to a website using either credential stored in Skyvern, Bitwarden or 1Password

        Parameters
        ----------
        credential_type : SkyvernSchemasRunBlocksCredentialType
            Where to get the credential from

        url : typing.Optional[str]
            Website url

        prompt : typing.Optional[str]
            Login instructions. Skyvern has default prompt/instruction for login if this field is not provided.

        webhook_url : typing.Optional[str]
            Webhook URL to send login status updates

        proxy_location : typing.Optional[ProxyLocation]
            Proxy location to use

        totp_identifier : typing.Optional[str]
            Identifier for TOTP (Time-based One-Time Password) if required

        totp_url : typing.Optional[str]
            TOTP URL to fetch one-time passwords

        browser_session_id : typing.Optional[str]
            ID of the browser session to use, which is prefixed by `pbs_` e.g. `pbs_123456`

        extra_http_headers : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Additional HTTP headers to include in requests

        max_screenshot_scrolling_times : typing.Optional[int]
            Maximum number of times to scroll for screenshots

        credential_id : typing.Optional[str]
            ID of the Skyvern credential to use for login.

        bitwarden_collection_id : typing.Optional[str]
            Bitwarden collection ID. You can find it in the Bitwarden collection URL. e.g. `https://vault.bitwarden.com/vaults/collection_id/items`

        bitwarden_item_id : typing.Optional[str]
            Bitwarden item ID

        onepassword_vault_id : typing.Optional[str]
            1Password vault ID

        onepassword_item_id : typing.Optional[str]
            1Password item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.login(
                credential_type="skyvern",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(
            credential_type=credential_type,
            url=url,
            prompt=prompt,
            webhook_url=webhook_url,
            proxy_location=proxy_location,
            totp_identifier=totp_identifier,
            totp_url=totp_url,
            browser_session_id=browser_session_id,
            extra_http_headers=extra_http_headers,
            max_screenshot_scrolling_times=max_screenshot_scrolling_times,
            credential_id=credential_id,
            bitwarden_collection_id=bitwarden_collection_id,
            bitwarden_item_id=bitwarden_item_id,
            onepassword_vault_id=onepassword_vault_id,
            onepassword_item_id=onepassword_item_id,
            request_options=request_options,
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
