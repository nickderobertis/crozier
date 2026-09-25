

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.action import Action
from .types.action_run import ActionRun
from .types.action_runs import ActionRuns
from .types.actions import Actions
from .types.agent import Agent
from .types.agent_run import AgentRun
from .types.agent_runs import AgentRuns
from .types.agent_statistics import AgentStatistics
from .types.agents import Agents
from .types.document import Document
from .types.documents import Documents
from .types.function import Function
from .types.functions import Functions
from .types.hook import Hook
from .types.hook_run import HookRun
from .types.hook_runs import HookRuns
from .types.hooks import Hooks
from .types.log import Log
from .types.logs import Logs
from .types.model import Model
from .types.models import Models
from .types.organization import Organization
from .types.organizations import Organizations
from .types.patch_action_run_id_status import PatchActionRunIdStatus
from .types.patch_agent_run_id_status import PatchAgentRunIdStatus
from .types.patch_document_id_ground_truth_item import PatchDocumentIdGroundTruthItem
from .types.patch_hook_id_trigger import PatchHookIdTrigger
from .types.patch_hook_run_id_status import PatchHookRunIdStatus
from .types.patch_model_id_confidence_version import PatchModelIdConfidenceVersion
from .types.patch_model_id_llm_version import PatchModelIdLlmVersion
from .types.patch_model_id_postprocess_config import PatchModelIdPostprocessConfig
from .types.patch_model_id_preprocess_config import PatchModelIdPreprocessConfig
from .types.patch_role_id_permissions_item import PatchRoleIdPermissionsItem
from .types.patch_validation_task_id_status import PatchValidationTaskIdStatus
from .types.post_documents_content_type import PostDocumentsContentType
from .types.post_documents_ground_truth_item import PostDocumentsGroundTruthItem
from .types.post_functions_runtime import PostFunctionsRuntime
from .types.post_hooks_trigger import PostHooksTrigger
from .types.post_models_confidence_version import PostModelsConfidenceVersion
from .types.post_models_llm_version import PostModelsLlmVersion
from .types.post_models_postprocess_config import PostModelsPostprocessConfig
from .types.post_models_preprocess_config import PostModelsPreprocessConfig
from .types.post_predictions_image_quality import PostPredictionsImageQuality
from .types.post_predictions_postprocess_config import PostPredictionsPostprocessConfig
from .types.post_predictions_preprocess_config import PostPredictionsPreprocessConfig
from .types.post_roles_permissions_item import PostRolesPermissionsItem
from .types.prediction import Prediction
from .types.predictions import Predictions
from .types.role import Role
from .types.roles import Roles
from .types.user import User
from .types.users import Users
from .types.validation import Validation
from .types.validation_task import ValidationTask
from .types.validation_tasks import ValidationTasks
from .types.validations import Validations


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



        Defaults to FernApiEnvironment.DEFAULT



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to 'v1'.

    token : typing.Union[str, typing.Callable[[], str]]
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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        token: typing.Union[str, typing.Callable[[], str]],
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
        if base_path is not None:
            _base_path = base_path if base_path is not None else "v1"
            base_url = "https://api.cradl.ai/{basePath}".format(basePath=_base_path)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
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

    def get_actions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Actions:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Actions
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_actions()
        """
        _response = self._raw_client.get_actions(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_actions(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        secret_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Action:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        connection_id : typing.Optional[str]

        secret_id : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_actions()
        """
        _response = self._raw_client.post_actions(
            metadata=metadata,
            function_id=function_id,
            name=name,
            description=description,
            connection_id=connection_id,
            secret_id=secret_id,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_actions_action_id(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_actions_action_id(
            action_id="actionId",
        )
        """
        _response = self._raw_client.get_actions_action_id(action_id, request_options=request_options)
        return _response.data

    def delete_actions_action_id(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_actions_action_id(
            action_id="actionId",
        )
        """
        _response = self._raw_client.delete_actions_action_id(action_id, request_options=request_options)
        return _response.data

    def patch_actions_action_id(
        self,
        action_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        secret_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        connection_id : typing.Optional[str]

        secret_id : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_actions_action_id(
            action_id="actionId",
        )
        """
        _response = self._raw_client.patch_actions_action_id(
            action_id,
            metadata=metadata,
            function_id=function_id,
            name=name,
            description=description,
            connection_id=connection_id,
            secret_id=secret_id,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_actions_action_id_runs(
        self,
        action_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRuns:
        """
        Parameters
        ----------
        action_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRuns
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_actions_action_id_runs(
            action_id="actionId",
        )
        """
        _response = self._raw_client.get_actions_action_id_runs(
            action_id, status=status, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_actions_action_id_runs(
        self,
        action_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        no_agent_run_update: typing.Optional[bool] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        no_agent_run_update : typing.Optional[bool]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_actions_action_id_runs(
            action_id="actionId",
        )
        """
        _response = self._raw_client.post_actions_action_id_runs(
            action_id,
            input=input,
            metadata=metadata,
            no_agent_run_update=no_agent_run_update,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    def get_actions_action_id_runs_run_id(
        self, action_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_actions_action_id_runs_run_id(
            action_id="actionId",
            run_id="runId",
        )
        """
        _response = self._raw_client.get_actions_action_id_runs_run_id(
            action_id, run_id, request_options=request_options
        )
        return _response.data

    def patch_actions_action_id_runs_run_id(
        self,
        action_id: str,
        run_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[PatchActionRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        run_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[PatchActionRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_actions_action_id_runs_run_id(
            action_id="actionId",
            run_id="runId",
        )
        """
        _response = self._raw_client.patch_actions_action_id_runs_run_id(
            action_id, run_id, output=output, metadata=metadata, status=status, request_options=request_options
        )
        return _response.data

    def get_agents(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agents:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agents
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_agents()
        """
        _response = self._raw_client.get_agents(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_agents(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        resource_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        resource_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_agents()
        """
        _response = self._raw_client.post_agents(
            metadata=metadata,
            name=name,
            description=description,
            resource_ids=resource_ids,
            request_options=request_options,
        )
        return _response.data

    def get_agents_agent_id(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_agents_agent_id(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.get_agents_agent_id(agent_id, request_options=request_options)
        return _response.data

    def delete_agents_agent_id(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_agents_agent_id(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.delete_agents_agent_id(agent_id, request_options=request_options)
        return _response.data

    def patch_agents_agent_id(
        self,
        agent_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        resource_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        resource_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_agents_agent_id(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.patch_agents_agent_id(
            agent_id,
            metadata=metadata,
            name=name,
            description=description,
            resource_ids=resource_ids,
            request_options=request_options,
        )
        return _response.data

    def get_agents_agent_id_runs(
        self,
        agent_id: str,
        *,
        history: typing.Optional[str] = None,
        created_time_after: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        updated_time_after: typing.Optional[str] = None,
        created_time_before: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        updated_time_before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRuns:
        """
        Parameters
        ----------
        agent_id : str

        history : typing.Optional[str]

        created_time_after : typing.Optional[str]

        next_token : typing.Optional[str]

        sort : typing.Optional[str]

        updated_time_after : typing.Optional[str]

        created_time_before : typing.Optional[str]

        status : typing.Optional[str]

        max_results : typing.Optional[str]

        updated_time_before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRuns
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_agents_agent_id_runs(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.get_agents_agent_id_runs(
            agent_id,
            history=history,
            created_time_after=created_time_after,
            next_token=next_token,
            sort=sort,
            updated_time_after=updated_time_after,
            created_time_before=created_time_before,
            status=status,
            max_results=max_results,
            updated_time_before=updated_time_before,
            request_options=request_options,
        )
        return _response.data

    def post_agents_agent_id_runs(
        self,
        agent_id: str,
        *,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        variables : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_agents_agent_id_runs(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.post_agents_agent_id_runs(
            agent_id, variables=variables, request_options=request_options
        )
        return _response.data

    def get_agents_agent_id_runs_run_id(
        self, agent_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_agents_agent_id_runs_run_id(
            agent_id="agentId",
            run_id="runId",
        )
        """
        _response = self._raw_client.get_agents_agent_id_runs_run_id(agent_id, run_id, request_options=request_options)
        return _response.data

    def delete_agents_agent_id_runs_run_id(
        self, agent_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_agents_agent_id_runs_run_id(
            agent_id="agentId",
            run_id="runId",
        )
        """
        _response = self._raw_client.delete_agents_agent_id_runs_run_id(
            agent_id, run_id, request_options=request_options
        )
        return _response.data

    def patch_agents_agent_id_runs_run_id(
        self,
        agent_id: str,
        run_id: str,
        *,
        status: typing.Optional[PatchAgentRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        status : typing.Optional[PatchAgentRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_agents_agent_id_runs_run_id(
            agent_id="agentId",
            run_id="runId",
        )
        """
        _response = self._raw_client.patch_agents_agent_id_runs_run_id(
            agent_id, run_id, status=status, request_options=request_options
        )
        return _response.data

    def get_agents_agent_id_statistics(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentStatistics:
        """
        Parameters
        ----------
        agent_id : str

        before : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentStatistics
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_agents_agent_id_statistics(
            agent_id="agentId",
        )
        """
        _response = self._raw_client.get_agents_agent_id_statistics(
            agent_id, before=before, after=after, request_options=request_options
        )
        return _response.data

    def get_documents(
        self,
        *,
        dataset_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        document_id: typing.Optional[str] = None,
        consent_id: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Documents:
        """
        Parameters
        ----------
        dataset_id : typing.Optional[str]

        next_token : typing.Optional[str]

        order : typing.Optional[str]

        document_id : typing.Optional[str]

        consent_id : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Documents
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_documents()
        """
        _response = self._raw_client.get_documents(
            dataset_id=dataset_id,
            next_token=next_token,
            order=order,
            document_id=document_id,
            consent_id=consent_id,
            max_results=max_results,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def post_documents(
        self,
        *,
        ground_truth: typing.Optional[typing.Sequence[PostDocumentsGroundTruthItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        consent_id: typing.Optional[str] = OMIT,
        retention_in_days: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        content_type: typing.Optional[PostDocumentsContentType] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        ground_truth : typing.Optional[typing.Sequence[PostDocumentsGroundTruthItem]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        consent_id : typing.Optional[str]

        retention_in_days : typing.Optional[int]

        name : typing.Optional[str]

        description : typing.Optional[str]

        dataset_id : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        content_type : typing.Optional[PostDocumentsContentType]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_documents()
        """
        _response = self._raw_client.post_documents(
            ground_truth=ground_truth,
            metadata=metadata,
            consent_id=consent_id,
            retention_in_days=retention_in_days,
            name=name,
            description=description,
            dataset_id=dataset_id,
            agent_run_id=agent_run_id,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        return _response.data

    def delete_documents(
        self,
        *,
        consent_id: typing.Optional[str] = None,
        dataset_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Documents:
        """
        Parameters
        ----------
        consent_id : typing.Optional[str]

        dataset_id : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Documents
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_documents()
        """
        _response = self._raw_client.delete_documents(
            consent_id=consent_id,
            dataset_id=dataset_id,
            next_token=next_token,
            max_results=max_results,
            request_options=request_options,
        )
        return _response.data

    def get_documents_document_id(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_documents_document_id(
            document_id="documentId",
        )
        """
        _response = self._raw_client.get_documents_document_id(document_id, request_options=request_options)
        return _response.data

    def delete_documents_document_id(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_documents_document_id(
            document_id="documentId",
        )
        """
        _response = self._raw_client.delete_documents_document_id(document_id, request_options=request_options)
        return _response.data

    def patch_documents_document_id(
        self,
        document_id: str,
        *,
        ground_truth: typing.Optional[typing.Sequence[PatchDocumentIdGroundTruthItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        retention_in_days: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        ground_truth : typing.Optional[typing.Sequence[PatchDocumentIdGroundTruthItem]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        retention_in_days : typing.Optional[int]

        name : typing.Optional[str]

        description : typing.Optional[str]

        dataset_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_documents_document_id(
            document_id="documentId",
        )
        """
        _response = self._raw_client.patch_documents_document_id(
            document_id,
            ground_truth=ground_truth,
            metadata=metadata,
            retention_in_days=retention_in_days,
            name=name,
            description=description,
            dataset_id=dataset_id,
            request_options=request_options,
        )
        return _response.data

    def get_functions(
        self,
        *,
        owner: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Functions:
        """
        Parameters
        ----------
        owner : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        order : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Functions
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_functions()
        """
        _response = self._raw_client.get_functions(
            owner=owner,
            next_token=next_token,
            max_results=max_results,
            sort_by=sort_by,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def post_functions(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        runtime: typing.Optional[PostFunctionsRuntime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        runtime : typing.Optional[PostFunctionsRuntime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_functions()
        """
        _response = self._raw_client.post_functions(
            metadata=metadata, name=name, description=description, runtime=runtime, request_options=request_options
        )
        return _response.data

    def get_functions_function_id(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_functions_function_id(
            function_id="functionId",
        )
        """
        _response = self._raw_client.get_functions_function_id(function_id, request_options=request_options)
        return _response.data

    def delete_functions_function_id(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_functions_function_id(
            function_id="functionId",
        )
        """
        _response = self._raw_client.delete_functions_function_id(function_id, request_options=request_options)
        return _response.data

    def patch_functions_function_id(
        self,
        function_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_functions_function_id(
            function_id="functionId",
        )
        """
        _response = self._raw_client.patch_functions_function_id(
            function_id, metadata=metadata, name=name, description=description, request_options=request_options
        )
        return _response.data

    def get_hooks(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hooks:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hooks
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_hooks()
        """
        _response = self._raw_client.get_hooks(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_hooks(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        false_action_id: typing.Optional[str] = OMIT,
        true_action_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[PostHooksTrigger] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hook:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        false_action_id : typing.Optional[str]

        true_action_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[PostHooksTrigger]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_hooks()
        """
        _response = self._raw_client.post_hooks(
            metadata=metadata,
            function_id=function_id,
            false_action_id=false_action_id,
            true_action_id=true_action_id,
            name=name,
            description=description,
            trigger=trigger,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_hooks_hook_id(self, hook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_hooks_hook_id(
            hook_id="hookId",
        )
        """
        _response = self._raw_client.get_hooks_hook_id(hook_id, request_options=request_options)
        return _response.data

    def delete_hooks_hook_id(self, hook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_hooks_hook_id(
            hook_id="hookId",
        )
        """
        _response = self._raw_client.delete_hooks_hook_id(hook_id, request_options=request_options)
        return _response.data

    def patch_hooks_hook_id(
        self,
        hook_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        false_action_id: typing.Optional[str] = OMIT,
        true_action_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[PatchHookIdTrigger] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        false_action_id : typing.Optional[str]

        true_action_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[PatchHookIdTrigger]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_hooks_hook_id(
            hook_id="hookId",
        )
        """
        _response = self._raw_client.patch_hooks_hook_id(
            hook_id,
            metadata=metadata,
            function_id=function_id,
            false_action_id=false_action_id,
            true_action_id=true_action_id,
            name=name,
            description=description,
            trigger=trigger,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_hooks_hook_id_runs(
        self,
        hook_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRuns:
        """
        Parameters
        ----------
        hook_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRuns
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_hooks_hook_id_runs(
            hook_id="hookId",
        )
        """
        _response = self._raw_client.get_hooks_hook_id_runs(
            hook_id, status=status, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_hooks_hook_id_runs(
        self,
        hook_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_hooks_hook_id_runs(
            hook_id="hookId",
        )
        """
        _response = self._raw_client.post_hooks_hook_id_runs(
            hook_id,
            input=input,
            metadata=metadata,
            name=name,
            description=description,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    def get_hooks_hook_id_runs_run_id(
        self, hook_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_hooks_hook_id_runs_run_id(
            hook_id="hookId",
            run_id="runId",
        )
        """
        _response = self._raw_client.get_hooks_hook_id_runs_run_id(hook_id, run_id, request_options=request_options)
        return _response.data

    def patch_hooks_hook_id_runs_run_id(
        self,
        hook_id: str,
        run_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[PatchHookRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        run_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[PatchHookRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_hooks_hook_id_runs_run_id(
            hook_id="hookId",
            run_id="runId",
        )
        """
        _response = self._raw_client.patch_hooks_hook_id_runs_run_id(
            hook_id, run_id, output=output, metadata=metadata, status=status, request_options=request_options
        )
        return _response.data

    def get_logs(
        self,
        *,
        workflow_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        transition_execution_id: typing.Optional[str] = None,
        transition_id: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        workflow_execution_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Logs:
        """
        Parameters
        ----------
        workflow_id : typing.Optional[str]

        next_token : typing.Optional[str]

        order : typing.Optional[str]

        transition_execution_id : typing.Optional[str]

        transition_id : typing.Optional[str]

        max_results : typing.Optional[str]

        workflow_execution_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Logs
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_logs()
        """
        _response = self._raw_client.get_logs(
            workflow_id=workflow_id,
            next_token=next_token,
            order=order,
            transition_execution_id=transition_execution_id,
            transition_id=transition_id,
            max_results=max_results,
            workflow_execution_id=workflow_execution_id,
            request_options=request_options,
        )
        return _response.data

    def get_logs_log_id(self, log_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Log:
        """
        Parameters
        ----------
        log_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Log
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_logs_log_id(
            log_id="logId",
        )
        """
        _response = self._raw_client.get_logs_log_id(log_id, request_options=request_options)
        return _response.data

    def get_models(
        self,
        *,
        owner: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Models:
        """
        Parameters
        ----------
        owner : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Models
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_models()
        """
        _response = self._raw_client.get_models(
            owner=owner, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_models(
        self,
        *,
        field_config: typing.Dict[str, typing.Any],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        confidence_version: typing.Optional[PostModelsConfidenceVersion] = OMIT,
        llm_version: typing.Optional[PostModelsLlmVersion] = OMIT,
        preprocess_config: typing.Optional[PostModelsPreprocessConfig] = OMIT,
        postprocess_config: typing.Optional[PostModelsPostprocessConfig] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        field_config : typing.Dict[str, typing.Any]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        confidence_version : typing.Optional[PostModelsConfidenceVersion]

        llm_version : typing.Optional[PostModelsLlmVersion]

        preprocess_config : typing.Optional[PostModelsPreprocessConfig]

        postprocess_config : typing.Optional[PostModelsPostprocessConfig]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_models(
            field_config={"key": "value"},
        )
        """
        _response = self._raw_client.post_models(
            field_config=field_config,
            metadata=metadata,
            confidence_version=confidence_version,
            llm_version=llm_version,
            preprocess_config=preprocess_config,
            postprocess_config=postprocess_config,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_models_model_id(
        self,
        model_id: str,
        *,
        statistics_last_n_days: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        statistics_last_n_days : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_models_model_id(
            model_id="modelId",
        )
        """
        _response = self._raw_client.get_models_model_id(
            model_id, statistics_last_n_days=statistics_last_n_days, request_options=request_options
        )
        return _response.data

    def delete_models_model_id(
        self, model_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_models_model_id(
            model_id="modelId",
        )
        """
        _response = self._raw_client.delete_models_model_id(model_id, request_options=request_options)
        return _response.data

    def patch_models_model_id(
        self,
        model_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        confidence_version: typing.Optional[PatchModelIdConfidenceVersion] = OMIT,
        llm_version: typing.Optional[PatchModelIdLlmVersion] = OMIT,
        preprocess_config: typing.Optional[PatchModelIdPreprocessConfig] = OMIT,
        training_id: typing.Optional[str] = OMIT,
        postprocess_config: typing.Optional[PatchModelIdPostprocessConfig] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        field_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        confidence_version : typing.Optional[PatchModelIdConfidenceVersion]

        llm_version : typing.Optional[PatchModelIdLlmVersion]

        preprocess_config : typing.Optional[PatchModelIdPreprocessConfig]

        training_id : typing.Optional[str]

        postprocess_config : typing.Optional[PatchModelIdPostprocessConfig]

        name : typing.Optional[str]

        description : typing.Optional[str]

        field_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_models_model_id(
            model_id="modelId",
        )
        """
        _response = self._raw_client.patch_models_model_id(
            model_id,
            metadata=metadata,
            confidence_version=confidence_version,
            llm_version=llm_version,
            preprocess_config=preprocess_config,
            training_id=training_id,
            postprocess_config=postprocess_config,
            name=name,
            description=description,
            field_config=field_config,
            request_options=request_options,
        )
        return _response.data

    def get_organizations(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organizations:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organizations
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_organizations()
        """
        _response = self._raw_client.get_organizations(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_organizations(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        use_new_scopes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        url : typing.Optional[str]

        use_new_scopes : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_organizations()
        """
        _response = self._raw_client.post_organizations(
            metadata=metadata,
            name=name,
            description=description,
            url=url,
            use_new_scopes=use_new_scopes,
            request_options=request_options,
        )
        return _response.data

    def get_organizations_organization_id(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_organizations_organization_id(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_organizations_organization_id(organization_id, request_options=request_options)
        return _response.data

    def patch_organizations_organization_id(
        self,
        organization_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        document_retention_in_days: typing.Optional[int] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        payment_method_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        document_retention_in_days : typing.Optional[int]

        plan_id : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_organizations_organization_id(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.patch_organizations_organization_id(
            organization_id,
            metadata=metadata,
            payment_method_id=payment_method_id,
            name=name,
            description=description,
            document_retention_in_days=document_retention_in_days,
            plan_id=plan_id,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def get_predictions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Predictions:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        order : typing.Optional[str]

        model_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Predictions
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_predictions()
        """
        _response = self._raw_client.get_predictions(
            next_token=next_token,
            max_results=max_results,
            sort_by=sort_by,
            order=order,
            model_id=model_id,
            request_options=request_options,
        )
        return _response.data

    def post_predictions(
        self,
        *,
        model_id: str,
        document_id: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        training_id: typing.Optional[str] = OMIT,
        postprocess_config: typing.Optional[PostPredictionsPostprocessConfig] = OMIT,
        rotation: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        preprocess_config: typing.Optional[PostPredictionsPreprocessConfig] = OMIT,
        max_pages: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        auto_rotate: typing.Optional[bool] = OMIT,
        image_quality: typing.Optional[PostPredictionsImageQuality] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prediction:
        """
        Parameters
        ----------
        model_id : str

        document_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        training_id : typing.Optional[str]

        postprocess_config : typing.Optional[PostPredictionsPostprocessConfig]

        rotation : typing.Optional[int]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        async_ : typing.Optional[bool]

        preprocess_config : typing.Optional[PostPredictionsPreprocessConfig]

        max_pages : typing.Optional[int]

        name : typing.Optional[str]

        auto_rotate : typing.Optional[bool]

        image_quality : typing.Optional[PostPredictionsImageQuality]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prediction
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_predictions(
            model_id="modelId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.post_predictions(
            model_id=model_id,
            document_id=document_id,
            metadata=metadata,
            training_id=training_id,
            postprocess_config=postprocess_config,
            rotation=rotation,
            description=description,
            agent_run_id=agent_run_id,
            async_=async_,
            preprocess_config=preprocess_config,
            max_pages=max_pages,
            name=name,
            auto_rotate=auto_rotate,
            image_quality=image_quality,
            request_options=request_options,
        )
        return _response.data

    def get_predictions_prediction_id(
        self, prediction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Prediction:
        """
        Parameters
        ----------
        prediction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prediction
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_predictions_prediction_id(
            prediction_id="predictionId",
        )
        """
        _response = self._raw_client.get_predictions_prediction_id(prediction_id, request_options=request_options)
        return _response.data

    def get_roles(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Roles:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Roles
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_roles()
        """
        _response = self._raw_client.get_roles(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_roles(
        self,
        *,
        permissions: typing.Sequence[PostRolesPermissionsItem],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Parameters
        ----------
        permissions : typing.Sequence[PostRolesPermissionsItem]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        from fern import (
            FernApi,
            PostRolesPermissionsItem,
            PostRolesPermissionsItemAction,
            PostRolesPermissionsItemEffect,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_roles(
            permissions=[
                PostRolesPermissionsItem(
                    resource_id="resourceId",
                    effect=PostRolesPermissionsItemEffect.ALLOW,
                    action=PostRolesPermissionsItemAction.READ,
                )
            ],
        )
        """
        _response = self._raw_client.post_roles(
            permissions=permissions,
            metadata=metadata,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_roles_role_id(self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Parameters
        ----------
        role_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_roles_role_id(
            role_id="roleId",
        )
        """
        _response = self._raw_client.get_roles_role_id(role_id, request_options=request_options)
        return _response.data

    def delete_roles_role_id(self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Parameters
        ----------
        role_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_roles_role_id(
            role_id="roleId",
        )
        """
        _response = self._raw_client.delete_roles_role_id(role_id, request_options=request_options)
        return _response.data

    def patch_roles_role_id(
        self,
        role_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        permissions: typing.Optional[typing.Sequence[PatchRoleIdPermissionsItem]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Parameters
        ----------
        role_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        permissions : typing.Optional[typing.Sequence[PatchRoleIdPermissionsItem]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_roles_role_id(
            role_id="roleId",
        )
        """
        _response = self._raw_client.patch_roles_role_id(
            role_id,
            metadata=metadata,
            permissions=permissions,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_users(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Users:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Users
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_users()
        """
        _response = self._raw_client.get_users(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_users(
        self,
        *,
        email: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        app_client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        email : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        role_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        app_client_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_users(
            email="email",
        )
        """
        _response = self._raw_client.post_users(
            email=email,
            metadata=metadata,
            role_ids=role_ids,
            name=name,
            description=description,
            app_client_id=app_client_id,
            request_options=request_options,
        )
        return _response.data

    def get_users_user_id(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_users_user_id(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_users_user_id(user_id, request_options=request_options)
        return _response.data

    def delete_users_user_id(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_users_user_id(
            user_id="userId",
        )
        """
        _response = self._raw_client.delete_users_user_id(user_id, request_options=request_options)
        return _response.data

    def patch_users_user_id(
        self,
        user_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        user_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        role_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_users_user_id(
            user_id="userId",
        )
        """
        _response = self._raw_client.patch_users_user_id(
            user_id,
            metadata=metadata,
            role_ids=role_ids,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_validations(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validations:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validations
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_validations()
        """
        _response = self._raw_client.get_validations(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    def post_validations(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validation:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_validations()
        """
        _response = self._raw_client.post_validations(
            metadata=metadata,
            name=name,
            description=description,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_validations_validation_id(
        self, validation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_validations_validation_id(
            validation_id="validationId",
        )
        """
        _response = self._raw_client.get_validations_validation_id(validation_id, request_options=request_options)
        return _response.data

    def delete_validations_validation_id(
        self, validation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_validations_validation_id(
            validation_id="validationId",
        )
        """
        _response = self._raw_client.delete_validations_validation_id(validation_id, request_options=request_options)
        return _response.data

    def patch_validations_validation_id(
        self,
        validation_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_validations_validation_id(
            validation_id="validationId",
        )
        """
        _response = self._raw_client.patch_validations_validation_id(
            validation_id,
            metadata=metadata,
            name=name,
            description=description,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def get_validations_validation_id_tasks(
        self,
        validation_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTasks:
        """
        Parameters
        ----------
        validation_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTasks
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_validations_validation_id_tasks(
            validation_id="validationId",
        )
        """
        _response = self._raw_client.get_validations_validation_id_tasks(
            validation_id,
            status=status,
            next_token=next_token,
            max_results=max_results,
            request_options=request_options,
        )
        return _response.data

    def post_validations_validation_id_tasks(
        self,
        validation_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.post_validations_validation_id_tasks(
            validation_id="validationId",
        )
        """
        _response = self._raw_client.post_validations_validation_id_tasks(
            validation_id,
            input=input,
            metadata=metadata,
            name=name,
            description=description,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    def get_validations_validation_id_tasks_task_id(
        self, validation_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_validations_validation_id_tasks_task_id(
            validation_id="validationId",
            task_id="taskId",
        )
        """
        _response = self._raw_client.get_validations_validation_id_tasks_task_id(
            validation_id, task_id, request_options=request_options
        )
        return _response.data

    def patch_validations_validation_id_tasks_task_id(
        self,
        validation_id: str,
        task_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[PatchValidationTaskIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        task_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[PatchValidationTaskIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.patch_validations_validation_id_tasks_task_id(
            validation_id="validationId",
            task_id="taskId",
        )
        """
        _response = self._raw_client.patch_validations_validation_id_tasks_task_id(
            validation_id,
            task_id,
            output=output,
            metadata=metadata,
            name=name,
            description=description,
            status=status,
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



        Defaults to FernApiEnvironment.DEFAULT



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to 'v1'.

    token : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
        if base_path is not None:
            _base_path = base_path if base_path is not None else "v1"
            base_url = "https://api.cradl.ai/{basePath}".format(basePath=_base_path)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            async_token=async_token,
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

    async def get_actions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Actions:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Actions
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_actions(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        secret_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Action:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        connection_id : typing.Optional[str]

        secret_id : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_actions(
            metadata=metadata,
            function_id=function_id,
            name=name,
            description=description,
            connection_id=connection_id,
            secret_id=secret_id,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_actions_action_id(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_actions_action_id(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions_action_id(action_id, request_options=request_options)
        return _response.data

    async def delete_actions_action_id(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_actions_action_id(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_actions_action_id(action_id, request_options=request_options)
        return _response.data

    async def patch_actions_action_id(
        self,
        action_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        secret_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        connection_id : typing.Optional[str]

        secret_id : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_actions_action_id(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_actions_action_id(
            action_id,
            metadata=metadata,
            function_id=function_id,
            name=name,
            description=description,
            connection_id=connection_id,
            secret_id=secret_id,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_actions_action_id_runs(
        self,
        action_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRuns:
        """
        Parameters
        ----------
        action_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRuns
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_actions_action_id_runs(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions_action_id_runs(
            action_id, status=status, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_actions_action_id_runs(
        self,
        action_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        no_agent_run_update: typing.Optional[bool] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        no_agent_run_update : typing.Optional[bool]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_actions_action_id_runs(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_actions_action_id_runs(
            action_id,
            input=input,
            metadata=metadata,
            no_agent_run_update=no_agent_run_update,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    async def get_actions_action_id_runs_run_id(
        self, action_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_actions_action_id_runs_run_id(
                action_id="actionId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions_action_id_runs_run_id(
            action_id, run_id, request_options=request_options
        )
        return _response.data

    async def patch_actions_action_id_runs_run_id(
        self,
        action_id: str,
        run_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[PatchActionRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionRun:
        """
        Parameters
        ----------
        action_id : str

        run_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[PatchActionRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_actions_action_id_runs_run_id(
                action_id="actionId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_actions_action_id_runs_run_id(
            action_id, run_id, output=output, metadata=metadata, status=status, request_options=request_options
        )
        return _response.data

    async def get_agents(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agents:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agents
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_agents(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        resource_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        resource_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_agents(
            metadata=metadata,
            name=name,
            description=description,
            resource_ids=resource_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_agents_agent_id(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_agents_agent_id(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_agent_id(agent_id, request_options=request_options)
        return _response.data

    async def delete_agents_agent_id(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_agents_agent_id(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_agents_agent_id(agent_id, request_options=request_options)
        return _response.data

    async def patch_agents_agent_id(
        self,
        agent_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        resource_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        agent_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        resource_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_agents_agent_id(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_agents_agent_id(
            agent_id,
            metadata=metadata,
            name=name,
            description=description,
            resource_ids=resource_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_agents_agent_id_runs(
        self,
        agent_id: str,
        *,
        history: typing.Optional[str] = None,
        created_time_after: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        updated_time_after: typing.Optional[str] = None,
        created_time_before: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        updated_time_before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRuns:
        """
        Parameters
        ----------
        agent_id : str

        history : typing.Optional[str]

        created_time_after : typing.Optional[str]

        next_token : typing.Optional[str]

        sort : typing.Optional[str]

        updated_time_after : typing.Optional[str]

        created_time_before : typing.Optional[str]

        status : typing.Optional[str]

        max_results : typing.Optional[str]

        updated_time_before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRuns
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_agents_agent_id_runs(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_agent_id_runs(
            agent_id,
            history=history,
            created_time_after=created_time_after,
            next_token=next_token,
            sort=sort,
            updated_time_after=updated_time_after,
            created_time_before=created_time_before,
            status=status,
            max_results=max_results,
            updated_time_before=updated_time_before,
            request_options=request_options,
        )
        return _response.data

    async def post_agents_agent_id_runs(
        self,
        agent_id: str,
        *,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        variables : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_agents_agent_id_runs(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_agents_agent_id_runs(
            agent_id, variables=variables, request_options=request_options
        )
        return _response.data

    async def get_agents_agent_id_runs_run_id(
        self, agent_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_agents_agent_id_runs_run_id(
                agent_id="agentId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_agent_id_runs_run_id(
            agent_id, run_id, request_options=request_options
        )
        return _response.data

    async def delete_agents_agent_id_runs_run_id(
        self, agent_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_agents_agent_id_runs_run_id(
                agent_id="agentId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_agents_agent_id_runs_run_id(
            agent_id, run_id, request_options=request_options
        )
        return _response.data

    async def patch_agents_agent_id_runs_run_id(
        self,
        agent_id: str,
        run_id: str,
        *,
        status: typing.Optional[PatchAgentRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRun:
        """
        Parameters
        ----------
        agent_id : str

        run_id : str

        status : typing.Optional[PatchAgentRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_agents_agent_id_runs_run_id(
                agent_id="agentId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_agents_agent_id_runs_run_id(
            agent_id, run_id, status=status, request_options=request_options
        )
        return _response.data

    async def get_agents_agent_id_statistics(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentStatistics:
        """
        Parameters
        ----------
        agent_id : str

        before : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentStatistics
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_agents_agent_id_statistics(
                agent_id="agentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_agent_id_statistics(
            agent_id, before=before, after=after, request_options=request_options
        )
        return _response.data

    async def get_documents(
        self,
        *,
        dataset_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        document_id: typing.Optional[str] = None,
        consent_id: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Documents:
        """
        Parameters
        ----------
        dataset_id : typing.Optional[str]

        next_token : typing.Optional[str]

        order : typing.Optional[str]

        document_id : typing.Optional[str]

        consent_id : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Documents
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_documents()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_documents(
            dataset_id=dataset_id,
            next_token=next_token,
            order=order,
            document_id=document_id,
            consent_id=consent_id,
            max_results=max_results,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def post_documents(
        self,
        *,
        ground_truth: typing.Optional[typing.Sequence[PostDocumentsGroundTruthItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        consent_id: typing.Optional[str] = OMIT,
        retention_in_days: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        content_type: typing.Optional[PostDocumentsContentType] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        ground_truth : typing.Optional[typing.Sequence[PostDocumentsGroundTruthItem]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        consent_id : typing.Optional[str]

        retention_in_days : typing.Optional[int]

        name : typing.Optional[str]

        description : typing.Optional[str]

        dataset_id : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        content_type : typing.Optional[PostDocumentsContentType]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_documents()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_documents(
            ground_truth=ground_truth,
            metadata=metadata,
            consent_id=consent_id,
            retention_in_days=retention_in_days,
            name=name,
            description=description,
            dataset_id=dataset_id,
            agent_run_id=agent_run_id,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        return _response.data

    async def delete_documents(
        self,
        *,
        consent_id: typing.Optional[str] = None,
        dataset_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Documents:
        """
        Parameters
        ----------
        consent_id : typing.Optional[str]

        dataset_id : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Documents
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_documents()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_documents(
            consent_id=consent_id,
            dataset_id=dataset_id,
            next_token=next_token,
            max_results=max_results,
            request_options=request_options,
        )
        return _response.data

    async def get_documents_document_id(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_documents_document_id(
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_documents_document_id(document_id, request_options=request_options)
        return _response.data

    async def delete_documents_document_id(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_documents_document_id(
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_documents_document_id(document_id, request_options=request_options)
        return _response.data

    async def patch_documents_document_id(
        self,
        document_id: str,
        *,
        ground_truth: typing.Optional[typing.Sequence[PatchDocumentIdGroundTruthItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        retention_in_days: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        document_id : str

        ground_truth : typing.Optional[typing.Sequence[PatchDocumentIdGroundTruthItem]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        retention_in_days : typing.Optional[int]

        name : typing.Optional[str]

        description : typing.Optional[str]

        dataset_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_documents_document_id(
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_documents_document_id(
            document_id,
            ground_truth=ground_truth,
            metadata=metadata,
            retention_in_days=retention_in_days,
            name=name,
            description=description,
            dataset_id=dataset_id,
            request_options=request_options,
        )
        return _response.data

    async def get_functions(
        self,
        *,
        owner: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Functions:
        """
        Parameters
        ----------
        owner : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        order : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Functions
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_functions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_functions(
            owner=owner,
            next_token=next_token,
            max_results=max_results,
            sort_by=sort_by,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def post_functions(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        runtime: typing.Optional[PostFunctionsRuntime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        runtime : typing.Optional[PostFunctionsRuntime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_functions()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_functions(
            metadata=metadata, name=name, description=description, runtime=runtime, request_options=request_options
        )
        return _response.data

    async def get_functions_function_id(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_functions_function_id(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_functions_function_id(function_id, request_options=request_options)
        return _response.data

    async def delete_functions_function_id(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_functions_function_id(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_functions_function_id(function_id, request_options=request_options)
        return _response.data

    async def patch_functions_function_id(
        self,
        function_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """
        Parameters
        ----------
        function_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_functions_function_id(
                function_id="functionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_functions_function_id(
            function_id, metadata=metadata, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def get_hooks(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hooks:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hooks
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_hooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hooks(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_hooks(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        false_action_id: typing.Optional[str] = OMIT,
        true_action_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[PostHooksTrigger] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hook:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        false_action_id : typing.Optional[str]

        true_action_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[PostHooksTrigger]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_hooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_hooks(
            metadata=metadata,
            function_id=function_id,
            false_action_id=false_action_id,
            true_action_id=true_action_id,
            name=name,
            description=description,
            trigger=trigger,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_hooks_hook_id(self, hook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_hooks_hook_id(
                hook_id="hookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hooks_hook_id(hook_id, request_options=request_options)
        return _response.data

    async def delete_hooks_hook_id(
        self, hook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_hooks_hook_id(
                hook_id="hookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_hooks_hook_id(hook_id, request_options=request_options)
        return _response.data

    async def patch_hooks_hook_id(
        self,
        hook_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        function_id: typing.Optional[str] = OMIT,
        false_action_id: typing.Optional[str] = OMIT,
        true_action_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[PatchHookIdTrigger] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Hook:
        """
        Parameters
        ----------
        hook_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        function_id : typing.Optional[str]

        false_action_id : typing.Optional[str]

        true_action_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[PatchHookIdTrigger]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Hook
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_hooks_hook_id(
                hook_id="hookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_hooks_hook_id(
            hook_id,
            metadata=metadata,
            function_id=function_id,
            false_action_id=false_action_id,
            true_action_id=true_action_id,
            name=name,
            description=description,
            trigger=trigger,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_hooks_hook_id_runs(
        self,
        hook_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRuns:
        """
        Parameters
        ----------
        hook_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRuns
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_hooks_hook_id_runs(
                hook_id="hookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hooks_hook_id_runs(
            hook_id, status=status, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_hooks_hook_id_runs(
        self,
        hook_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_hooks_hook_id_runs(
                hook_id="hookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_hooks_hook_id_runs(
            hook_id,
            input=input,
            metadata=metadata,
            name=name,
            description=description,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    async def get_hooks_hook_id_runs_run_id(
        self, hook_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_hooks_hook_id_runs_run_id(
                hook_id="hookId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hooks_hook_id_runs_run_id(
            hook_id, run_id, request_options=request_options
        )
        return _response.data

    async def patch_hooks_hook_id_runs_run_id(
        self,
        hook_id: str,
        run_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[PatchHookRunIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HookRun:
        """
        Parameters
        ----------
        hook_id : str

        run_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        status : typing.Optional[PatchHookRunIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HookRun
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_hooks_hook_id_runs_run_id(
                hook_id="hookId",
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_hooks_hook_id_runs_run_id(
            hook_id, run_id, output=output, metadata=metadata, status=status, request_options=request_options
        )
        return _response.data

    async def get_logs(
        self,
        *,
        workflow_id: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        transition_execution_id: typing.Optional[str] = None,
        transition_id: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        workflow_execution_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Logs:
        """
        Parameters
        ----------
        workflow_id : typing.Optional[str]

        next_token : typing.Optional[str]

        order : typing.Optional[str]

        transition_execution_id : typing.Optional[str]

        transition_id : typing.Optional[str]

        max_results : typing.Optional[str]

        workflow_execution_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Logs
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs(
            workflow_id=workflow_id,
            next_token=next_token,
            order=order,
            transition_execution_id=transition_execution_id,
            transition_id=transition_id,
            max_results=max_results,
            workflow_execution_id=workflow_execution_id,
            request_options=request_options,
        )
        return _response.data

    async def get_logs_log_id(self, log_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Log:
        """
        Parameters
        ----------
        log_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Log
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_logs_log_id(
                log_id="logId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs_log_id(log_id, request_options=request_options)
        return _response.data

    async def get_models(
        self,
        *,
        owner: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Models:
        """
        Parameters
        ----------
        owner : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Models
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_models(
            owner=owner, next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_models(
        self,
        *,
        field_config: typing.Dict[str, typing.Any],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        confidence_version: typing.Optional[PostModelsConfidenceVersion] = OMIT,
        llm_version: typing.Optional[PostModelsLlmVersion] = OMIT,
        preprocess_config: typing.Optional[PostModelsPreprocessConfig] = OMIT,
        postprocess_config: typing.Optional[PostModelsPostprocessConfig] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        field_config : typing.Dict[str, typing.Any]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        confidence_version : typing.Optional[PostModelsConfidenceVersion]

        llm_version : typing.Optional[PostModelsLlmVersion]

        preprocess_config : typing.Optional[PostModelsPreprocessConfig]

        postprocess_config : typing.Optional[PostModelsPostprocessConfig]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_models(
                field_config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_models(
            field_config=field_config,
            metadata=metadata,
            confidence_version=confidence_version,
            llm_version=llm_version,
            preprocess_config=preprocess_config,
            postprocess_config=postprocess_config,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_models_model_id(
        self,
        model_id: str,
        *,
        statistics_last_n_days: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        statistics_last_n_days : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_models_model_id(
                model_id="modelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_models_model_id(
            model_id, statistics_last_n_days=statistics_last_n_days, request_options=request_options
        )
        return _response.data

    async def delete_models_model_id(
        self, model_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_models_model_id(
                model_id="modelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_models_model_id(model_id, request_options=request_options)
        return _response.data

    async def patch_models_model_id(
        self,
        model_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        confidence_version: typing.Optional[PatchModelIdConfidenceVersion] = OMIT,
        llm_version: typing.Optional[PatchModelIdLlmVersion] = OMIT,
        preprocess_config: typing.Optional[PatchModelIdPreprocessConfig] = OMIT,
        training_id: typing.Optional[str] = OMIT,
        postprocess_config: typing.Optional[PatchModelIdPostprocessConfig] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        field_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        confidence_version : typing.Optional[PatchModelIdConfidenceVersion]

        llm_version : typing.Optional[PatchModelIdLlmVersion]

        preprocess_config : typing.Optional[PatchModelIdPreprocessConfig]

        training_id : typing.Optional[str]

        postprocess_config : typing.Optional[PatchModelIdPostprocessConfig]

        name : typing.Optional[str]

        description : typing.Optional[str]

        field_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_models_model_id(
                model_id="modelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_models_model_id(
            model_id,
            metadata=metadata,
            confidence_version=confidence_version,
            llm_version=llm_version,
            preprocess_config=preprocess_config,
            training_id=training_id,
            postprocess_config=postprocess_config,
            name=name,
            description=description,
            field_config=field_config,
            request_options=request_options,
        )
        return _response.data

    async def get_organizations(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organizations:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organizations
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_organizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organizations(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_organizations(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        use_new_scopes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        url : typing.Optional[str]

        use_new_scopes : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_organizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_organizations(
            metadata=metadata,
            name=name,
            description=description,
            url=url,
            use_new_scopes=use_new_scopes,
            request_options=request_options,
        )
        return _response.data

    async def get_organizations_organization_id(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_organizations_organization_id(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organizations_organization_id(
            organization_id, request_options=request_options
        )
        return _response.data

    async def patch_organizations_organization_id(
        self,
        organization_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        document_retention_in_days: typing.Optional[int] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        payment_method_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        document_retention_in_days : typing.Optional[int]

        plan_id : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_organizations_organization_id(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_organizations_organization_id(
            organization_id,
            metadata=metadata,
            payment_method_id=payment_method_id,
            name=name,
            description=description,
            document_retention_in_days=document_retention_in_days,
            plan_id=plan_id,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def get_predictions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Predictions:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        sort_by : typing.Optional[str]

        order : typing.Optional[str]

        model_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Predictions
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_predictions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_predictions(
            next_token=next_token,
            max_results=max_results,
            sort_by=sort_by,
            order=order,
            model_id=model_id,
            request_options=request_options,
        )
        return _response.data

    async def post_predictions(
        self,
        *,
        model_id: str,
        document_id: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        training_id: typing.Optional[str] = OMIT,
        postprocess_config: typing.Optional[PostPredictionsPostprocessConfig] = OMIT,
        rotation: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        preprocess_config: typing.Optional[PostPredictionsPreprocessConfig] = OMIT,
        max_pages: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        auto_rotate: typing.Optional[bool] = OMIT,
        image_quality: typing.Optional[PostPredictionsImageQuality] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prediction:
        """
        Parameters
        ----------
        model_id : str

        document_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        training_id : typing.Optional[str]

        postprocess_config : typing.Optional[PostPredictionsPostprocessConfig]

        rotation : typing.Optional[int]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        async_ : typing.Optional[bool]

        preprocess_config : typing.Optional[PostPredictionsPreprocessConfig]

        max_pages : typing.Optional[int]

        name : typing.Optional[str]

        auto_rotate : typing.Optional[bool]

        image_quality : typing.Optional[PostPredictionsImageQuality]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prediction
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_predictions(
                model_id="modelId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_predictions(
            model_id=model_id,
            document_id=document_id,
            metadata=metadata,
            training_id=training_id,
            postprocess_config=postprocess_config,
            rotation=rotation,
            description=description,
            agent_run_id=agent_run_id,
            async_=async_,
            preprocess_config=preprocess_config,
            max_pages=max_pages,
            name=name,
            auto_rotate=auto_rotate,
            image_quality=image_quality,
            request_options=request_options,
        )
        return _response.data

    async def get_predictions_prediction_id(
        self, prediction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Prediction:
        """
        Parameters
        ----------
        prediction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prediction
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_predictions_prediction_id(
                prediction_id="predictionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_predictions_prediction_id(prediction_id, request_options=request_options)
        return _response.data

    async def get_roles(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Roles:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Roles
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_roles(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_roles(
        self,
        *,
        permissions: typing.Sequence[PostRolesPermissionsItem],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Parameters
        ----------
        permissions : typing.Sequence[PostRolesPermissionsItem]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostRolesPermissionsItem,
            PostRolesPermissionsItemAction,
            PostRolesPermissionsItemEffect,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_roles(
                permissions=[
                    PostRolesPermissionsItem(
                        resource_id="resourceId",
                        effect=PostRolesPermissionsItemEffect.ALLOW,
                        action=PostRolesPermissionsItemAction.READ,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_roles(
            permissions=permissions,
            metadata=metadata,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_roles_role_id(self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """
        Parameters
        ----------
        role_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_roles_role_id(
                role_id="roleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_roles_role_id(role_id, request_options=request_options)
        return _response.data

    async def delete_roles_role_id(
        self, role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Role:
        """
        Parameters
        ----------
        role_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_roles_role_id(
                role_id="roleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_roles_role_id(role_id, request_options=request_options)
        return _response.data

    async def patch_roles_role_id(
        self,
        role_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        permissions: typing.Optional[typing.Sequence[PatchRoleIdPermissionsItem]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Parameters
        ----------
        role_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        permissions : typing.Optional[typing.Sequence[PatchRoleIdPermissionsItem]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_roles_role_id(
                role_id="roleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_roles_role_id(
            role_id,
            metadata=metadata,
            permissions=permissions,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_users(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Users:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Users
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_users(
        self,
        *,
        email: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        app_client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        email : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        role_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        app_client_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_users(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users(
            email=email,
            metadata=metadata,
            role_ids=role_ids,
            name=name,
            description=description,
            app_client_id=app_client_id,
            request_options=request_options,
        )
        return _response.data

    async def get_users_user_id(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_users_user_id(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_user_id(user_id, request_options=request_options)
        return _response.data

    async def delete_users_user_id(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_users_user_id(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_users_user_id(user_id, request_options=request_options)
        return _response.data

    async def patch_users_user_id(
        self,
        user_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        user_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        role_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_users_user_id(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_users_user_id(
            user_id,
            metadata=metadata,
            role_ids=role_ids,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_validations(
        self,
        *,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validations:
        """
        Parameters
        ----------
        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validations
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_validations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validations(
            next_token=next_token, max_results=max_results, request_options=request_options
        )
        return _response.data

    async def post_validations(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validation:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_validations()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validations(
            metadata=metadata,
            name=name,
            description=description,
            config=config,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_validations_validation_id(
        self, validation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_validations_validation_id(
                validation_id="validationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validations_validation_id(validation_id, request_options=request_options)
        return _response.data

    async def delete_validations_validation_id(
        self, validation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_validations_validation_id(
                validation_id="validationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_validations_validation_id(
            validation_id, request_options=request_options
        )
        return _response.data

    async def patch_validations_validation_id(
        self,
        validation_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Validation:
        """
        Parameters
        ----------
        validation_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Validation
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_validations_validation_id(
                validation_id="validationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_validations_validation_id(
            validation_id,
            metadata=metadata,
            name=name,
            description=description,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def get_validations_validation_id_tasks(
        self,
        validation_id: str,
        *,
        status: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTasks:
        """
        Parameters
        ----------
        validation_id : str

        status : typing.Optional[str]

        next_token : typing.Optional[str]

        max_results : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTasks
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_validations_validation_id_tasks(
                validation_id="validationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validations_validation_id_tasks(
            validation_id,
            status=status,
            next_token=next_token,
            max_results=max_results,
            request_options=request_options,
        )
        return _response.data

    async def post_validations_validation_id_tasks(
        self,
        validation_id: str,
        *,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        agent_run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        input : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        agent_run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_validations_validation_id_tasks(
                validation_id="validationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_validations_validation_id_tasks(
            validation_id,
            input=input,
            metadata=metadata,
            name=name,
            description=description,
            agent_run_id=agent_run_id,
            request_options=request_options,
        )
        return _response.data

    async def get_validations_validation_id_tasks_task_id(
        self, validation_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_validations_validation_id_tasks_task_id(
                validation_id="validationId",
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validations_validation_id_tasks_task_id(
            validation_id, task_id, request_options=request_options
        )
        return _response.data

    async def patch_validations_validation_id_tasks_task_id(
        self,
        validation_id: str,
        task_id: str,
        *,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[PatchValidationTaskIdStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationTask:
        """
        Parameters
        ----------
        validation_id : str

        task_id : str

        output : typing.Optional[typing.Dict[str, typing.Any]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[PatchValidationTaskIdStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationTask
            200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.patch_validations_validation_id_tasks_task_id(
                validation_id="validationId",
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_validations_validation_id_tasks_task_id(
            validation_id,
            task_id,
            output=output,
            metadata=metadata,
            name=name,
            description=description,
            status=status,
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
