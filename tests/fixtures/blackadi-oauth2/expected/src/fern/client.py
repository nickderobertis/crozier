

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_authorization_request_code_challenge_method import GetAuthorizationRequestCodeChallengeMethod
from .types.get_authorization_request_prompt import GetAuthorizationRequestPrompt
from .types.get_authorization_request_response_type import GetAuthorizationRequestResponseType
from .types.get_fapi_config_response import GetFapiConfigResponse
from .types.get_fapi_status_response import GetFapiStatusResponse
from .types.get_health_all_response import GetHealthAllResponse
from .types.get_health_authlete_request_extended import GetHealthAuthleteRequestExtended
from .types.get_health_response import GetHealthResponse
from .types.get_logout_request_backchannel import GetLogoutRequestBackchannel
from .types.get_token_list_response import GetTokenListResponse
from .types.post_ciba_complete_request_result import PostCibaCompleteRequestResult
from .types.post_device_authorization_response import PostDeviceAuthorizationResponse
from .types.post_device_complete_request_result import PostDeviceCompleteRequestResult
from .types.post_introspection_standard_response import PostIntrospectionStandardResponse
from .types.post_logout_request_backchannel import PostLogoutRequestBackchannel
from .types.post_par_response import PostParResponse
from .types.post_session_consent_request_decision import PostSessionConsentRequestDecision
from .types.post_token_request_grant_type import PostTokenRequestGrantType
from .types.post_token_response import PostTokenResponse
from .types.post_vci_deferred_issue_request_order import PostVciDeferredIssueRequestOrder


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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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

    def o_auth_authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: typing.Optional[GetAuthorizationRequestResponseType] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetAuthorizationRequestCodeChallengeMethod] = None,
        claims: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        prompt: typing.Optional[GetAuthorizationRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiates an OAuth 2.0 / OIDC authorization request. Redirects to login or consent pages for interactive flows.

        Three request shapes are accepted, and `client_id` is the only parameter required by all of them:
        - **Plain** — `response_type` + `client_id` (+ `redirect_uri`, which RFC 6749 §3.1.2.3 makes optional when exactly one full redirection URI is registered).
        - **PAR (RFC 9126)** — `client_id` + `request_uri`; the rest was pushed to `/par` beforehand.
        - **JAR (RFC 9101 §5)** — `client_id` + `request`; every other parameter lives inside the signed Request Object. Per RFC 9101 §6.3 the server uses *only* the parameters in the Request Object, so anything duplicated on the query string is ignored rather than merged.

        Parameters
        ----------
        client_id : str
            The only always-required parameter (RFC 6749 §4.1.1; RFC 9101 §5 requires it alongside a Request Object and requires it to match the object's own client_id).

        response_type : typing.Optional[GetAuthorizationRequestResponseType]
            Required for a plain request; supplied inside the Request Object for JAR/PAR.

        request : typing.Optional[str]
            A signed Request Object (JAR, RFC 9101). Verified against the client's registered `jwks` / `jwks_uri` — the client's public keys, not the authorization server's.

        request_uri : typing.Optional[str]
            Reference to a pushed authorization request (RFC 9126). Single-use.

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        code_challenge : typing.Optional[str]
            PKCE code challenge (RFC 7636)

        code_challenge_method : typing.Optional[GetAuthorizationRequestCodeChallengeMethod]

        claims : typing.Optional[str]
            JSON object specifying requested claims (OIDC Core §5.5)

        resource : typing.Optional[str]
            Resource indicator (RFC 8707)

        prompt : typing.Optional[GetAuthorizationRequestPrompt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_authorization_endpoint(
            client_id="client_id",
        )
        """
        _response = self._raw_client.o_auth_authorization_endpoint(
            client_id=client_id,
            response_type=response_type,
            request=request,
            request_uri=request_uri,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            claims=claims,
            resource=resource,
            prompt=prompt,
            request_options=request_options,
        )
        return _response.data

    def o_auth_token_endpoint(
        self,
        *,
        grant_type: PostTokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        auth_req_id: typing.Optional[str] = OMIT,
        device_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostTokenResponse:
        """
        Exchanges authorization codes, refresh tokens, client credentials, or other grant types for access tokens.

        Parameters
        ----------
        grant_type : PostTokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        assertion : typing.Optional[str]

        resource : typing.Optional[str]

        auth_req_id : typing.Optional[str]

        device_code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTokenResponse
            Token issued successfully

        Examples
        --------
        from fern import FernApi, PostTokenRequestGrantType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_token_endpoint(
            grant_type=PostTokenRequestGrantType.AUTHORIZATION_CODE,
        )
        """
        _response = self._raw_client.o_auth_token_endpoint(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            username=username,
            password=password,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            assertion=assertion,
            resource=resource,
            auth_req_id=auth_req_id,
            device_code=device_code,
            request_options=request_options,
        )
        return _response.data

    def user_info_endpoint(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns claims about the authenticated end-user. Accepts either the Bearer scheme (RFC 6750 §2.1) or the DPoP scheme (RFC 9449 §7.1); the scheme name is case-insensitive. A token issued with token_type: DPoP MUST use the DPoP scheme and be accompanied by a proof — presenting it as Bearer is rejected per RFC 9449 §7.2. Requires the openid scope.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            User claims

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_info_endpoint()
        """
        _response = self._raw_client.user_info_endpoint(request_options=request_options)
        return _response.data

    def user_info_endpoint_post(
        self, *, access_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        As GET. The token may also be sent as access_token in an application/x-www-form-urlencoded body (RFC 6750 §2.2), but not by both methods at once. The URI query parameter method of RFC 6750 §2.3 is not supported: RFC 9700 §4.3.2 forbids it.

        Parameters
        ----------
        access_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_info_endpoint_post()
        """
        _response = self._raw_client.user_info_endpoint_post(access_token=access_token, request_options=request_options)
        return _response.data

    def authlete_specific_token_introspection(
        self,
        *,
        token: str,
        scopes: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        acr_values: typing.Optional[str] = OMIT,
        max_age: typing.Optional[int] = OMIT,
        resources: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Non-standard token introspection returning Authlete's raw response. Supports RFC 9470 step-up authentication validation via acrValues and maxAge parameters.

        Parameters
        ----------
        token : str
            The access token to introspect.

        scopes : typing.Optional[str]
            Space-separated list of required scopes.

        subject : typing.Optional[str]
            Required subject (user) for the token.

        acr_values : typing.Optional[str]
            RFC 9470: Space-separated ACR values one of which the token must satisfy.

        max_age : typing.Optional[int]
            RFC 9470: Maximum authentication age in seconds.

        resources : typing.Optional[str]
            Space-separated resource indicators.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authlete_specific_token_introspection(
            token="token",
        )
        """
        _response = self._raw_client.authlete_specific_token_introspection(
            token=token,
            scopes=scopes,
            subject=subject,
            acr_values=acr_values,
            max_age=max_age,
            resources=resources,
            request_options=request_options,
        )
        return _response.data

    def rfc7662token_introspection(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostIntrospectionStandardResponse:
        """
        Standard OAuth 2.0 token introspection as defined in RFC 7662.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostIntrospectionStandardResponse
            Introspection result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rfc7662token_introspection(
            token="token",
        )
        """
        _response = self._raw_client.rfc7662token_introspection(token=token, request_options=request_options)
        return _response.data

    def rfc7009token_revocation(
        self,
        *,
        token: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes an access or refresh token.

        Parameters
        ----------
        token : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rfc7009token_revocation(
            token="token",
        )
        """
        _response = self._raw_client.rfc7009token_revocation(
            token=token, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def login_form(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Renders the login page (EJS template).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.login_form()
        """
        _response = self._raw_client.login_form(request_options=request_options)
        return _response.data

    def submit_login(
        self,
        *,
        username: str,
        password: str,
        csrf: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Validates username/password and initiates the OAuth session.

        Parameters
        ----------
        username : str

        password : str

        csrf : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.submit_login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.submit_login(
            username=username, password=password, csrf=csrf, request_options=request_options
        )
        return _response.data

    def consent_form(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Renders the consent page (EJS template).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.consent_form()
        """
        _response = self._raw_client.consent_form(request_options=request_options)
        return _response.data

    def submit_consent_decision(
        self,
        *,
        decision: PostSessionConsentRequestDecision,
        csrf: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Approves or denies the OAuth authorization request.

        Parameters
        ----------
        decision : PostSessionConsentRequestDecision

        csrf : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PostSessionConsentRequestDecision

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.submit_consent_decision(
            decision=PostSessionConsentRequestDecision.APPROVE,
        )
        """
        _response = self._raw_client.submit_consent_decision(
            decision=decision, csrf=csrf, request_options=request_options
        )
        return _response.data

    def open_id_connect_discovery(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the OIDC Discovery document (RFC 8414).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Discovery document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_connect_discovery()
        """
        _response = self._raw_client.open_id_connect_discovery(request_options=request_options)
        return _response.data

    def jwks_endpoint(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Returns the JSON Web Key Set (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JWK Set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jwks_endpoint()
        """
        _response = self._raw_client.jwks_endpoint(request_options=request_options)
        return _response.data

    def dynamic_client_registration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Registers a new OAuth client (RFC 7591). Requires admin Basic auth.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dynamic_client_registration(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.dynamic_client_registration(request=request, request_options=request_options)
        return _response.data

    def get_registered_client(
        self,
        *,
        token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieves a client by registration access token (RFC 7592).

        Parameters
        ----------
        token : typing.Optional[str]

        client_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_registered_client()
        """
        _response = self._raw_client.get_registered_client(
            token=token, client_id=client_id, request_options=request_options
        )
        return _response.data

    def update_registered_client(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a client's registration (RFC 7592).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_registered_client(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_registered_client(request=request, request_options=request_options)
        return _response.data

    def delete_registered_client(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a client's registration (RFC 7592).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_registered_client(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.delete_registered_client(request=request, request_options=request_options)
        return _response.data

    def ciba_backchannel_authentication(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Starts a CIBA authentication request (Client-Initiated Backchannel Authentication, OIDC CIBA Core). The `parameters` field is a URL-encoded string containing the backchannel authentication request (login_hint, scope, client_notification_token, etc.). Client credentials are passed as `clientId`/`clientSecret` in the JSON body.

        Parameters
        ----------
        parameters : str
            URL-encoded backchannel authentication request parameters

        client_id : typing.Optional[str]
            Client identifier

        client_secret : typing.Optional[str]
            Client secret for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ciba_backchannel_authentication(
            parameters="parameters",
        )
        """
        _response = self._raw_client.ciba_backchannel_authentication(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def issue_ciba_auth_req_id(
        self, *, ticket: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Issues an auth_req_id for a validated CIBA ticket.

        Parameters
        ----------
        ticket : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_ciba_auth_req_id()
        """
        _response = self._raw_client.issue_ciba_auth_req_id(ticket=ticket, request_options=request_options)
        return _response.data

    def fail_ciba_request(
        self, *, ticket: str, reason: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks a CIBA authentication request as failed. The `reason` field describes why the request failed (e.g., TRANSACTION_FAILED, ACCESS_DENIED).

        Parameters
        ----------
        ticket : str
            Ticket from the authentication endpoint

        reason : str
            Failure reason (e.g. TRANSACTION_FAILED, ACCESS_DENIED)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fail_ciba_request(
            ticket="ticket",
            reason="reason",
        )
        """
        _response = self._raw_client.fail_ciba_request(ticket=ticket, reason=reason, request_options=request_options)
        return _response.data

    def complete_ciba_request(
        self,
        *,
        ticket: str,
        result: PostCibaCompleteRequestResult,
        subject: str,
        acr: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        claims: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completes a CIBA authentication request with end-user result. Requires `subject` to identify the authenticated user.

        Parameters
        ----------
        ticket : str

        result : PostCibaCompleteRequestResult

        subject : str
            Authenticated user subject

        acr : typing.Optional[str]
            ACR satisfied during authentication

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

        claims : typing.Optional[str]
            JSON string of additional claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PostCibaCompleteRequestResult

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.complete_ciba_request(
            ticket="ticket",
            result=PostCibaCompleteRequestResult.AUTHORIZED,
            subject="subject",
        )
        """
        _response = self._raw_client.complete_ciba_request(
            ticket=ticket,
            result=result,
            subject=subject,
            acr=acr,
            auth_time=auth_time,
            claims=claims,
            request_options=request_options,
        )
        return _response.data

    def pushed_authorization_request_rfc9126(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostParResponse:
        """
        Pushes authorization request parameters to the PAR endpoint. Returns a `request_uri` for use in `/authorization`. For `CLIENT_SECRET_POST` clients, `client_id` and `client_secret` are merged into the `parameters` string (not sent as separate JSON fields).

        Parameters
        ----------
        parameters : str
            URL-encoded authorization request parameters

        client_id : typing.Optional[str]
            Client ID (merged into parameters for CLIENT_SECRET_POST)

        client_secret : typing.Optional[str]
            Client secret (merged into parameters for CLIENT_SECRET_POST)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostParResponse
            PAR created. The body is RFC 9126 §2.2's, not Authlete's envelope (T1-11).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pushed_authorization_request_rfc9126(
            parameters="parameters",
        )
        """
        _response = self._raw_client.pushed_authorization_request_rfc9126(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def query_grant_status(self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the status of a granted authorization (Grant Management API). This is a protected resource: a DPoP-bound token must be presented with the DPoP scheme and a proof (RFC 9449 §7.1), and Bearer with a proof is refused as the §7.2 downgrade.

        Parameters
        ----------
        grant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.query_grant_status(
            grant_id="grantId",
        )
        """
        _response = self._raw_client.query_grant_status(grant_id, request_options=request_options)
        return _response.data

    def revoke_grant(self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes a granted authorization (Grant Management API). Same presentation rules as the query operation — Bearer or DPoP, per RFC 6750 §2 and RFC 9449 §7.

        Parameters
        ----------
        grant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.revoke_grant(
            grant_id="grantId",
        )
        """
        _response = self._raw_client.revoke_grant(grant_id, request_options=request_options)
        return _response.data

    def rp_initiated_logout_confirmation_page(
        self,
        *,
        client_id: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        id_token_hint: typing.Optional[str] = None,
        backchannel: typing.Optional[GetLogoutRequestBackchannel] = None,
        state: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Renders the logout confirmation page required by OpenID Connect RP-Initiated Logout 1.0 §2. This request destroys nothing: it returns an HTML form carrying a CSRF token and the supplied parameters as hidden fields. Submitting that form (POST /logout) is what ends the session.

        Parameters
        ----------
        client_id : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        id_token_hint : typing.Optional[str]

        backchannel : typing.Optional[GetLogoutRequestBackchannel]
            Trigger backchannel logout delivery on the subsequent POST

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML confirmation page containing the _csrf token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rp_initiated_logout_confirmation_page()
        """
        _response = self._raw_client.rp_initiated_logout_confirmation_page(
            client_id=client_id,
            post_logout_redirect_uri=post_logout_redirect_uri,
            id_token_hint=id_token_hint,
            backchannel=backchannel,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def rp_initiated_logout_end_the_session(
        self,
        *,
        csrf: str,
        client_id: typing.Optional[str] = OMIT,
        post_logout_redirect_uri: typing.Optional[str] = OMIT,
        id_token_hint: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        backchannel: typing.Optional[PostLogoutRequestBackchannel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Ends the session: verifies any id_token_hint against the OP's JWKS, optionally delivers backchannel logout tokens, destroys the session and clears the cookie, then redirects if post_logout_redirect_uri is allowed. Requires the _csrf token issued by GET /logout.

        Parameters
        ----------
        csrf : str
            CSRF token from the GET /logout confirmation page

        client_id : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        id_token_hint : typing.Optional[str]

        state : typing.Optional[str]

        backchannel : typing.Optional[PostLogoutRequestBackchannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Session ended; signed-out page rendered because no allowed redirect target was supplied

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rp_initiated_logout_end_the_session(
            csrf="_csrf",
        )
        """
        _response = self._raw_client.rp_initiated_logout_end_the_session(
            csrf=csrf,
            client_id=client_id,
            post_logout_redirect_uri=post_logout_redirect_uri,
            id_token_hint=id_token_hint,
            state=state,
            backchannel=backchannel,
            request_options=request_options,
        )
        return _response.data

    def backchannel_logout_receiver(
        self, *, logout_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Receives incoming backchannel logout tokens from other OPs (OpenID Provider).

        Parameters
        ----------
        logout_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.backchannel_logout_receiver(
            logout_token="logout_token",
        )
        """
        _response = self._raw_client.backchannel_logout_receiver(
            logout_token=logout_token, request_options=request_options
        )
        return _response.data

    def issue_backchannel_logout_token(
        self,
        *,
        client_identifier: str,
        subject: str,
        session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a signed logout token for a client. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        subject : str

        session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_backchannel_logout_token(
            client_identifier="clientIdentifier",
            subject="subject",
        )
        """
        _response = self._raw_client.issue_backchannel_logout_token(
            client_identifier=client_identifier, subject=subject, session_id=session_id, request_options=request_options
        )
        return _response.data

    def issue_and_deliver_logout_token(
        self, *, client_identifier: str, subject: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Issues a logout token and delivers it to a specific client. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_and_deliver_logout_token(
            client_identifier="clientIdentifier",
            subject="subject",
        )
        """
        _response = self._raw_client.issue_and_deliver_logout_token(
            client_identifier=client_identifier, subject=subject, request_options=request_options
        )
        return _response.data

    def issue_and_deliver_logout_tokens_to_all_clients(
        self,
        *,
        subject: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues and delivers backchannel logout tokens to every client with a backchannel_logout_uri configured. At least one of `subject` or `sessionId` is required. Requires admin Basic auth.

        Parameters
        ----------
        subject : typing.Optional[str]
            End-user subject to include in logout tokens

        session_id : typing.Optional[str]
            Session ID to include in logout tokens

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_and_deliver_logout_tokens_to_all_clients()
        """
        _response = self._raw_client.issue_and_deliver_logout_tokens_to_all_clients(
            subject=subject, session_id=session_id, request_options=request_options
        )
        return _response.data

    def list_tokens(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetTokenListResponse:
        """
        Lists all tokens via Authlete token management. Returns paginated results. Requires admin Basic auth.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenListResponse
            Token list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tokens()
        """
        _response = self._raw_client.list_tokens(request_options=request_options)
        return _response.data

    def create_token_programmatically(
        self,
        *,
        grant_type: str,
        client_id: int,
        subject: typing.Optional[str] = OMIT,
        scopes: typing.Optional[str] = OMIT,
        access_token_duration: typing.Optional[int] = OMIT,
        refresh_token_duration: typing.Optional[int] = OMIT,
        access_token: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new token via Authlete token management. Requires admin Basic auth. The `grantType` uses Authlete enum format (e.g. AUTHORIZATION_CODE, CLIENT_CREDENTIALS).

        Parameters
        ----------
        grant_type : str
            Authlete grant type enum (AUTHORIZATION_CODE, CLIENT_CREDENTIALS, PASSWORD, REFRESH_TOKEN, etc.)

        client_id : int
            Numeric client ID

        subject : typing.Optional[str]
            End-user subject identifier

        scopes : typing.Optional[str]
            Space-separated scope values

        access_token_duration : typing.Optional[int]
            Access token duration in seconds

        refresh_token_duration : typing.Optional[int]
            Refresh token duration in seconds

        access_token : typing.Optional[str]
            Pre-defined access token value

        refresh_token : typing.Optional[str]
            Pre-defined refresh token value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_token_programmatically(
            grant_type="grantType",
            client_id=1,
        )
        """
        _response = self._raw_client.create_token_programmatically(
            grant_type=grant_type,
            client_id=client_id,
            subject=subject,
            scopes=scopes,
            access_token_duration=access_token_duration,
            refresh_token_duration=refresh_token_duration,
            access_token=access_token,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    def delete_token(
        self, access_token_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a token by its identifier. Requires admin Basic auth.

        Parameters
        ----------
        access_token_identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_token(
            access_token_identifier="accessTokenIdentifier",
        )
        """
        _response = self._raw_client.delete_token(access_token_identifier, request_options=request_options)
        return _response.data

    def update_token_scopes(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a token's scopes or metadata. Requires admin Basic auth.

        Parameters
        ----------
        access_token : typing.Optional[str]

        scopes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_token_scopes()
        """
        _response = self._raw_client.update_token_scopes(
            access_token=access_token, scopes=scopes, request_options=request_options
        )
        return _response.data

    def revoke_token_via_management_api(
        self,
        *,
        access_token_identifier: typing.Optional[str] = OMIT,
        refresh_token_identifier: typing.Optional[str] = OMIT,
        client_identifier: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes a token using the Authlete token management API. Accepts multiple identifier fields — at least one is recommended. Requires admin Basic auth.

        Parameters
        ----------
        access_token_identifier : typing.Optional[str]
            Access token identifier to revoke

        refresh_token_identifier : typing.Optional[str]
            Refresh token identifier to revoke

        client_identifier : typing.Optional[str]
            Client identifier to scope the revocation

        subject : typing.Optional[str]
            Subject to scope the revocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.revoke_token_via_management_api()
        """
        _response = self._raw_client.revoke_token_via_management_api(
            access_token_identifier=access_token_identifier,
            refresh_token_identifier=refresh_token_identifier,
            client_identifier=client_identifier,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def reissue_id_token(
        self,
        *,
        access_token: str,
        refresh_token: str,
        sub: typing.Optional[str] = OMIT,
        claims: typing.Optional[str] = OMIT,
        idt_header_params: typing.Optional[str] = OMIT,
        id_token_aud_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reissues an ID token for an existing session using Authlete's ID Token Reissue API. Requires admin Basic auth.

        Parameters
        ----------
        access_token : str
            Current access token

        refresh_token : str
            Current refresh token

        sub : typing.Optional[str]
            Subject to override in the reissued ID token

        claims : typing.Optional[str]
            JSON string of additional claims to embed

        idt_header_params : typing.Optional[str]
            JSON string of additional JOSE header parameters

        id_token_aud_type : typing.Optional[str]
            Audience type for the reissued ID token (string or array)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reissue_id_token(
            access_token="accessToken",
            refresh_token="refreshToken",
        )
        """
        _response = self._raw_client.reissue_id_token(
            access_token=access_token,
            refresh_token=refresh_token,
            sub=sub,
            claims=claims,
            idt_header_params=idt_header_params,
            id_token_aud_type=id_token_aud_type,
            request_options=request_options,
        )
        return _response.data

    def create_local_jwt(
        self,
        *,
        sub: str,
        aud: str,
        client_id: str,
        iss: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        acr: typing.Optional[str] = None,
        auth_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a locally-signed RFC 9068 JWT access token (development only, no Authlete call). Returns the JWT and the public key for verification. The token carries `typ: at+jwt` and all seven claims RFC 9068 §2.2 marks REQUIRED — it is the repo's worked example of that section, so `client_id` is required here even though the endpoint is a fixture.

        Parameters
        ----------
        sub : str

        aud : str
            Space-delimited; becomes the `aud` array

        client_id : str
            REQUIRED — RFC 9068 §2.2 marks `client_id` a required claim of a JWT access token

        iss : typing.Optional[str]
            Defaults to the JWT_ISSUER environment value when omitted

        scope : typing.Optional[str]
            Space-delimited. RFC 9068 §2.2.3 makes `scope` a SHOULD, so it is omitted from the token rather than emitted empty

        acr : typing.Optional[str]
            ACR claim to embed in the JWT (RFC 9068 §2.2.1, OPTIONAL)

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds) to embed as auth_time. Ignored unless it parses as a positive integer — an unparseable value stamps no claim rather than the Unix epoch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_local_jwt(
            sub="sub",
            aud="aud",
            client_id="client_id",
        )
        """
        _response = self._raw_client.create_local_jwt(
            sub=sub,
            aud=aud,
            client_id=client_id,
            iss=iss,
            scope=scope,
            acr=acr,
            auth_time=auth_time,
            request_options=request_options,
        )
        return _response.data

    def prometheus_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns runtime and HTTP metrics in Prometheus text format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Metrics in text format

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.prometheus_metrics()
        """
        _response = self._raw_client.prometheus_metrics(request_options=request_options)
        return _response.data

    def server_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetHealthResponse:
        """
        Returns basic server health status.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHealthResponse
            Health status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.server_health()
        """
        _response = self._raw_client.server_health(request_options=request_options)
        return _response.data

    def aggregate_health_check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetHealthAllResponse:
        """
        Returns combined health status of all dependencies (server, Redis, Authlete).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHealthAllResponse
            All healthy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.aggregate_health_check()
        """
        _response = self._raw_client.aggregate_health_check(request_options=request_options)
        return _response.data

    def authlete_connectivity_check(
        self,
        *,
        extended: typing.Optional[GetHealthAuthleteRequestExtended] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Checks connectivity to Authlete's API. Add ?extended=true for a detailed check.

        Parameters
        ----------
        extended : typing.Optional[GetHealthAuthleteRequestExtended]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authlete_connectivity_check()
        """
        _response = self._raw_client.authlete_connectivity_check(extended=extended, request_options=request_options)
        return _response.data

    def list_all_clients(
        self,
        *,
        start: typing.Optional[int] = None,
        end: typing.Optional[int] = None,
        developer: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Lists all OAuth clients registered in Authlete. Supports pagination via `start` and `end` query parameters. Requires admin Basic auth.

        Parameters
        ----------
        start : typing.Optional[int]
            Start index for pagination

        end : typing.Optional[int]
            End index for pagination

        developer : typing.Optional[str]
            Filter by developer name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_all_clients()
        """
        _response = self._raw_client.list_all_clients(
            start=start, end=end, developer=developer, request_options=request_options
        )
        return _response.data

    def create_client(
        self,
        *,
        client: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_client()
        """
        _response = self._raw_client.create_client(client=client, request_options=request_options)
        return _response.data

    def get_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieves an OAuth client by ID. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.get_client(client_id, request_options=request_options)
        return _response.data

    def update_client(
        self,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_client(
            client_id="clientId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_client(client_id, request=request, request_options=request_options)
        return _response.data

    def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data

    def update_client_lock_flag(
        self, client_identifier: str, *, client_locked: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the lock flag on a client to prevent or allow credential refresh. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        client_locked : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_client_lock_flag(
            client_identifier="clientIdentifier",
            client_locked=True,
        )
        """
        _response = self._raw_client.update_client_lock_flag(
            client_identifier, client_locked=client_locked, request_options=request_options
        )
        return _response.data

    def refresh_client_secret(
        self, client_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Generates a new randomly-generated client secret and deactivates the old one. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.refresh_client_secret(
            client_identifier="clientIdentifier",
        )
        """
        _response = self._raw_client.refresh_client_secret(client_identifier, request_options=request_options)
        return _response.data

    def update_client_secret(
        self, client_identifier: str, *, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets a known client secret value (replaces the current secret). Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_client_secret(
            client_identifier="clientIdentifier",
            client_secret="clientSecret",
        )
        """
        _response = self._raw_client.update_client_secret(
            client_identifier, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def list_client_authorizations_for_a_subject(
        self,
        subject: str,
        *,
        start: typing.Optional[int] = None,
        end: typing.Optional[int] = None,
        developer: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Lists all authorizations granted by a specific end-user. Supports pagination.

        Parameters
        ----------
        subject : str

        start : typing.Optional[int]

        end : typing.Optional[int]

        developer : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_client_authorizations_for_a_subject(
            subject="subject",
        )
        """
        _response = self._raw_client.list_client_authorizations_for_a_subject(
            subject, start=start, end=end, developer=developer, request_options=request_options
        )
        return _response.data

    def update_client_authorization(
        self,
        client_id: str,
        *,
        subject: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a client's authorization for a specific user (e.g., modify granted scopes).

        Parameters
        ----------
        client_id : str

        subject : typing.Optional[str]

        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_client_authorization(
            client_id="clientId",
        )
        """
        _response = self._raw_client.update_client_authorization(
            client_id, subject=subject, scopes=scopes, request_options=request_options
        )
        return _response.data

    def delete_client_authorization(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a client's authorization for a specific user.

        Parameters
        ----------
        client_id : str

        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_client_authorization(
            client_id="clientId",
            subject="subject",
        )
        """
        _response = self._raw_client.delete_client_authorization(client_id, subject, request_options=request_options)
        return _response.data

    def get_granted_scopes(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the scopes that have been granted to a specific client for a specific user.

        Parameters
        ----------
        client_id : str

        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_granted_scopes(
            client_id="clientId",
            subject="subject",
        )
        """
        _response = self._raw_client.get_granted_scopes(client_id, subject, request_options=request_options)
        return _response.data

    def delete_granted_scopes(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all granted scopes for a specific client and user combination.

        Parameters
        ----------
        client_id : str

        subject : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_granted_scopes(
            client_id="clientId",
            subject="subject",
        )
        """
        _response = self._raw_client.delete_granted_scopes(client_id, subject, request_options=request_options)
        return _response.data

    def get_requestable_scopes(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the scopes that a client is allowed to request.

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_requestable_scopes(
            client_id="clientId",
        )
        """
        _response = self._raw_client.get_requestable_scopes(client_id, request_options=request_options)
        return _response.data

    def update_requestable_scopes(
        self,
        client_id: str,
        *,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sets the scopes that a client is allowed to request.

        Parameters
        ----------
        client_id : str

        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_requestable_scopes(
            client_id="clientId",
        )
        """
        _response = self._raw_client.update_requestable_scopes(
            client_id, scopes=scopes, request_options=request_options
        )
        return _response.data

    def delete_requestable_scopes(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all requestable scopes for a client.

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_requestable_scopes(
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_requestable_scopes(client_id, request_options=request_options)
        return _response.data

    def device_authorization(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDeviceAuthorizationResponse:
        """
        Initiates the Device Authorization Flow (RFC 8628). Designed for public clients (smart TVs, CLI, IoT) that cannot securely store a client secret. Public clients only need `client_id`; confidential clients can optionally provide `client_secret` for authentication.

        Parameters
        ----------
        parameters : str
            URL-encoded device authorization request parameters (scope, client_id, etc.)

        client_id : typing.Optional[str]
            Client identifier (required for public clients, optional if embedded in parameters)

        client_secret : typing.Optional[str]
            Client secret — only for confidential clients. Public clients omit this.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDeviceAuthorizationResponse
            Device code issued. The body is RFC 8628 §3.2's, not Authlete's envelope (T1-11).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device_authorization(
            parameters="parameters",
        )
        """
        _response = self._raw_client.device_authorization(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def verify_device_user_code(
        self, *, user_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verifies a user code from the Device Flow. Returns VALID if the code exists and has not expired, NOT_EXIST if not found, EXPIRED if expired.

        Parameters
        ----------
        user_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.verify_device_user_code(
            user_code="userCode",
        )
        """
        _response = self._raw_client.verify_device_user_code(user_code=user_code, request_options=request_options)
        return _response.data

    def complete_device_authentication(
        self,
        *,
        user_code: str,
        result: PostDeviceCompleteRequestResult,
        subject: str,
        acr: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        claims: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completes device authentication with end-user approval or denial. Requires `subject` to identify the authenticated user.

        Parameters
        ----------
        user_code : str

        result : PostDeviceCompleteRequestResult

        subject : str
            Authenticated user subject

        acr : typing.Optional[str]
            ACR satisfied during authentication

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

        claims : typing.Optional[str]
            JSON string of additional claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PostDeviceCompleteRequestResult

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.complete_device_authentication(
            user_code="userCode",
            result=PostDeviceCompleteRequestResult.SUCCESS,
            subject="subject",
        )
        """
        _response = self._raw_client.complete_device_authentication(
            user_code=user_code,
            result=result,
            subject=subject,
            acr=acr,
            auth_time=auth_time,
            claims=claims,
            request_options=request_options,
        )
        return _response.data

    def vci_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves Verifiable Credential Issuer metadata. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vci_metadata()
        """
        _response = self._raw_client.vci_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    def vci_jwt_issuer_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves the JWT issuer configuration for VCI. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vci_jwt_issuer_metadata()
        """
        _response = self._raw_client.vci_jwt_issuer_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    def vci_jwks(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves the JWK Set for VCI. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vci_jwks()
        """
        _response = self._raw_client.vci_jwks(pretty=pretty, request_options=request_options)
        return _response.data

    def create_credential_offer(
        self,
        *,
        credential_configuration_ids: typing.Sequence[str],
        subject: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        acr: typing.Optional[str] = OMIT,
        tx_code: typing.Optional[str] = OMIT,
        tx_code_input_mode: typing.Optional[str] = OMIT,
        tx_code_description: typing.Optional[str] = OMIT,
        authorization_code_grant_included: typing.Optional[bool] = OMIT,
        issuer_state_included: typing.Optional[bool] = OMIT,
        pre_authorized_code_grant_included: typing.Optional[bool] = OMIT,
        context: typing.Optional[str] = OMIT,
        properties: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        jwt_at_claims: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new OID4VCI credential offer. Requires admin Basic auth. The `credentialConfigurationIds` field must reference pre-configured credential configurations in Authlete.

        Parameters
        ----------
        credential_configuration_ids : typing.Sequence[str]
            IDs of credential configurations to offer

        subject : typing.Optional[str]
            Pre-determined subject for the credential

        duration : typing.Optional[float]
            Offer duration in seconds

        acr : typing.Optional[str]
            ACR value for the offer

        tx_code : typing.Optional[str]
            Pre-defined transaction code

        tx_code_input_mode : typing.Optional[str]
            Transaction code input mode (text or numeric)

        tx_code_description : typing.Optional[str]
            Description of the transaction code for the user

        authorization_code_grant_included : typing.Optional[bool]
            Include authorization code grant in the offer

        issuer_state_included : typing.Optional[bool]
            Include issuer state in the offer

        pre_authorized_code_grant_included : typing.Optional[bool]
            Include pre-authorized code grant in the offer

        context : typing.Optional[str]
            Context string for the offer

        properties : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Additional properties to include

        jwt_at_claims : typing.Optional[str]
            JSON string of additional JWT access token claims

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_credential_offer(
            credential_configuration_ids=["credentialConfigurationIds"],
        )
        """
        _response = self._raw_client.create_credential_offer(
            credential_configuration_ids=credential_configuration_ids,
            subject=subject,
            duration=duration,
            acr=acr,
            tx_code=tx_code,
            tx_code_input_mode=tx_code_input_mode,
            tx_code_description=tx_code_description,
            authorization_code_grant_included=authorization_code_grant_included,
            issuer_state_included=issuer_state_included,
            pre_authorized_code_grant_included=pre_authorized_code_grant_included,
            context=context,
            properties=properties,
            jwt_at_claims=jwt_at_claims,
            auth_time=auth_time,
            request_options=request_options,
        )
        return _response.data

    def get_offer_information(
        self, *, identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves information about a credential offer. Requires admin Basic auth.

        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_offer_information(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_offer_information(identifier=identifier, request_options=request_options)
        return _response.data

    def issue_single_credential(
        self,
        *,
        access_token: str,
        order: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues a single verifiable credential. Requires a Bearer access token (from the pre-authorized code flow) in the Authorization header, or `accessToken` in the request body. Returns 202 for deferred issuance.

        Parameters
        ----------
        access_token : str

        order : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_single_credential(
            access_token="accessToken",
        )
        """
        _response = self._raw_client.issue_single_credential(
            access_token=access_token, order=order, request_options=request_options
        )
        return _response.data

    def issue_batch_credentials(
        self,
        *,
        access_token: str,
        orders: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues multiple verifiable credentials in a single request (OID4VCI §10). Requires a Bearer access token in the Authorization header or `accessToken` in the body.

        Parameters
        ----------
        access_token : str
            Access token from pre-authorized code flow

        orders : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Array of credential issuance orders

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_batch_credentials(
            access_token="accessToken",
        )
        """
        _response = self._raw_client.issue_batch_credentials(
            access_token=access_token, orders=orders, request_options=request_options
        )
        return _response.data

    def issue_deferred_credential(
        self,
        *,
        order: PostVciDeferredIssueRequestOrder,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieves a credential after deferred issuance (OID4VCI §9), when the Credential Endpoint returned 202 with a `transaction_id`. Requires the same Bearer access token used at the Credential Endpoint, in the Authorization header or as `accessToken` in the body. `order.transactionId` is required; `order.requestIdentifier` is ignored if supplied, because the server takes it from Authlete's deferred parse response so issuance is bound to the credential request the validated transaction_id resolves to. This endpoint makes two Authlete calls: `/vci/deferred/parse` validates the token (the deferred issue API has no accessToken field and cannot), then `/vci/deferred/issue` issues.

        Parameters
        ----------
        order : PostVciDeferredIssueRequestOrder

        access_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PostVciDeferredIssueRequestOrder

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_deferred_credential(
            order=PostVciDeferredIssueRequestOrder(
                transaction_id="transactionId",
            ),
        )
        """
        _response = self._raw_client.issue_deferred_credential(
            order=order, access_token=access_token, request_options=request_options
        )
        return _response.data

    def vci_well_known_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Alias for VCI metadata endpoint. Returns Verifiable Credential Issuer metadata per OID4VCI §12.2. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vci_well_known_metadata()
        """
        _response = self._raw_client.vci_well_known_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    def oidc_federation_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the OpenID Federation entity configuration per OpenID Federation 1.0. Public endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.oidc_federation_configuration()
        """
        _response = self._raw_client.oidc_federation_configuration(request_options=request_options)
        return _response.data

    def open_id_federation_well_known(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the OpenID Federation entity configuration at the well-known URL for spec compliance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_federation_well_known()
        """
        _response = self._raw_client.open_id_federation_well_known(request_options=request_options)
        return _response.data

    def federation_registration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Handles entity registration in the OpenID Federation.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.federation_registration(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.federation_registration(request=request, request_options=request_options)
        return _response.data

    def create_hardware_security_key(
        self,
        *,
        kty: str,
        hsm_name: str,
        use: typing.Optional[str] = OMIT,
        kid: typing.Optional[str] = OMIT,
        alg: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new Hardware Security Key (HSK). Requires admin Basic auth.

        Parameters
        ----------
        kty : str
            Key type (e.g., EC, RSA)

        hsm_name : str
            HSM provider name

        use : typing.Optional[str]
            Key use (e.g., sig, enc)

        kid : typing.Optional[str]
            Key ID

        alg : typing.Optional[str]
            Algorithm (e.g., ES256, RS256)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_hardware_security_key(
            kty="kty",
            hsm_name="hsmName",
        )
        """
        _response = self._raw_client.create_hardware_security_key(
            kty=kty, hsm_name=hsm_name, use=use, kid=kid, alg=alg, request_options=request_options
        )
        return _response.data

    def get_hardware_security_key(
        self, handle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves a Hardware Security Key by its handle. Requires admin Basic auth.

        Parameters
        ----------
        handle : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_hardware_security_key(
            handle="handle",
        )
        """
        _response = self._raw_client.get_hardware_security_key(handle, request_options=request_options)
        return _response.data

    def delete_hardware_security_key(
        self, handle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a Hardware Security Key by its handle. Requires admin Basic auth.

        Parameters
        ----------
        handle : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_hardware_security_key(
            handle="handle",
        )
        """
        _response = self._raw_client.delete_hardware_security_key(handle, request_options=request_options)
        return _response.data

    def list_hardware_security_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Lists all Hardware Security Keys. Requires admin Basic auth.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_hardware_security_keys()
        """
        _response = self._raw_client.list_hardware_security_keys(request_options=request_options)
        return _response.data

    def fapi_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetFapiConfigResponse:
        """
        Returns the FAPI 2.0 posture of this deployment, read from the live Authlete service configuration. Every field is a value the server has actually checked — none is asserted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFapiConfigResponse
            FAPI configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fapi_configuration()
        """
        _response = self._raw_client.fapi_configuration(request_options=request_options)
        return _response.data

    def fapi_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetFapiStatusResponse:
        """
        Returns the current FAPI 2.0 compliance status including active configurations, test results, and whether CIMD (Client ID Metadata Document) is enabled on the Authlete service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFapiStatusResponse
            FAPI status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fapi_status()
        """
        _response = self._raw_client.fapi_status(request_options=request_options)
        return _response.data

    def process_jwt_authenticated_request(
        self,
        *,
        request: str,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Processes a JAR (JWT-Secured Authorization Request) per RFC 9101. Validates the request object JWT and reports how Authlete parsed it. This is a debugging surface, not a specification endpoint, and it requires admin Basic auth: the underlying authorization response carries a ticket, which is a credential. The response is an allowlist of action, resultCode, resultMessage, responseContent and scopes; ticket, service and client are never returned.

        Parameters
        ----------
        request : str
            JWT-encoded request object

        client_id : typing.Optional[str]
            Client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.process_jwt_authenticated_request(
            request="request",
        )
        """
        _response = self._raw_client.process_jwt_authenticated_request(
            request=request, client_id=client_id, request_options=request_options
        )
        return _response.data

    def authorization_server_metadata_rfc8414(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the authorization server metadata document for MCP (Model Context Protocol) discovery. Serves the same OpenID Connect Discovery content at the RFC 8414 well-known path. MCP clients try this path first, then fall back to /.well-known/openid-configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AS metadata document (same as openid-configuration)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authorization_server_metadata_rfc8414()
        """
        _response = self._raw_client.authorization_server_metadata_rfc8414(request_options=request_options)
        return _response.data

    def native_sso_processing(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Processes a Native SSO (Shared Signal Framework) request per OpenID Native SSO spec. Handles cross-device session management signals.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.native_sso_processing(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.native_sso_processing(request=request, request_options=request_options)
        return _response.data

    def native_sso_logout(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Processes a logout signal via Native SSO. Terminates sessions associated with the subject.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.native_sso_logout(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.native_sso_logout(request=request, request_options=request_options)
        return _response.data

    def oid4vci_credential_issuer_metadata(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        OpenID for Verifiable Credential Issuance 1.0 §12.2 fixes this path at the true root. Serves the same document as GET /api/vci/metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.oid4vci_credential_issuer_metadata()
        """
        _response = self._raw_client.oid4vci_credential_issuer_metadata(request_options=request_options)
        return _response.data

    def device_flow_browser_verification_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        RFC 8628 §3.3 verification_uri. Renders the form where the end-user types their user code. POST /device submits it and POST /device/consent completes the approval.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device_flow_browser_verification_page()
        """
        _response = self._raw_client.device_flow_browser_verification_page(request_options=request_options)
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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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

    async def o_auth_authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: typing.Optional[GetAuthorizationRequestResponseType] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetAuthorizationRequestCodeChallengeMethod] = None,
        claims: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        prompt: typing.Optional[GetAuthorizationRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiates an OAuth 2.0 / OIDC authorization request. Redirects to login or consent pages for interactive flows.

        Three request shapes are accepted, and `client_id` is the only parameter required by all of them:
        - **Plain** — `response_type` + `client_id` (+ `redirect_uri`, which RFC 6749 §3.1.2.3 makes optional when exactly one full redirection URI is registered).
        - **PAR (RFC 9126)** — `client_id` + `request_uri`; the rest was pushed to `/par` beforehand.
        - **JAR (RFC 9101 §5)** — `client_id` + `request`; every other parameter lives inside the signed Request Object. Per RFC 9101 §6.3 the server uses *only* the parameters in the Request Object, so anything duplicated on the query string is ignored rather than merged.

        Parameters
        ----------
        client_id : str
            The only always-required parameter (RFC 6749 §4.1.1; RFC 9101 §5 requires it alongside a Request Object and requires it to match the object's own client_id).

        response_type : typing.Optional[GetAuthorizationRequestResponseType]
            Required for a plain request; supplied inside the Request Object for JAR/PAR.

        request : typing.Optional[str]
            A signed Request Object (JAR, RFC 9101). Verified against the client's registered `jwks` / `jwks_uri` — the client's public keys, not the authorization server's.

        request_uri : typing.Optional[str]
            Reference to a pushed authorization request (RFC 9126). Single-use.

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        code_challenge : typing.Optional[str]
            PKCE code challenge (RFC 7636)

        code_challenge_method : typing.Optional[GetAuthorizationRequestCodeChallengeMethod]

        claims : typing.Optional[str]
            JSON object specifying requested claims (OIDC Core §5.5)

        resource : typing.Optional[str]
            Resource indicator (RFC 8707)

        prompt : typing.Optional[GetAuthorizationRequestPrompt]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_authorization_endpoint(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.o_auth_authorization_endpoint(
            client_id=client_id,
            response_type=response_type,
            request=request,
            request_uri=request_uri,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            claims=claims,
            resource=resource,
            prompt=prompt,
            request_options=request_options,
        )
        return _response.data

    async def o_auth_token_endpoint(
        self,
        *,
        grant_type: PostTokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        auth_req_id: typing.Optional[str] = OMIT,
        device_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostTokenResponse:
        """
        Exchanges authorization codes, refresh tokens, client credentials, or other grant types for access tokens.

        Parameters
        ----------
        grant_type : PostTokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        assertion : typing.Optional[str]

        resource : typing.Optional[str]

        auth_req_id : typing.Optional[str]

        device_code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTokenResponse
            Token issued successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostTokenRequestGrantType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_token_endpoint(
                grant_type=PostTokenRequestGrantType.AUTHORIZATION_CODE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.o_auth_token_endpoint(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            username=username,
            password=password,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            assertion=assertion,
            resource=resource,
            auth_req_id=auth_req_id,
            device_code=device_code,
            request_options=request_options,
        )
        return _response.data

    async def user_info_endpoint(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns claims about the authenticated end-user. Accepts either the Bearer scheme (RFC 6750 §2.1) or the DPoP scheme (RFC 9449 §7.1); the scheme name is case-insensitive. A token issued with token_type: DPoP MUST use the DPoP scheme and be accompanied by a proof — presenting it as Bearer is rejected per RFC 9449 §7.2. Requires the openid scope.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            User claims

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_info_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.user_info_endpoint(request_options=request_options)
        return _response.data

    async def user_info_endpoint_post(
        self, *, access_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        As GET. The token may also be sent as access_token in an application/x-www-form-urlencoded body (RFC 6750 §2.2), but not by both methods at once. The URI query parameter method of RFC 6750 §2.3 is not supported: RFC 9700 §4.3.2 forbids it.

        Parameters
        ----------
        access_token : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_info_endpoint_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.user_info_endpoint_post(
            access_token=access_token, request_options=request_options
        )
        return _response.data

    async def authlete_specific_token_introspection(
        self,
        *,
        token: str,
        scopes: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        acr_values: typing.Optional[str] = OMIT,
        max_age: typing.Optional[int] = OMIT,
        resources: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Non-standard token introspection returning Authlete's raw response. Supports RFC 9470 step-up authentication validation via acrValues and maxAge parameters.

        Parameters
        ----------
        token : str
            The access token to introspect.

        scopes : typing.Optional[str]
            Space-separated list of required scopes.

        subject : typing.Optional[str]
            Required subject (user) for the token.

        acr_values : typing.Optional[str]
            RFC 9470: Space-separated ACR values one of which the token must satisfy.

        max_age : typing.Optional[int]
            RFC 9470: Maximum authentication age in seconds.

        resources : typing.Optional[str]
            Space-separated resource indicators.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authlete_specific_token_introspection(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authlete_specific_token_introspection(
            token=token,
            scopes=scopes,
            subject=subject,
            acr_values=acr_values,
            max_age=max_age,
            resources=resources,
            request_options=request_options,
        )
        return _response.data

    async def rfc7662token_introspection(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostIntrospectionStandardResponse:
        """
        Standard OAuth 2.0 token introspection as defined in RFC 7662.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostIntrospectionStandardResponse
            Introspection result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rfc7662token_introspection(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rfc7662token_introspection(token=token, request_options=request_options)
        return _response.data

    async def rfc7009token_revocation(
        self,
        *,
        token: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes an access or refresh token.

        Parameters
        ----------
        token : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rfc7009token_revocation(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rfc7009token_revocation(
            token=token, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def login_form(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Renders the login page (EJS template).

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.login_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.login_form(request_options=request_options)
        return _response.data

    async def submit_login(
        self,
        *,
        username: str,
        password: str,
        csrf: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Validates username/password and initiates the OAuth session.

        Parameters
        ----------
        username : str

        password : str

        csrf : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.submit_login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_login(
            username=username, password=password, csrf=csrf, request_options=request_options
        )
        return _response.data

    async def consent_form(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Renders the consent page (EJS template).

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.consent_form(request_options=request_options)
        return _response.data

    async def submit_consent_decision(
        self,
        *,
        decision: PostSessionConsentRequestDecision,
        csrf: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Approves or denies the OAuth authorization request.

        Parameters
        ----------
        decision : PostSessionConsentRequestDecision

        csrf : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostSessionConsentRequestDecision

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.submit_consent_decision(
                decision=PostSessionConsentRequestDecision.APPROVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_consent_decision(
            decision=decision, csrf=csrf, request_options=request_options
        )
        return _response.data

    async def open_id_connect_discovery(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the OIDC Discovery document (RFC 8414).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Discovery document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_connect_discovery()


        asyncio.run(main())
        """
        _response = await self._raw_client.open_id_connect_discovery(request_options=request_options)
        return _response.data

    async def jwks_endpoint(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the JSON Web Key Set (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JWK Set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jwks_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.jwks_endpoint(request_options=request_options)
        return _response.data

    async def dynamic_client_registration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Registers a new OAuth client (RFC 7591). Requires admin Basic auth.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dynamic_client_registration(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dynamic_client_registration(request=request, request_options=request_options)
        return _response.data

    async def get_registered_client(
        self,
        *,
        token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieves a client by registration access token (RFC 7592).

        Parameters
        ----------
        token : typing.Optional[str]

        client_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_registered_client()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_registered_client(
            token=token, client_id=client_id, request_options=request_options
        )
        return _response.data

    async def update_registered_client(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a client's registration (RFC 7592).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_registered_client(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_registered_client(request=request, request_options=request_options)
        return _response.data

    async def delete_registered_client(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a client's registration (RFC 7592).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_registered_client(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_registered_client(request=request, request_options=request_options)
        return _response.data

    async def ciba_backchannel_authentication(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Starts a CIBA authentication request (Client-Initiated Backchannel Authentication, OIDC CIBA Core). The `parameters` field is a URL-encoded string containing the backchannel authentication request (login_hint, scope, client_notification_token, etc.). Client credentials are passed as `clientId`/`clientSecret` in the JSON body.

        Parameters
        ----------
        parameters : str
            URL-encoded backchannel authentication request parameters

        client_id : typing.Optional[str]
            Client identifier

        client_secret : typing.Optional[str]
            Client secret for authentication

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ciba_backchannel_authentication(
                parameters="parameters",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ciba_backchannel_authentication(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def issue_ciba_auth_req_id(
        self, *, ticket: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Issues an auth_req_id for a validated CIBA ticket.

        Parameters
        ----------
        ticket : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_ciba_auth_req_id()


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_ciba_auth_req_id(ticket=ticket, request_options=request_options)
        return _response.data

    async def fail_ciba_request(
        self, *, ticket: str, reason: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks a CIBA authentication request as failed. The `reason` field describes why the request failed (e.g., TRANSACTION_FAILED, ACCESS_DENIED).

        Parameters
        ----------
        ticket : str
            Ticket from the authentication endpoint

        reason : str
            Failure reason (e.g. TRANSACTION_FAILED, ACCESS_DENIED)

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fail_ciba_request(
                ticket="ticket",
                reason="reason",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fail_ciba_request(
            ticket=ticket, reason=reason, request_options=request_options
        )
        return _response.data

    async def complete_ciba_request(
        self,
        *,
        ticket: str,
        result: PostCibaCompleteRequestResult,
        subject: str,
        acr: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        claims: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completes a CIBA authentication request with end-user result. Requires `subject` to identify the authenticated user.

        Parameters
        ----------
        ticket : str

        result : PostCibaCompleteRequestResult

        subject : str
            Authenticated user subject

        acr : typing.Optional[str]
            ACR satisfied during authentication

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

        claims : typing.Optional[str]
            JSON string of additional claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostCibaCompleteRequestResult

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.complete_ciba_request(
                ticket="ticket",
                result=PostCibaCompleteRequestResult.AUTHORIZED,
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_ciba_request(
            ticket=ticket,
            result=result,
            subject=subject,
            acr=acr,
            auth_time=auth_time,
            claims=claims,
            request_options=request_options,
        )
        return _response.data

    async def pushed_authorization_request_rfc9126(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostParResponse:
        """
        Pushes authorization request parameters to the PAR endpoint. Returns a `request_uri` for use in `/authorization`. For `CLIENT_SECRET_POST` clients, `client_id` and `client_secret` are merged into the `parameters` string (not sent as separate JSON fields).

        Parameters
        ----------
        parameters : str
            URL-encoded authorization request parameters

        client_id : typing.Optional[str]
            Client ID (merged into parameters for CLIENT_SECRET_POST)

        client_secret : typing.Optional[str]
            Client secret (merged into parameters for CLIENT_SECRET_POST)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostParResponse
            PAR created. The body is RFC 9126 §2.2's, not Authlete's envelope (T1-11).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pushed_authorization_request_rfc9126(
                parameters="parameters",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pushed_authorization_request_rfc9126(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def query_grant_status(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the status of a granted authorization (Grant Management API). This is a protected resource: a DPoP-bound token must be presented with the DPoP scheme and a proof (RFC 9449 §7.1), and Bearer with a proof is refused as the §7.2 downgrade.

        Parameters
        ----------
        grant_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.query_grant_status(
                grant_id="grantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_grant_status(grant_id, request_options=request_options)
        return _response.data

    async def revoke_grant(self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes a granted authorization (Grant Management API). Same presentation rules as the query operation — Bearer or DPoP, per RFC 6750 §2 and RFC 9449 §7.

        Parameters
        ----------
        grant_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revoke_grant(
                grant_id="grantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_grant(grant_id, request_options=request_options)
        return _response.data

    async def rp_initiated_logout_confirmation_page(
        self,
        *,
        client_id: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        id_token_hint: typing.Optional[str] = None,
        backchannel: typing.Optional[GetLogoutRequestBackchannel] = None,
        state: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Renders the logout confirmation page required by OpenID Connect RP-Initiated Logout 1.0 §2. This request destroys nothing: it returns an HTML form carrying a CSRF token and the supplied parameters as hidden fields. Submitting that form (POST /logout) is what ends the session.

        Parameters
        ----------
        client_id : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        id_token_hint : typing.Optional[str]

        backchannel : typing.Optional[GetLogoutRequestBackchannel]
            Trigger backchannel logout delivery on the subsequent POST

        state : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML confirmation page containing the _csrf token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rp_initiated_logout_confirmation_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.rp_initiated_logout_confirmation_page(
            client_id=client_id,
            post_logout_redirect_uri=post_logout_redirect_uri,
            id_token_hint=id_token_hint,
            backchannel=backchannel,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def rp_initiated_logout_end_the_session(
        self,
        *,
        csrf: str,
        client_id: typing.Optional[str] = OMIT,
        post_logout_redirect_uri: typing.Optional[str] = OMIT,
        id_token_hint: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        backchannel: typing.Optional[PostLogoutRequestBackchannel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Ends the session: verifies any id_token_hint against the OP's JWKS, optionally delivers backchannel logout tokens, destroys the session and clears the cookie, then redirects if post_logout_redirect_uri is allowed. Requires the _csrf token issued by GET /logout.

        Parameters
        ----------
        csrf : str
            CSRF token from the GET /logout confirmation page

        client_id : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        id_token_hint : typing.Optional[str]

        state : typing.Optional[str]

        backchannel : typing.Optional[PostLogoutRequestBackchannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Session ended; signed-out page rendered because no allowed redirect target was supplied

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rp_initiated_logout_end_the_session(
                csrf="_csrf",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rp_initiated_logout_end_the_session(
            csrf=csrf,
            client_id=client_id,
            post_logout_redirect_uri=post_logout_redirect_uri,
            id_token_hint=id_token_hint,
            state=state,
            backchannel=backchannel,
            request_options=request_options,
        )
        return _response.data

    async def backchannel_logout_receiver(
        self, *, logout_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Receives incoming backchannel logout tokens from other OPs (OpenID Provider).

        Parameters
        ----------
        logout_token : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.backchannel_logout_receiver(
                logout_token="logout_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.backchannel_logout_receiver(
            logout_token=logout_token, request_options=request_options
        )
        return _response.data

    async def issue_backchannel_logout_token(
        self,
        *,
        client_identifier: str,
        subject: str,
        session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a signed logout token for a client. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        subject : str

        session_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_backchannel_logout_token(
                client_identifier="clientIdentifier",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_backchannel_logout_token(
            client_identifier=client_identifier, subject=subject, session_id=session_id, request_options=request_options
        )
        return _response.data

    async def issue_and_deliver_logout_token(
        self, *, client_identifier: str, subject: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Issues a logout token and delivers it to a specific client. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        subject : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_and_deliver_logout_token(
                client_identifier="clientIdentifier",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_and_deliver_logout_token(
            client_identifier=client_identifier, subject=subject, request_options=request_options
        )
        return _response.data

    async def issue_and_deliver_logout_tokens_to_all_clients(
        self,
        *,
        subject: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues and delivers backchannel logout tokens to every client with a backchannel_logout_uri configured. At least one of `subject` or `sessionId` is required. Requires admin Basic auth.

        Parameters
        ----------
        subject : typing.Optional[str]
            End-user subject to include in logout tokens

        session_id : typing.Optional[str]
            Session ID to include in logout tokens

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_and_deliver_logout_tokens_to_all_clients()


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_and_deliver_logout_tokens_to_all_clients(
            subject=subject, session_id=session_id, request_options=request_options
        )
        return _response.data

    async def list_tokens(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetTokenListResponse:
        """
        Lists all tokens via Authlete token management. Returns paginated results. Requires admin Basic auth.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenListResponse
            Token list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tokens(request_options=request_options)
        return _response.data

    async def create_token_programmatically(
        self,
        *,
        grant_type: str,
        client_id: int,
        subject: typing.Optional[str] = OMIT,
        scopes: typing.Optional[str] = OMIT,
        access_token_duration: typing.Optional[int] = OMIT,
        refresh_token_duration: typing.Optional[int] = OMIT,
        access_token: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new token via Authlete token management. Requires admin Basic auth. The `grantType` uses Authlete enum format (e.g. AUTHORIZATION_CODE, CLIENT_CREDENTIALS).

        Parameters
        ----------
        grant_type : str
            Authlete grant type enum (AUTHORIZATION_CODE, CLIENT_CREDENTIALS, PASSWORD, REFRESH_TOKEN, etc.)

        client_id : int
            Numeric client ID

        subject : typing.Optional[str]
            End-user subject identifier

        scopes : typing.Optional[str]
            Space-separated scope values

        access_token_duration : typing.Optional[int]
            Access token duration in seconds

        refresh_token_duration : typing.Optional[int]
            Refresh token duration in seconds

        access_token : typing.Optional[str]
            Pre-defined access token value

        refresh_token : typing.Optional[str]
            Pre-defined refresh token value

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_token_programmatically(
                grant_type="grantType",
                client_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token_programmatically(
            grant_type=grant_type,
            client_id=client_id,
            subject=subject,
            scopes=scopes,
            access_token_duration=access_token_duration,
            refresh_token_duration=refresh_token_duration,
            access_token=access_token,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    async def delete_token(
        self, access_token_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a token by its identifier. Requires admin Basic auth.

        Parameters
        ----------
        access_token_identifier : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_token(
                access_token_identifier="accessTokenIdentifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_token(access_token_identifier, request_options=request_options)
        return _response.data

    async def update_token_scopes(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a token's scopes or metadata. Requires admin Basic auth.

        Parameters
        ----------
        access_token : typing.Optional[str]

        scopes : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_token_scopes()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_token_scopes(
            access_token=access_token, scopes=scopes, request_options=request_options
        )
        return _response.data

    async def revoke_token_via_management_api(
        self,
        *,
        access_token_identifier: typing.Optional[str] = OMIT,
        refresh_token_identifier: typing.Optional[str] = OMIT,
        client_identifier: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes a token using the Authlete token management API. Accepts multiple identifier fields — at least one is recommended. Requires admin Basic auth.

        Parameters
        ----------
        access_token_identifier : typing.Optional[str]
            Access token identifier to revoke

        refresh_token_identifier : typing.Optional[str]
            Refresh token identifier to revoke

        client_identifier : typing.Optional[str]
            Client identifier to scope the revocation

        subject : typing.Optional[str]
            Subject to scope the revocation

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revoke_token_via_management_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_token_via_management_api(
            access_token_identifier=access_token_identifier,
            refresh_token_identifier=refresh_token_identifier,
            client_identifier=client_identifier,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def reissue_id_token(
        self,
        *,
        access_token: str,
        refresh_token: str,
        sub: typing.Optional[str] = OMIT,
        claims: typing.Optional[str] = OMIT,
        idt_header_params: typing.Optional[str] = OMIT,
        id_token_aud_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reissues an ID token for an existing session using Authlete's ID Token Reissue API. Requires admin Basic auth.

        Parameters
        ----------
        access_token : str
            Current access token

        refresh_token : str
            Current refresh token

        sub : typing.Optional[str]
            Subject to override in the reissued ID token

        claims : typing.Optional[str]
            JSON string of additional claims to embed

        idt_header_params : typing.Optional[str]
            JSON string of additional JOSE header parameters

        id_token_aud_type : typing.Optional[str]
            Audience type for the reissued ID token (string or array)

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reissue_id_token(
                access_token="accessToken",
                refresh_token="refreshToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reissue_id_token(
            access_token=access_token,
            refresh_token=refresh_token,
            sub=sub,
            claims=claims,
            idt_header_params=idt_header_params,
            id_token_aud_type=id_token_aud_type,
            request_options=request_options,
        )
        return _response.data

    async def create_local_jwt(
        self,
        *,
        sub: str,
        aud: str,
        client_id: str,
        iss: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        acr: typing.Optional[str] = None,
        auth_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a locally-signed RFC 9068 JWT access token (development only, no Authlete call). Returns the JWT and the public key for verification. The token carries `typ: at+jwt` and all seven claims RFC 9068 §2.2 marks REQUIRED — it is the repo's worked example of that section, so `client_id` is required here even though the endpoint is a fixture.

        Parameters
        ----------
        sub : str

        aud : str
            Space-delimited; becomes the `aud` array

        client_id : str
            REQUIRED — RFC 9068 §2.2 marks `client_id` a required claim of a JWT access token

        iss : typing.Optional[str]
            Defaults to the JWT_ISSUER environment value when omitted

        scope : typing.Optional[str]
            Space-delimited. RFC 9068 §2.2.3 makes `scope` a SHOULD, so it is omitted from the token rather than emitted empty

        acr : typing.Optional[str]
            ACR claim to embed in the JWT (RFC 9068 §2.2.1, OPTIONAL)

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds) to embed as auth_time. Ignored unless it parses as a positive integer — an unparseable value stamps no claim rather than the Unix epoch

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_local_jwt(
                sub="sub",
                aud="aud",
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_local_jwt(
            sub=sub,
            aud=aud,
            client_id=client_id,
            iss=iss,
            scope=scope,
            acr=acr,
            auth_time=auth_time,
            request_options=request_options,
        )
        return _response.data

    async def prometheus_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns runtime and HTTP metrics in Prometheus text format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Metrics in text format

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.prometheus_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.prometheus_metrics(request_options=request_options)
        return _response.data

    async def server_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetHealthResponse:
        """
        Returns basic server health status.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHealthResponse
            Health status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.server_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.server_health(request_options=request_options)
        return _response.data

    async def aggregate_health_check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetHealthAllResponse:
        """
        Returns combined health status of all dependencies (server, Redis, Authlete).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHealthAllResponse
            All healthy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.aggregate_health_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregate_health_check(request_options=request_options)
        return _response.data

    async def authlete_connectivity_check(
        self,
        *,
        extended: typing.Optional[GetHealthAuthleteRequestExtended] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Checks connectivity to Authlete's API. Add ?extended=true for a detailed check.

        Parameters
        ----------
        extended : typing.Optional[GetHealthAuthleteRequestExtended]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authlete_connectivity_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.authlete_connectivity_check(
            extended=extended, request_options=request_options
        )
        return _response.data

    async def list_all_clients(
        self,
        *,
        start: typing.Optional[int] = None,
        end: typing.Optional[int] = None,
        developer: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Lists all OAuth clients registered in Authlete. Supports pagination via `start` and `end` query parameters. Requires admin Basic auth.

        Parameters
        ----------
        start : typing.Optional[int]
            Start index for pagination

        end : typing.Optional[int]
            End index for pagination

        developer : typing.Optional[str]
            Filter by developer name

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_all_clients()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_clients(
            start=start, end=end, developer=developer, request_options=request_options
        )
        return _response.data

    async def create_client(
        self,
        *,
        client: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client : typing.Optional[typing.Dict[str, typing.Any]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_client()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_client(client=client, request_options=request_options)
        return _response.data

    async def get_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieves an OAuth client by ID. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_client(client_id, request_options=request_options)
        return _response.data

    async def update_client(
        self,
        client_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_client(
                client_id="clientId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client(client_id, request=request, request_options=request_options)
        return _response.data

    async def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an OAuth client. Requires admin Basic auth.

        Parameters
        ----------
        client_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data

    async def update_client_lock_flag(
        self, client_identifier: str, *, client_locked: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the lock flag on a client to prevent or allow credential refresh. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        client_locked : bool

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_client_lock_flag(
                client_identifier="clientIdentifier",
                client_locked=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client_lock_flag(
            client_identifier, client_locked=client_locked, request_options=request_options
        )
        return _response.data

    async def refresh_client_secret(
        self, client_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Generates a new randomly-generated client secret and deactivates the old one. Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.refresh_client_secret(
                client_identifier="clientIdentifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_client_secret(client_identifier, request_options=request_options)
        return _response.data

    async def update_client_secret(
        self, client_identifier: str, *, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets a known client secret value (replaces the current secret). Requires admin Basic auth.

        Parameters
        ----------
        client_identifier : str

        client_secret : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_client_secret(
                client_identifier="clientIdentifier",
                client_secret="clientSecret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client_secret(
            client_identifier, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def list_client_authorizations_for_a_subject(
        self,
        subject: str,
        *,
        start: typing.Optional[int] = None,
        end: typing.Optional[int] = None,
        developer: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Lists all authorizations granted by a specific end-user. Supports pagination.

        Parameters
        ----------
        subject : str

        start : typing.Optional[int]

        end : typing.Optional[int]

        developer : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_client_authorizations_for_a_subject(
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_client_authorizations_for_a_subject(
            subject, start=start, end=end, developer=developer, request_options=request_options
        )
        return _response.data

    async def update_client_authorization(
        self,
        client_id: str,
        *,
        subject: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a client's authorization for a specific user (e.g., modify granted scopes).

        Parameters
        ----------
        client_id : str

        subject : typing.Optional[str]

        scopes : typing.Optional[typing.Sequence[str]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_client_authorization(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client_authorization(
            client_id, subject=subject, scopes=scopes, request_options=request_options
        )
        return _response.data

    async def delete_client_authorization(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a client's authorization for a specific user.

        Parameters
        ----------
        client_id : str

        subject : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_client_authorization(
                client_id="clientId",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_client_authorization(
            client_id, subject, request_options=request_options
        )
        return _response.data

    async def get_granted_scopes(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the scopes that have been granted to a specific client for a specific user.

        Parameters
        ----------
        client_id : str

        subject : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_granted_scopes(
                client_id="clientId",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_granted_scopes(client_id, subject, request_options=request_options)
        return _response.data

    async def delete_granted_scopes(
        self, client_id: str, subject: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all granted scopes for a specific client and user combination.

        Parameters
        ----------
        client_id : str

        subject : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_granted_scopes(
                client_id="clientId",
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_granted_scopes(client_id, subject, request_options=request_options)
        return _response.data

    async def get_requestable_scopes(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the scopes that a client is allowed to request.

        Parameters
        ----------
        client_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_requestable_scopes(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_requestable_scopes(client_id, request_options=request_options)
        return _response.data

    async def update_requestable_scopes(
        self,
        client_id: str,
        *,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sets the scopes that a client is allowed to request.

        Parameters
        ----------
        client_id : str

        scopes : typing.Optional[typing.Sequence[str]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_requestable_scopes(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_requestable_scopes(
            client_id, scopes=scopes, request_options=request_options
        )
        return _response.data

    async def delete_requestable_scopes(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all requestable scopes for a client.

        Parameters
        ----------
        client_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_requestable_scopes(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_requestable_scopes(client_id, request_options=request_options)
        return _response.data

    async def device_authorization(
        self,
        *,
        parameters: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDeviceAuthorizationResponse:
        """
        Initiates the Device Authorization Flow (RFC 8628). Designed for public clients (smart TVs, CLI, IoT) that cannot securely store a client secret. Public clients only need `client_id`; confidential clients can optionally provide `client_secret` for authentication.

        Parameters
        ----------
        parameters : str
            URL-encoded device authorization request parameters (scope, client_id, etc.)

        client_id : typing.Optional[str]
            Client identifier (required for public clients, optional if embedded in parameters)

        client_secret : typing.Optional[str]
            Client secret — only for confidential clients. Public clients omit this.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDeviceAuthorizationResponse
            Device code issued. The body is RFC 8628 §3.2's, not Authlete's envelope (T1-11).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device_authorization(
                parameters="parameters",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.device_authorization(
            parameters=parameters, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def verify_device_user_code(
        self, *, user_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verifies a user code from the Device Flow. Returns VALID if the code exists and has not expired, NOT_EXIST if not found, EXPIRED if expired.

        Parameters
        ----------
        user_code : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.verify_device_user_code(
                user_code="userCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_device_user_code(user_code=user_code, request_options=request_options)
        return _response.data

    async def complete_device_authentication(
        self,
        *,
        user_code: str,
        result: PostDeviceCompleteRequestResult,
        subject: str,
        acr: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        claims: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completes device authentication with end-user approval or denial. Requires `subject` to identify the authenticated user.

        Parameters
        ----------
        user_code : str

        result : PostDeviceCompleteRequestResult

        subject : str
            Authenticated user subject

        acr : typing.Optional[str]
            ACR satisfied during authentication

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

        claims : typing.Optional[str]
            JSON string of additional claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostDeviceCompleteRequestResult

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.complete_device_authentication(
                user_code="userCode",
                result=PostDeviceCompleteRequestResult.SUCCESS,
                subject="subject",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_device_authentication(
            user_code=user_code,
            result=result,
            subject=subject,
            acr=acr,
            auth_time=auth_time,
            claims=claims,
            request_options=request_options,
        )
        return _response.data

    async def vci_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves Verifiable Credential Issuer metadata. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vci_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.vci_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    async def vci_jwt_issuer_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves the JWT issuer configuration for VCI. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vci_jwt_issuer_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.vci_jwt_issuer_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    async def vci_jwks(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves the JWK Set for VCI. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vci_jwks()


        asyncio.run(main())
        """
        _response = await self._raw_client.vci_jwks(pretty=pretty, request_options=request_options)
        return _response.data

    async def create_credential_offer(
        self,
        *,
        credential_configuration_ids: typing.Sequence[str],
        subject: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        acr: typing.Optional[str] = OMIT,
        tx_code: typing.Optional[str] = OMIT,
        tx_code_input_mode: typing.Optional[str] = OMIT,
        tx_code_description: typing.Optional[str] = OMIT,
        authorization_code_grant_included: typing.Optional[bool] = OMIT,
        issuer_state_included: typing.Optional[bool] = OMIT,
        pre_authorized_code_grant_included: typing.Optional[bool] = OMIT,
        context: typing.Optional[str] = OMIT,
        properties: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        jwt_at_claims: typing.Optional[str] = OMIT,
        auth_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new OID4VCI credential offer. Requires admin Basic auth. The `credentialConfigurationIds` field must reference pre-configured credential configurations in Authlete.

        Parameters
        ----------
        credential_configuration_ids : typing.Sequence[str]
            IDs of credential configurations to offer

        subject : typing.Optional[str]
            Pre-determined subject for the credential

        duration : typing.Optional[float]
            Offer duration in seconds

        acr : typing.Optional[str]
            ACR value for the offer

        tx_code : typing.Optional[str]
            Pre-defined transaction code

        tx_code_input_mode : typing.Optional[str]
            Transaction code input mode (text or numeric)

        tx_code_description : typing.Optional[str]
            Description of the transaction code for the user

        authorization_code_grant_included : typing.Optional[bool]
            Include authorization code grant in the offer

        issuer_state_included : typing.Optional[bool]
            Include issuer state in the offer

        pre_authorized_code_grant_included : typing.Optional[bool]
            Include pre-authorized code grant in the offer

        context : typing.Optional[str]
            Context string for the offer

        properties : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Additional properties to include

        jwt_at_claims : typing.Optional[str]
            JSON string of additional JWT access token claims

        auth_time : typing.Optional[int]
            Authentication time (epoch seconds)

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_credential_offer(
                credential_configuration_ids=["credentialConfigurationIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_credential_offer(
            credential_configuration_ids=credential_configuration_ids,
            subject=subject,
            duration=duration,
            acr=acr,
            tx_code=tx_code,
            tx_code_input_mode=tx_code_input_mode,
            tx_code_description=tx_code_description,
            authorization_code_grant_included=authorization_code_grant_included,
            issuer_state_included=issuer_state_included,
            pre_authorized_code_grant_included=pre_authorized_code_grant_included,
            context=context,
            properties=properties,
            jwt_at_claims=jwt_at_claims,
            auth_time=auth_time,
            request_options=request_options,
        )
        return _response.data

    async def get_offer_information(
        self, *, identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves information about a credential offer. Requires admin Basic auth.

        Parameters
        ----------
        identifier : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_offer_information(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_offer_information(identifier=identifier, request_options=request_options)
        return _response.data

    async def issue_single_credential(
        self,
        *,
        access_token: str,
        order: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues a single verifiable credential. Requires a Bearer access token (from the pre-authorized code flow) in the Authorization header, or `accessToken` in the request body. Returns 202 for deferred issuance.

        Parameters
        ----------
        access_token : str

        order : typing.Optional[typing.Dict[str, typing.Any]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_single_credential(
                access_token="accessToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_single_credential(
            access_token=access_token, order=order, request_options=request_options
        )
        return _response.data

    async def issue_batch_credentials(
        self,
        *,
        access_token: str,
        orders: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Issues multiple verifiable credentials in a single request (OID4VCI §10). Requires a Bearer access token in the Authorization header or `accessToken` in the body.

        Parameters
        ----------
        access_token : str
            Access token from pre-authorized code flow

        orders : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Array of credential issuance orders

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_batch_credentials(
                access_token="accessToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_batch_credentials(
            access_token=access_token, orders=orders, request_options=request_options
        )
        return _response.data

    async def issue_deferred_credential(
        self,
        *,
        order: PostVciDeferredIssueRequestOrder,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieves a credential after deferred issuance (OID4VCI §9), when the Credential Endpoint returned 202 with a `transaction_id`. Requires the same Bearer access token used at the Credential Endpoint, in the Authorization header or as `accessToken` in the body. `order.transactionId` is required; `order.requestIdentifier` is ignored if supplied, because the server takes it from Authlete's deferred parse response so issuance is bound to the credential request the validated transaction_id resolves to. This endpoint makes two Authlete calls: `/vci/deferred/parse` validates the token (the deferred issue API has no accessToken field and cannot), then `/vci/deferred/issue` issues.

        Parameters
        ----------
        order : PostVciDeferredIssueRequestOrder

        access_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostVciDeferredIssueRequestOrder

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_deferred_credential(
                order=PostVciDeferredIssueRequestOrder(
                    transaction_id="transactionId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_deferred_credential(
            order=order, access_token=access_token, request_options=request_options
        )
        return _response.data

    async def vci_well_known_metadata(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Alias for VCI metadata endpoint. Returns Verifiable Credential Issuer metadata per OID4VCI §12.2. Public endpoint.

        Parameters
        ----------
        pretty : typing.Optional[bool]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vci_well_known_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.vci_well_known_metadata(pretty=pretty, request_options=request_options)
        return _response.data

    async def oidc_federation_configuration(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the OpenID Federation entity configuration per OpenID Federation 1.0. Public endpoint.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.oidc_federation_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_federation_configuration(request_options=request_options)
        return _response.data

    async def open_id_federation_well_known(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the OpenID Federation entity configuration at the well-known URL for spec compliance.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_federation_well_known()


        asyncio.run(main())
        """
        _response = await self._raw_client.open_id_federation_well_known(request_options=request_options)
        return _response.data

    async def federation_registration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Handles entity registration in the OpenID Federation.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.federation_registration(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.federation_registration(request=request, request_options=request_options)
        return _response.data

    async def create_hardware_security_key(
        self,
        *,
        kty: str,
        hsm_name: str,
        use: typing.Optional[str] = OMIT,
        kid: typing.Optional[str] = OMIT,
        alg: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new Hardware Security Key (HSK). Requires admin Basic auth.

        Parameters
        ----------
        kty : str
            Key type (e.g., EC, RSA)

        hsm_name : str
            HSM provider name

        use : typing.Optional[str]
            Key use (e.g., sig, enc)

        kid : typing.Optional[str]
            Key ID

        alg : typing.Optional[str]
            Algorithm (e.g., ES256, RS256)

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_hardware_security_key(
                kty="kty",
                hsm_name="hsmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_hardware_security_key(
            kty=kty, hsm_name=hsm_name, use=use, kid=kid, alg=alg, request_options=request_options
        )
        return _response.data

    async def get_hardware_security_key(
        self, handle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retrieves a Hardware Security Key by its handle. Requires admin Basic auth.

        Parameters
        ----------
        handle : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_hardware_security_key(
                handle="handle",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hardware_security_key(handle, request_options=request_options)
        return _response.data

    async def delete_hardware_security_key(
        self, handle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a Hardware Security Key by its handle. Requires admin Basic auth.

        Parameters
        ----------
        handle : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_hardware_security_key(
                handle="handle",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_hardware_security_key(handle, request_options=request_options)
        return _response.data

    async def list_hardware_security_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Lists all Hardware Security Keys. Requires admin Basic auth.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_hardware_security_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_hardware_security_keys(request_options=request_options)
        return _response.data

    async def fapi_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFapiConfigResponse:
        """
        Returns the FAPI 2.0 posture of this deployment, read from the live Authlete service configuration. Every field is a value the server has actually checked — none is asserted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFapiConfigResponse
            FAPI configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fapi_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.fapi_configuration(request_options=request_options)
        return _response.data

    async def fapi_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetFapiStatusResponse:
        """
        Returns the current FAPI 2.0 compliance status including active configurations, test results, and whether CIMD (Client ID Metadata Document) is enabled on the Authlete service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFapiStatusResponse
            FAPI status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fapi_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.fapi_status(request_options=request_options)
        return _response.data

    async def process_jwt_authenticated_request(
        self,
        *,
        request: str,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Processes a JAR (JWT-Secured Authorization Request) per RFC 9101. Validates the request object JWT and reports how Authlete parsed it. This is a debugging surface, not a specification endpoint, and it requires admin Basic auth: the underlying authorization response carries a ticket, which is a credential. The response is an allowlist of action, resultCode, resultMessage, responseContent and scopes; ticket, service and client are never returned.

        Parameters
        ----------
        request : str
            JWT-encoded request object

        client_id : typing.Optional[str]
            Client identifier

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.process_jwt_authenticated_request(
                request="request",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.process_jwt_authenticated_request(
            request=request, client_id=client_id, request_options=request_options
        )
        return _response.data

    async def authorization_server_metadata_rfc8414(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the authorization server metadata document for MCP (Model Context Protocol) discovery. Serves the same OpenID Connect Discovery content at the RFC 8414 well-known path. MCP clients try this path first, then fall back to /.well-known/openid-configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            AS metadata document (same as openid-configuration)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authorization_server_metadata_rfc8414()


        asyncio.run(main())
        """
        _response = await self._raw_client.authorization_server_metadata_rfc8414(request_options=request_options)
        return _response.data

    async def native_sso_processing(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Processes a Native SSO (Shared Signal Framework) request per OpenID Native SSO spec. Handles cross-device session management signals.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.native_sso_processing(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.native_sso_processing(request=request, request_options=request_options)
        return _response.data

    async def native_sso_logout(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Processes a logout signal via Native SSO. Terminates sessions associated with the subject.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.native_sso_logout(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.native_sso_logout(request=request, request_options=request_options)
        return _response.data

    async def oid4vci_credential_issuer_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        OpenID for Verifiable Credential Issuance 1.0 §12.2 fixes this path at the true root. Serves the same document as GET /api/vci/metadata.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.oid4vci_credential_issuer_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.oid4vci_credential_issuer_metadata(request_options=request_options)
        return _response.data

    async def device_flow_browser_verification_page(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        RFC 8628 §3.3 verification_uri. Renders the form where the end-user types their user code. POST /device submits it and POST /device/consent completes the approval.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device_flow_browser_verification_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.device_flow_browser_verification_page(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
