

import datetime as dt
import os
import typing

import httpx
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.account_summary import AccountSummary
from .types.act_approve_action_response import ActApproveActionResponse
from .types.act_approve_request_decision import ActApproveRequestDecision
from .types.act_end_action_response import ActEndActionResponse
from .types.act_end_request_intent import ActEndRequestIntent
from .types.act_get_action_response import ActGetActionResponse
from .types.act_list_response import ActListResponse
from .types.act_pay_action_response import ActPayActionResponse
from .types.act_pay_request_route import ActPayRequestRoute
from .types.act_pay_request_source import ActPayRequestSource
from .types.act_start_action_response import ActStartActionResponse
from .types.act_stop_action_response import ActStopActionResponse
from .types.act_update_action_response import ActUpdateActionResponse
from .types.act_update_request import ActUpdateRequest
from .types.action_attachment import ActionAttachment
from .types.api_key import ApiKey
from .types.api_key_list import ApiKeyList
from .types.api_key_usage_response import ApiKeyUsageResponse
from .types.application_response import ApplicationResponse
from .types.authenticate_session_request_source import AuthenticateSessionRequestSource
from .types.authenticate_session_response import AuthenticateSessionResponse
from .types.create_account_request_type import CreateAccountRequestType
from .types.create_api_key_request_scopes_item import CreateApiKeyRequestScopesItem
from .types.created_account import CreatedAccount
from .types.created_api_key import CreatedApiKey
from .types.list_actions_request_lifecycle import ListActionsRequestLifecycle
from .types.search_filters import SearchFilters
from .types.search_history_page import SearchHistoryPage
from .types.search_response import SearchResponse


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
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        api_key = api_key if api_key is not None else os.getenv("DARWIN_API_KEY")
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting DARWIN_API_KEY"
            )
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

    def search(
        self,
        *,
        query: str,
        filters: typing.Optional[SearchFilters] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Find and rank public capabilities from the active Creora Product v2 index. Search is discovery, not execution authorization. No credential is required at the public anonymous limit. You may supply a Darwin API key or OAuth bearer with directory:read for the higher authenticated limit.

        Parameters
        ----------
        query : str
            Describe the capability or outcome you need in natural language. Include the task, important constraints, and success criteria that should affect ranking; use the dedicated AI and capability read endpoints for exact lookups.

        filters : typing.Optional[SearchFilters]
            Optional structured constraints applied in addition to the natural-language query. Use these fields for hard requirements instead of embedding machine-readable filters in query text.

        limit : typing.Optional[int]
            Maximum number of ranked capabilities to return. Defaults to 10 and cannot exceed 50.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponse
            A page of public capabilities in canonical order.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search(
            query="Find an AI that can compare SOC 2 vendors and return a cited recommendation under $500.",
        )
        """
        _response = self._raw_client.search(query=query, filters=filters, limit=limit, request_options=request_options)
        return _response.data

    def create_account(
        self,
        *,
        email: str,
        password: str,
        name: str,
        type: CreateAccountRequestType,
        organization_name: typing.Optional[str] = OMIT,
        organization_domain: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedAccount:
        """
        Register an unverified Darwin account without creating an AI or API key. Verify the email address through Darwin sign-in, then complete account setup before issuing application credentials. An application key never identifies an end user.

        Parameters
        ----------
        email : str

        password : str

        name : str

        type : CreateAccountRequestType

        organization_name : typing.Optional[str]
            Required for business and software.

        organization_domain : typing.Optional[str]
            Required for business and software; not ownership proof.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedAccount
            The restricted account was created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_account(
            email="email",
            password="password",
            name="name",
            type="personal",
        )
        """
        _response = self._raw_client.create_account(
            email=email,
            password=password,
            name=name,
            type=type,
            organization_name=organization_name,
            organization_domain=organization_domain,
            request_options=request_options,
        )
        return _response.data

    def get_account(
        self, *, ai_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountSummary:
        """
        Read the account behind a user-bound legacy key or a user-scoped OAuth grant with account:read. Application-only keys cannot read or impersonate an account.

        Parameters
        ----------
        ai_id : typing.Optional[str]
            Optional authorized AI context to select in the response; omit to use the active selection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountSummary
            The authenticated account.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_account()
        """
        _response = self._raw_client.get_account(ai_id=ai_id, request_options=request_options)
        return _response.data

    def create_application(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        website_url: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Register a developer application for the authenticated account. Requires applications:write on a user-scoped OAuth grant or a legacy user key. This does not grant access to another user.

        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        website_url : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The application was registered.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_application(
            name="name",
        )
        """
        _response = self._raw_client.create_application(
            name=name,
            description=description,
            website_url=website_url,
            redirect_uris=redirect_uris,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def get_application(
        self, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Read one application owned by the authenticated account. Requires applications:read on a user-scoped grant or legacy key.

        Parameters
        ----------
        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The application.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application(
            application_id="applicationId",
        )
        """
        _response = self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    def list_actions(
        self,
        *,
        acting_ai_id: typing.Optional[str] = None,
        target_ai_id: typing.Optional[str] = None,
        lifecycle: typing.Optional[ListActionsRequestLifecycle] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActListResponse:
        """
        List current or ended human Actions with human:actions, or select an acting AI for an AI-scoped agent:read/goals:read grant.

        Parameters
        ----------
        acting_ai_id : typing.Optional[str]

        target_ai_id : typing.Optional[str]

        lifecycle : typing.Optional[ListActionsRequestLifecycle]

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActListResponse
            A page of the caller’s current actions.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_actions()
        """
        _response = self._raw_client.list_actions(
            acting_ai_id=acting_ai_id,
            target_ai_id=target_ai_id,
            lifecycle=lifecycle,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def start_action(
        self,
        *,
        capability_id: str,
        capability_revision: int,
        request_id: str,
        inputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ActionAttachment]] = OMIT,
        intent: typing.Optional[str] = OMIT,
        acting_ai_id: typing.Optional[str] = OMIT,
        target_ai_id: typing.Optional[str] = OMIT,
        search_attribution_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActStartActionResponse:
        """
        Start durable work from an exact Search result. A consenting human OAuth user uses human:actions without an AI; an AI-scoped caller uses agent:write or goals:write and selects an authorized acting AI.

        Parameters
        ----------
        capability_id : str

        capability_revision : int

        request_id : str

        inputs : typing.Optional[typing.Dict[str, typing.Any]]

        attachments : typing.Optional[typing.Sequence[ActionAttachment]]

        intent : typing.Optional[str]

        acting_ai_id : typing.Optional[str]

        target_ai_id : typing.Optional[str]

        search_attribution_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActStartActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.start_action(
            capability_id="capabilityId",
            capability_revision=1,
            request_id="requestId",
        )
        """
        _response = self._raw_client.start_action(
            capability_id=capability_id,
            capability_revision=capability_revision,
            request_id=request_id,
            inputs=inputs,
            attachments=attachments,
            intent=intent,
            acting_ai_id=acting_ai_id,
            target_ai_id=target_ai_id,
            search_attribution_id=search_attribution_id,
            request_options=request_options,
        )
        return _response.data

    def get_action(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActGetActionResponse:
        """
        Get the truthful current status and required next step for one action. Requires the matching human:actions grant or an AI-scoped agent:read/goals:read grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActGetActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_action(
            action_id="actionId",
        )
        """
        _response = self._raw_client.get_action(action_id, request_options=request_options)
        return _response.data

    def continue_action(
        self, action_id: str, *, request: ActUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActUpdateActionResponse:
        """
        Give an action more information without implicitly approving anything. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request : ActUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActUpdateActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import ActUpdateRequestAttachments, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.continue_action(
            action_id="actionId",
            request=ActUpdateRequestAttachments(
                request_id="requestId",
            ),
        )
        """
        _response = self._raw_client.continue_action(action_id, request=request, request_options=request_options)
        return _response.data

    def authenticate_session(
        self,
        ai_id: str,
        *,
        method_id: str,
        source: AuthenticateSessionRequestSource,
        save_to_darwin_vault: bool,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthenticateSessionResponse:
        """
        Establish or reuse one bounded authentication relationship between the caller and a destination AI. When the destination has no account for the user, the same hosted flow completes required first-time setup before connecting. The relationship can be reused across Actions until it expires or is revoked.

        Parameters
        ----------
        ai_id : str
            The destination AI to authenticate with.

        method_id : str

        source : AuthenticateSessionRequestSource

        save_to_darwin_vault : bool
            Explicit consent to persist a one-time credential in Darwin Vault after authorization.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticateSessionResponse
            The reusable authentication relationship or a first-party webLink for the required provider step.

        Examples
        --------
        from fern import AuthenticateSessionRequestSource_OneTime, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.authenticate_session(
            ai_id="aiId",
            method_id="oauth_github",
            source=AuthenticateSessionRequestSource_OneTime(),
            save_to_darwin_vault=False,
            request_id="request_auth_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
        )
        """
        _response = self._raw_client.authenticate_session(
            ai_id,
            method_id=method_id,
            source=source,
            save_to_darwin_vault=save_to_darwin_vault,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    def pay_action(
        self,
        action_id: str,
        *,
        interaction_id: str,
        expected_revision: int,
        route: ActPayRequestRoute,
        source: ActPayRequestSource,
        save: bool,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActPayActionResponse:
        """
        Choose a bound direct or Darwin Pay route without overriding the reviewed merchant, amount, currency, protocol, or scope.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        interaction_id : str

        expected_revision : int

        route : ActPayRequestRoute

        source : ActPayRequestSource

        save : bool
            Explicit consent to save a tokenized processor reference after a successful one-time flow.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActPayActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import ActPayRequestSource_OneTime, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pay_action(
            action_id="actionId",
            interaction_id="interaction_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
            expected_revision=4,
            route="darwin_pay",
            source=ActPayRequestSource_OneTime(),
            save=False,
            request_id="request_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
        )
        """
        _response = self._raw_client.pay_action(
            action_id,
            interaction_id=interaction_id,
            expected_revision=expected_revision,
            route=route,
            source=source,
            save=save,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    def approve_action(
        self,
        action_id: str,
        *,
        approval_id: str,
        decision: ActApproveRequestDecision,
        expected_revision: dt.datetime,
        reviewed_payload_digest: str,
        request_id: str,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActApproveActionResponse:
        """
        Apply an exact reviewed approval decision with stale-preview protection. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        approval_id : str

        decision : ActApproveRequestDecision

        expected_revision : dt.datetime

        reviewed_payload_digest : str

        request_id : str

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActApproveActionResponse
            The current truthful state of the action.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.approve_action(
            action_id="actionId",
            approval_id="approvalId",
            decision="approve",
            expected_revision=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            reviewed_payload_digest="reviewedPayloadDigest",
            request_id="requestId",
        )
        """
        _response = self._raw_client.approve_action(
            action_id,
            approval_id=approval_id,
            decision=decision,
            expected_revision=expected_revision,
            reviewed_payload_digest=reviewed_payload_digest,
            request_id=request_id,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def stop_action(
        self, action_id: str, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActStopActionResponse:
        """
        Compatibility operation that interrupts only the current queued or running turn. New integrations should use End action for one clear finish-or-cancel closure flow. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActStopActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.stop_action(
            action_id="actionId",
            request_id="requestId",
        )
        """
        _response = self._raw_client.stop_action(action_id, request_id=request_id, request_options=request_options)
        return _response.data

    def end_action(
        self,
        action_id: str,
        *,
        expected_revision: int,
        intent: ActEndRequestIntent,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActEndActionResponse:
        """
        Freeze ordinary new work and request durable closure with finish or cancel intent. Darwin derives the final outcome; the caller cannot declare success.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        expected_revision : int

        intent : ActEndRequestIntent

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActEndActionResponse
            The current truthful state of the action.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.end_action(
            action_id="actionId",
            expected_revision=7,
            intent="finish",
            request_id="request_end_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
        )
        """
        _response = self._raw_client.end_action(
            action_id,
            expected_revision=expected_revision,
            intent=intent,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    def list_api_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyList:
        """
        List application keys and existing legacy user-bound keys for the signed-in account. Plaintext secrets are never included.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyList
            Every API key owned by the account, including expired and revoked keys.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_api_keys()
        """
        _response = self._raw_client.list_api_keys(request_options=request_options)
        return _response.data

    def create_api_key(
        self,
        *,
        application_id: str,
        name: str,
        scopes: typing.Optional[typing.Sequence[CreateApiKeyRequestScopesItem]] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedApiKey:
        """
        Create an application-only key for an owned application. It can Search public capabilities but cannot impersonate a user or Act. The plaintext apiKey is returned once. Requires a verified account session.

        Parameters
        ----------
        application_id : str
            An active application owned by the signed-in account.

        name : str
            A recognizable name for the environment or integration that will use this key.

        scopes : typing.Optional[typing.Sequence[CreateApiKeyRequestScopesItem]]
            Optional. New application keys are limited to directory:read; use OAuth for user-scoped Act.

        expires_at : typing.Optional[dt.datetime]
            Optional future ISO 8601 expiration. Omit or set null for no scheduled expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedApiKey
            The API key was created. Store apiKey securely because Darwin will not return it again.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_api_key(
            application_id="applicationId",
            name="Production server",
        )
        """
        _response = self._raw_client.create_api_key(
            application_id=application_id,
            name=name,
            scopes=scopes,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    def get_api_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyUsageResponse:
        """
        Get lifetime authenticated-request counts for the account and each API key. This is operational key usage, not billable Action spend. Requires an authenticated account session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyUsageResponse
            Lifetime API-key request counts and key-status totals.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_api_usage()
        """
        _response = self._raw_client.get_api_usage(request_options=request_options)
        return _response.data

    def delete_api_key(self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKey:
        """
        Revoke an API key owned by the signed-in Darwin account. Revocation is immediate and keeps non-secret audit metadata. Requires an authenticated account session.

        Parameters
        ----------
        api_key_id : str
            The API-key ID returned by Create API key or List API keys. This is not the secret key value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            The revoked API-key metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_api_key(
            api_key_id="apiKeyId",
        )
        """
        _response = self._raw_client.delete_api_key(api_key_id, request_options=request_options)
        return _response.data

    def list_search_history(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchHistoryPage:
        """
        List Search-history entries retained for up to 90 days for a user-bound legacy key or user-scoped OAuth grant. Application-only keys cannot read a user’s history.

        Parameters
        ----------
        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchHistoryPage
            A bounded page of retained Search-history entries.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_search_history()
        """
        _response = self._raw_client.list_search_history(cursor=cursor, limit=limit, request_options=request_options)
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
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        api_key = api_key if api_key is not None else os.getenv("DARWIN_API_KEY")
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting DARWIN_API_KEY"
            )
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

    async def search(
        self,
        *,
        query: str,
        filters: typing.Optional[SearchFilters] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Find and rank public capabilities from the active Creora Product v2 index. Search is discovery, not execution authorization. No credential is required at the public anonymous limit. You may supply a Darwin API key or OAuth bearer with directory:read for the higher authenticated limit.

        Parameters
        ----------
        query : str
            Describe the capability or outcome you need in natural language. Include the task, important constraints, and success criteria that should affect ranking; use the dedicated AI and capability read endpoints for exact lookups.

        filters : typing.Optional[SearchFilters]
            Optional structured constraints applied in addition to the natural-language query. Use these fields for hard requirements instead of embedding machine-readable filters in query text.

        limit : typing.Optional[int]
            Maximum number of ranked capabilities to return. Defaults to 10 and cannot exceed 50.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponse
            A page of public capabilities in canonical order.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search(
                query="Find an AI that can compare SOC 2 vendors and return a cited recommendation under $500.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            query=query, filters=filters, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_account(
        self,
        *,
        email: str,
        password: str,
        name: str,
        type: CreateAccountRequestType,
        organization_name: typing.Optional[str] = OMIT,
        organization_domain: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedAccount:
        """
        Register an unverified Darwin account without creating an AI or API key. Verify the email address through Darwin sign-in, then complete account setup before issuing application credentials. An application key never identifies an end user.

        Parameters
        ----------
        email : str

        password : str

        name : str

        type : CreateAccountRequestType

        organization_name : typing.Optional[str]
            Required for business and software.

        organization_domain : typing.Optional[str]
            Required for business and software; not ownership proof.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedAccount
            The restricted account was created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_account(
                email="email",
                password="password",
                name="name",
                type="personal",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_account(
            email=email,
            password=password,
            name=name,
            type=type,
            organization_name=organization_name,
            organization_domain=organization_domain,
            request_options=request_options,
        )
        return _response.data

    async def get_account(
        self, *, ai_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountSummary:
        """
        Read the account behind a user-bound legacy key or a user-scoped OAuth grant with account:read. Application-only keys cannot read or impersonate an account.

        Parameters
        ----------
        ai_id : typing.Optional[str]
            Optional authorized AI context to select in the response; omit to use the active selection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountSummary
            The authenticated account.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(ai_id=ai_id, request_options=request_options)
        return _response.data

    async def create_application(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        website_url: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Register a developer application for the authenticated account. Requires applications:write on a user-scoped OAuth grant or a legacy user key. This does not grant access to another user.

        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        website_url : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The application was registered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_application(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_application(
            name=name,
            description=description,
            website_url=website_url,
            redirect_uris=redirect_uris,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def get_application(
        self, application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Read one application owned by the authenticated account. Requires applications:read on a user-scoped grant or legacy key.

        Parameters
        ----------
        application_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The application.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application(
                application_id="applicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    async def list_actions(
        self,
        *,
        acting_ai_id: typing.Optional[str] = None,
        target_ai_id: typing.Optional[str] = None,
        lifecycle: typing.Optional[ListActionsRequestLifecycle] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActListResponse:
        """
        List current or ended human Actions with human:actions, or select an acting AI for an AI-scoped agent:read/goals:read grant.

        Parameters
        ----------
        acting_ai_id : typing.Optional[str]

        target_ai_id : typing.Optional[str]

        lifecycle : typing.Optional[ListActionsRequestLifecycle]

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActListResponse
            A page of the caller’s current actions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_actions(
            acting_ai_id=acting_ai_id,
            target_ai_id=target_ai_id,
            lifecycle=lifecycle,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def start_action(
        self,
        *,
        capability_id: str,
        capability_revision: int,
        request_id: str,
        inputs: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ActionAttachment]] = OMIT,
        intent: typing.Optional[str] = OMIT,
        acting_ai_id: typing.Optional[str] = OMIT,
        target_ai_id: typing.Optional[str] = OMIT,
        search_attribution_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActStartActionResponse:
        """
        Start durable work from an exact Search result. A consenting human OAuth user uses human:actions without an AI; an AI-scoped caller uses agent:write or goals:write and selects an authorized acting AI.

        Parameters
        ----------
        capability_id : str

        capability_revision : int

        request_id : str

        inputs : typing.Optional[typing.Dict[str, typing.Any]]

        attachments : typing.Optional[typing.Sequence[ActionAttachment]]

        intent : typing.Optional[str]

        acting_ai_id : typing.Optional[str]

        target_ai_id : typing.Optional[str]

        search_attribution_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActStartActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.start_action(
                capability_id="capabilityId",
                capability_revision=1,
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_action(
            capability_id=capability_id,
            capability_revision=capability_revision,
            request_id=request_id,
            inputs=inputs,
            attachments=attachments,
            intent=intent,
            acting_ai_id=acting_ai_id,
            target_ai_id=target_ai_id,
            search_attribution_id=search_attribution_id,
            request_options=request_options,
        )
        return _response.data

    async def get_action(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActGetActionResponse:
        """
        Get the truthful current status and required next step for one action. Requires the matching human:actions grant or an AI-scoped agent:read/goals:read grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActGetActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_action(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_action(action_id, request_options=request_options)
        return _response.data

    async def continue_action(
        self, action_id: str, *, request: ActUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActUpdateActionResponse:
        """
        Give an action more information without implicitly approving anything. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request : ActUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActUpdateActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import ActUpdateRequestAttachments, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.continue_action(
                action_id="actionId",
                request=ActUpdateRequestAttachments(
                    request_id="requestId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.continue_action(action_id, request=request, request_options=request_options)
        return _response.data

    async def authenticate_session(
        self,
        ai_id: str,
        *,
        method_id: str,
        source: AuthenticateSessionRequestSource,
        save_to_darwin_vault: bool,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthenticateSessionResponse:
        """
        Establish or reuse one bounded authentication relationship between the caller and a destination AI. When the destination has no account for the user, the same hosted flow completes required first-time setup before connecting. The relationship can be reused across Actions until it expires or is revoked.

        Parameters
        ----------
        ai_id : str
            The destination AI to authenticate with.

        method_id : str

        source : AuthenticateSessionRequestSource

        save_to_darwin_vault : bool
            Explicit consent to persist a one-time credential in Darwin Vault after authorization.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticateSessionResponse
            The reusable authentication relationship or a first-party webLink for the required provider step.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AuthenticateSessionRequestSource_OneTime

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.authenticate_session(
                ai_id="aiId",
                method_id="oauth_github",
                source=AuthenticateSessionRequestSource_OneTime(),
                save_to_darwin_vault=False,
                request_id="request_auth_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authenticate_session(
            ai_id,
            method_id=method_id,
            source=source,
            save_to_darwin_vault=save_to_darwin_vault,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    async def pay_action(
        self,
        action_id: str,
        *,
        interaction_id: str,
        expected_revision: int,
        route: ActPayRequestRoute,
        source: ActPayRequestSource,
        save: bool,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActPayActionResponse:
        """
        Choose a bound direct or Darwin Pay route without overriding the reviewed merchant, amount, currency, protocol, or scope.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        interaction_id : str

        expected_revision : int

        route : ActPayRequestRoute

        source : ActPayRequestSource

        save : bool
            Explicit consent to save a tokenized processor reference after a successful one-time flow.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActPayActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import ActPayRequestSource_OneTime, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pay_action(
                action_id="actionId",
                interaction_id="interaction_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
                expected_revision=4,
                route="darwin_pay",
                source=ActPayRequestSource_OneTime(),
                save=False,
                request_id="request_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pay_action(
            action_id,
            interaction_id=interaction_id,
            expected_revision=expected_revision,
            route=route,
            source=source,
            save=save,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    async def approve_action(
        self,
        action_id: str,
        *,
        approval_id: str,
        decision: ActApproveRequestDecision,
        expected_revision: dt.datetime,
        reviewed_payload_digest: str,
        request_id: str,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActApproveActionResponse:
        """
        Apply an exact reviewed approval decision with stale-preview protection. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        approval_id : str

        decision : ActApproveRequestDecision

        expected_revision : dt.datetime

        reviewed_payload_digest : str

        request_id : str

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActApproveActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.approve_action(
                action_id="actionId",
                approval_id="approvalId",
                decision="approve",
                expected_revision=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                reviewed_payload_digest="reviewedPayloadDigest",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_action(
            action_id,
            approval_id=approval_id,
            decision=decision,
            expected_revision=expected_revision,
            reviewed_payload_digest=reviewed_payload_digest,
            request_id=request_id,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def stop_action(
        self, action_id: str, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActStopActionResponse:
        """
        Compatibility operation that interrupts only the current queued or running turn. New integrations should use End action for one clear finish-or-cancel closure flow. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActStopActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.stop_action(
                action_id="actionId",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_action(
            action_id, request_id=request_id, request_options=request_options
        )
        return _response.data

    async def end_action(
        self,
        action_id: str,
        *,
        expected_revision: int,
        intent: ActEndRequestIntent,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActEndActionResponse:
        """
        Freeze ordinary new work and request durable closure with finish or cancel intent. Darwin derives the final outcome; the caller cannot declare success.

        Parameters
        ----------
        action_id : str
            The Action identifier returned by Start action or List actions.

        expected_revision : int

        intent : ActEndRequestIntent

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActEndActionResponse
            The current truthful state of the action.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.end_action(
                action_id="actionId",
                expected_revision=7,
                intent="finish",
                request_id="request_end_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_action(
            action_id,
            expected_revision=expected_revision,
            intent=intent,
            request_id=request_id,
            request_options=request_options,
        )
        return _response.data

    async def list_api_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyList:
        """
        List application keys and existing legacy user-bound keys for the signed-in account. Plaintext secrets are never included.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyList
            Every API key owned by the account, including expired and revoked keys.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_api_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_api_keys(request_options=request_options)
        return _response.data

    async def create_api_key(
        self,
        *,
        application_id: str,
        name: str,
        scopes: typing.Optional[typing.Sequence[CreateApiKeyRequestScopesItem]] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedApiKey:
        """
        Create an application-only key for an owned application. It can Search public capabilities but cannot impersonate a user or Act. The plaintext apiKey is returned once. Requires a verified account session.

        Parameters
        ----------
        application_id : str
            An active application owned by the signed-in account.

        name : str
            A recognizable name for the environment or integration that will use this key.

        scopes : typing.Optional[typing.Sequence[CreateApiKeyRequestScopesItem]]
            Optional. New application keys are limited to directory:read; use OAuth for user-scoped Act.

        expires_at : typing.Optional[dt.datetime]
            Optional future ISO 8601 expiration. Omit or set null for no scheduled expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedApiKey
            The API key was created. Store apiKey securely because Darwin will not return it again.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_api_key(
                application_id="applicationId",
                name="Production server",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key(
            application_id=application_id,
            name=name,
            scopes=scopes,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    async def get_api_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyUsageResponse:
        """
        Get lifetime authenticated-request counts for the account and each API key. This is operational key usage, not billable Action spend. Requires an authenticated account session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyUsageResponse
            Lifetime API-key request counts and key-status totals.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_api_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_usage(request_options=request_options)
        return _response.data

    async def delete_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Revoke an API key owned by the signed-in Darwin account. Revocation is immediate and keeps non-secret audit metadata. Requires an authenticated account session.

        Parameters
        ----------
        api_key_id : str
            The API-key ID returned by Create API key or List API keys. This is not the secret key value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            The revoked API-key metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_api_key(
                api_key_id="apiKeyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(api_key_id, request_options=request_options)
        return _response.data

    async def list_search_history(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchHistoryPage:
        """
        List Search-history entries retained for up to 90 days for a user-bound legacy key or user-scoped OAuth grant. Application-only keys cannot read a user’s history.

        Parameters
        ----------
        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchHistoryPage
            A bounded page of retained Search-history entries.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_search_history()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_search_history(
            cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
