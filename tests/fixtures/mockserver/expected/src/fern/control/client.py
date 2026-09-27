

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.body import Body
from ..types.clock_response import ClockResponse
from ..types.clock_status import ClockStatus
from ..types.http_request import HttpRequest
from ..types.http_response import HttpResponse
from ..types.jwt import Jwt
from ..types.key_to_multi_value import KeyToMultiValue
from ..types.key_to_value import KeyToValue
from ..types.ports import Ports
from ..types.protocol import Protocol
from ..types.socket_address import SocketAddress
from ..types.string_or_json_schema import StringOrJsonSchema
from .raw_client import AsyncRawControlClient, RawControlClient
from .types.clock_request_action import ClockRequestAction
from .types.delete_mockserver_cassettes_response import DeleteMockserverCassettesResponse
from .types.get_mockserver_breakpoint_matchers_response import GetMockserverBreakpointMatchersResponse
from .types.get_mockserver_cassettes_response import GetMockserverCassettesResponse
from .types.get_mockserver_http3status_response import GetMockserverHttp3StatusResponse
from .types.get_mockserver_mode_response import GetMockserverModeResponse
from .types.get_mockserver_proxy_configuration_response import GetMockserverProxyConfigurationResponse
from .types.get_mockserver_ready_response import GetMockserverReadyResponse
from .types.put_mockserver_breakpoint_matcher_clear_response import PutMockserverBreakpointMatcherClearResponse
from .types.put_mockserver_breakpoint_matcher_remove_response import PutMockserverBreakpointMatcherRemoveResponse
from .types.put_mockserver_breakpoint_matcher_request_phases_item import PutMockserverBreakpointMatcherRequestPhasesItem
from .types.put_mockserver_breakpoint_matcher_response import PutMockserverBreakpointMatcherResponse
from .types.put_mockserver_breakpoint_matchers_response import PutMockserverBreakpointMatchersResponse
from .types.put_mockserver_cassettes_response import PutMockserverCassettesResponse
from .types.put_mockserver_clear_request_body import PutMockserverClearRequestBody
from .types.put_mockserver_clear_request_type import PutMockserverClearRequestType
from .types.put_mockserver_mode_request_mode import PutMockserverModeRequestMode
from .types.put_mockserver_mode_response import PutMockserverModeResponse
from .types.put_mockserver_retrieve_request_body import PutMockserverRetrieveRequestBody
from .types.put_mockserver_retrieve_request_format import PutMockserverRetrieveRequestFormat
from .types.put_mockserver_retrieve_request_type import PutMockserverRetrieveRequestType
from .types.put_mockserver_retrieve_response import PutMockserverRetrieveResponse


OMIT = typing.cast(typing.Any, ...)


class ControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawControlClient
        """
        return self._raw_client

    def clears_expectations_and_recorded_requests_that_match_the_request_matcher(
        self,
        *,
        request: PutMockserverClearRequestBody,
        type: typing.Optional[PutMockserverClearRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : PutMockserverClearRequestBody

        type : typing.Optional[PutMockserverClearRequestType]
            specifies the type of information to clear, default if not specified is "all", supported values are "all", "log", "expectations"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ExpectationId, FernApi

        client = FernApi()
        client.control.clears_expectations_and_recorded_requests_that_match_the_request_matcher(
            request=ExpectationId(
                id="id",
            ),
        )
        """
        _response = self._raw_client.clears_expectations_and_recorded_requests_that_match_the_request_matcher(
            request=request, type=type, request_options=request_options
        )
        return _response.data

    def clears_all_expectations_and_recorded_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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

        client = FernApi()
        client.control.clears_all_expectations_and_recorded_requests()
        """
        _response = self._raw_client.clears_all_expectations_and_recorded_requests(request_options=request_options)
        return _response.data

    def retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
        self,
        *,
        request: PutMockserverRetrieveRequestBody,
        format: typing.Optional[PutMockserverRetrieveRequestFormat] = None,
        type: typing.Optional[PutMockserverRetrieveRequestType] = None,
        correlation_id: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        fan_in_local_only: typing.Optional[bool] = None,
        forward_unmatched_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverRetrieveResponse:
        """
        Parameters
        ----------
        request : PutMockserverRetrieveRequestBody

        format : typing.Optional[PutMockserverRetrieveRequestFormat]
            changes response format, default if not specified is "json". Not every format is valid for every "type" - the combinations are constrained, and an inapplicable pairing is rejected: the code-generation formats ("java", "javascript", "python", "go", "csharp", "ruby", "rust", "php") apply to "recorded_expectations" and "active_expectations" only and are rejected for "requests" and "request_responses"; the export formats ("openapi", "postman", "bruno") apply to "active_expectations" only; "curl" applies to "requests" and "request_responses" only. "json", "log_entries" and "har" are unconstrained.

        type : typing.Optional[PutMockserverRetrieveRequestType]
            specifies the type of object that is retrieve, default if not specified is "requests", supported values are "logs", "requests", "request_responses", "recorded_expectations", "active_expectations", "metrics"

        correlation_id : typing.Optional[str]
            only return entries whose log correlation id matches this value

        namespace : typing.Optional[str]
            tenant filter applied to "active_expectations" retrieval - returns only that namespace's expectations plus global (no-namespace) expectations. When omitted the namespace is taken from the request header named by the matchNamespaceHeader configuration property, if set; when neither is present the retrieval spans all namespaces.

        fan_in_local_only : typing.Optional[bool]
            when true serve only this node's log rather than aggregating peers. Set by peer nodes on cluster fan-in queries as an infinite-recursion guard; callers do not normally set it. Only affects "requests" and "request_responses" retrieval, and only when cluster fan-in is enabled and configured.

        forward_unmatched_to : typing.Optional[str]
            arms record-and-forward for the session - subsequent requests matching no expectation are forwarded to this upstream and captured as recorded expectations, which this and later retrievals return in the requested format. Only arms recording; it does not synthesise traffic, so a retrieval made before any traffic arrives returns nothing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverRetrieveResponse
            recorded requests or active expectations returned

        Examples
        --------
        from fern import ExpectationId, FernApi

        client = FernApi()
        client.control.retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
            request=ExpectationId(
                id="id",
            ),
        )
        """
        _response = (
            self._raw_client.retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
                request=request,
                format=format,
                type=type,
                correlation_id=correlation_id,
                namespace=namespace,
                fan_in_local_only=fan_in_local_only,
                forward_unmatched_to=forward_unmatched_to,
                request_options=request_options,
            )
        )
        return _response.data

    def return_listening_ports(self, *, request_options: typing.Optional[RequestOptions] = None) -> Ports:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ports
            MockServer is running and listening on the listed ports

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.return_listening_ports()
        """
        _response = self._raw_client.return_listening_ports(request_options=request_options)
        return _response.data

    def bind_additional_listening_ports(
        self,
        *,
        ports: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ports:
        """
        only supported on Netty version

        Parameters
        ----------
        ports : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ports
            listening on additional requested ports, note: the response ony contains ports added for the request, to list all ports use /status

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.bind_additional_listening_ports(
            ports=[1090.0],
        )
        """
        _response = self._raw_client.bind_additional_listening_ports(ports=ports, request_options=request_options)
        return _response.data

    def retrieve_the_open_api_specification_for_mock_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        returns the OpenAPI specification describing the MockServer REST API in YAML format

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

        client = FernApi()
        client.control.retrieve_the_open_api_specification_for_mock_server()
        """
        _response = self._raw_client.retrieve_the_open_api_specification_for_mock_server(
            request_options=request_options
        )
        return _response.data

    def retrieve_the_current_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the current MockServer configuration as JSON

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            current configuration returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_the_current_configuration()
        """
        _response = self._raw_client.retrieve_the_current_configuration(request_options=request_options)
        return _response.data

    def update_the_current_configuration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        updates MockServer configuration properties at runtime, only non-null fields in the request body are applied

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            configuration updated successfully, returns the full updated configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.update_the_current_configuration(
            request={"logLevel": "INFO"},
        )
        """
        _response = self._raw_client.update_the_current_configuration(request=request, request_options=request_options)
        return _response.data

    def retrieve_the_current_server_clock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClockStatus:
        """
        Returns the current instant, epoch milliseconds, and whether the clock is frozen.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClockStatus
            current clock status returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_the_current_server_clock_status()
        """
        _response = self._raw_client.retrieve_the_current_server_clock_status(request_options=request_options)
        return _response.data

    def control_the_server_clock_for_deterministic_time_based_testing(
        self,
        *,
        action: ClockRequestAction,
        instant: typing.Optional[dt.datetime] = OMIT,
        duration_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClockResponse:
        """
        Freeze, advance, or reset MockServer's internal clock. The controllable clock affects response template date/time helpers (now_iso_8601, now_epoch, now_rfc_1123, dates.*) and expectation TimeToLive expiry. Event-log timestamps and JWT issuance are not affected.

        Parameters
        ----------
        action : ClockRequestAction
            freeze: freeze the clock at the given instant (or current time if instant is omitted); advance: advance the frozen clock by durationMillis (freezes first if not already frozen); reset: reset the clock to real wall-clock time

        instant : typing.Optional[dt.datetime]
            ISO-8601 instant to freeze at (only used with action 'freeze'; omit to freeze at current time)

        duration_millis : typing.Optional[int]
            number of milliseconds to advance the clock by (required when action is 'advance')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClockResponse
            clock action applied successfully

        Examples
        --------
        import datetime

        from fern.control import ClockRequestAction

        from fern import FernApi

        client = FernApi()
        client.control.control_the_server_clock_for_deterministic_time_based_testing(
            action=ClockRequestAction.FREEZE,
            instant=datetime.datetime.fromisoformat(
                "2026-01-15 10:00:00+00:00",
            ),
        )
        """
        _response = self._raw_client.control_the_server_clock_for_deterministic_time_based_testing(
            action=action, instant=instant, duration_millis=duration_millis, request_options=request_options
        )
        return _response.data

    def retrieve_the_current_proxy_mock_operating_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverModeResponse:
        """
        returns the current operating mode and whether unmatched requests are proxied

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverModeResponse
            current mode returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_the_current_proxy_mock_operating_mode()
        """
        _response = self._raw_client.retrieve_the_current_proxy_mock_operating_mode(request_options=request_options)
        return _response.data

    def set_the_proxy_mock_operating_mode(
        self, *, mode: PutMockserverModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverModeResponse:
        """
        Sets the operating mode that controls how unmatched requests are handled. SIMULATE matches expectations and returns a 404 for unmatched requests; SPY matches expectations but forwards (and records) unmatched requests to the real downstream; CAPTURE forwards and records all traffic (the same proxy-on-no-match behaviour as SPY).

        Parameters
        ----------
        mode : PutMockserverModeRequestMode
            the operating mode to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverModeResponse
            mode set successfully

        Examples
        --------
        from fern.control import PutMockserverModeRequestMode

        from fern import FernApi

        client = FernApi()
        client.control.set_the_proxy_mock_operating_mode(
            mode=PutMockserverModeRequestMode.SIMULATE,
        )
        """
        _response = self._raw_client.set_the_proxy_mock_operating_mode(mode=mode, request_options=request_options)
        return _response.data

    def list_registered_cassettes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverCassettesResponse:
        """
        returns all registered cassettes held in the in-memory cassette registry

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverCassettesResponse
            registered cassettes returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.list_registered_cassettes()
        """
        _response = self._raw_client.list_registered_cassettes(request_options=request_options)
        return _response.data

    def register_or_update_a_record_replay_cassette(
        self,
        *,
        path: str,
        filename: typing.Optional[str] = OMIT,
        expectation_count: typing.Optional[int] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverCassettesResponse:
        """
        Registers (or updates) a cassette entry in the in-memory cassette registry from a JSON body. The 'path' field is required; 'filename', 'expectationCount' and 'origin' are optional.

        Parameters
        ----------
        path : str
            cassette path (required, used as the registry key)

        filename : typing.Optional[str]

        expectation_count : typing.Optional[int]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverCassettesResponse
            cassette registered

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.register_or_update_a_record_replay_cassette(
            path="/api/users",
            filename="users-cassette.json",
            expectation_count=3,
            origin="test",
        )
        """
        _response = self._raw_client.register_or_update_a_record_replay_cassette(
            path=path,
            filename=filename,
            expectation_count=expectation_count,
            origin=origin,
            request_options=request_options,
        )
        return _response.data

    def remove_a_registered_cassette(
        self,
        *,
        path: typing.Optional[str] = None,
        delete_mockserver_cassettes_request_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteMockserverCassettesResponse:
        """
        removes a cassette by path, supplied either as the 'path' query parameter or a JSON body with a 'path' field

        Parameters
        ----------
        path : typing.Optional[str]
            path of the cassette to remove (alternatively supply 'path' in the request body)

        delete_mockserver_cassettes_request_path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverCassettesResponse
            removal processed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.remove_a_registered_cassette(
            delete_mockserver_cassettes_request_path="/api/users",
        )
        """
        _response = self._raw_client.remove_a_registered_cassette(
            path=path,
            delete_mockserver_cassettes_request_path=delete_mockserver_cassettes_request_path,
            request_options=request_options,
        )
        return _response.data

    def replay_a_previously_recorded_request_to_its_original_target(
        self,
        *,
        secure: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[bool] = OMIT,
        method: typing.Optional[StringOrJsonSchema] = OMIT,
        path: typing.Optional[StringOrJsonSchema] = OMIT,
        path_parameters: typing.Optional[KeyToMultiValue] = OMIT,
        query_string_parameters: typing.Optional[KeyToMultiValue] = OMIT,
        body: typing.Optional[Body] = OMIT,
        headers: typing.Optional[KeyToMultiValue] = OMIT,
        cookies: typing.Optional[KeyToValue] = OMIT,
        socket_address: typing.Optional[SocketAddress] = OMIT,
        protocol: typing.Optional[Protocol] = OMIT,
        jwt: typing.Optional[Jwt] = OMIT,
        not_: typing.Optional[bool] = OMIT,
        respond_before_body: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse:
        """
        Re-issues a previously recorded or proxied HTTP request to its upstream target and returns the upstream response. The target host/port is resolved from the socketAddress field or the Host header in the submitted HttpRequest JSON. Subject to the SSRF policy (mockserver.forwardProxyBlockPrivateNetworks) and a 10 MB body-size cap on both the outbound request and the upstream response.

        Parameters
        ----------
        secure : typing.Optional[bool]

        keep_alive : typing.Optional[bool]

        method : typing.Optional[StringOrJsonSchema]

        path : typing.Optional[StringOrJsonSchema]

        path_parameters : typing.Optional[KeyToMultiValue]

        query_string_parameters : typing.Optional[KeyToMultiValue]

        body : typing.Optional[Body]

        headers : typing.Optional[KeyToMultiValue]

        cookies : typing.Optional[KeyToValue]

        socket_address : typing.Optional[SocketAddress]

        protocol : typing.Optional[Protocol]

        jwt : typing.Optional[Jwt]

        not_ : typing.Optional[bool]

        respond_before_body : typing.Optional[bool]
            If true, MockServer responds to a matching request before consuming its body and may close the connection. Required: the matcher must not specify a body matcher, and the action must be RESPONSE or ERROR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse
            upstream response returned successfully

        Examples
        --------
        from fern import FernApi, KeyToMultiValueZeroItem

        client = FernApi()
        client.control.replay_a_previously_recorded_request_to_its_original_target(
            method="PUT",
            path="/mockserver/status",
            headers=[KeyToMultiValueZeroItem()],
        )
        """
        _response = self._raw_client.replay_a_previously_recorded_request_to_its_original_target(
            secure=secure,
            keep_alive=keep_alive,
            method=method,
            path=path,
            path_parameters=path_parameters,
            query_string_parameters=query_string_parameters,
            body=body,
            headers=headers,
            cookies=cookies,
            socket_address=socket_address,
            protocol=protocol,
            jwt=jwt,
            not_=not_,
            respond_before_body=respond_before_body,
            request_options=request_options,
        )
        return _response.data

    def register_a_breakpoint_matcher(
        self,
        *,
        http_request: HttpRequest,
        phases: typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem],
        client_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverBreakpointMatcherResponse:
        """
        Registers a request matcher that activates breakpoints for forwarded/proxied exchanges. When a proxied request matches the httpRequest definition, the exchange is paused at each specified phase. Returns the assigned matcher id and the registered phases. The clientId field is required — paused items are dispatched over the callback WebSocket (/_mockserver_callback_websocket) to the owning client for interactive resolution.

        Parameters
        ----------
        http_request : HttpRequest
            request matcher — same fields as an expectation request matcher

        phases : typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem]
            phases at which matching exchanges will be paused

        client_id : str
            Required. The callback WebSocket client id to dispatch paused items to for interactive resolution. Must be a connected callback client.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherResponse
            matcher registered successfully

        Examples
        --------
        from fern.control import PutMockserverBreakpointMatcherRequestPhasesItem

        from fern import FernApi, HttpRequest

        client = FernApi()
        client.control.register_a_breakpoint_matcher(
            http_request=HttpRequest(
                method="GET",
                path="/api/test",
            ),
            phases=[PutMockserverBreakpointMatcherRequestPhasesItem.REQUEST],
            client_id="test-client-123",
        )
        """
        _response = self._raw_client.register_a_breakpoint_matcher(
            http_request=http_request, phases=phases, client_id=client_id, request_options=request_options
        )
        return _response.data

    def list_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverBreakpointMatchersResponse:
        """
        Returns all currently registered breakpoint matchers. Each entry includes the matcher id, the httpRequest definition, the set of phases, and the clientId.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverBreakpointMatchersResponse
            list of registered matchers

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.list_all_registered_breakpoint_matchers()
        """
        _response = self._raw_client.list_all_registered_breakpoint_matchers(request_options=request_options)
        return _response.data

    def list_all_registered_breakpoint_matchers_put_variant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatchersResponse:
        """
        Same as GET /mockserver/breakpoint/matchers. The PUT variant exists for consistency with other control-plane endpoints that use PUT for idempotent queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatchersResponse
            list of registered matchers

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.list_all_registered_breakpoint_matchers_put_variant()
        """
        _response = self._raw_client.list_all_registered_breakpoint_matchers_put_variant(
            request_options=request_options
        )
        return _response.data

    def remove_a_registered_breakpoint_matcher(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatcherRemoveResponse:
        """
        Removes a previously registered breakpoint matcher by id. Returns status "removed" on success or 404 if no matcher with the given id exists.

        Parameters
        ----------
        id : str
            the matcher id to remove

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherRemoveResponse
            matcher removed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.remove_a_registered_breakpoint_matcher(
            id="78fa44ff-5989-467a-ba44-ff5989667a71",
        )
        """
        _response = self._raw_client.remove_a_registered_breakpoint_matcher(id=id, request_options=request_options)
        return _response.data

    def remove_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatcherClearResponse:
        """
        Removes all registered breakpoint matchers. After this call, no exchanges will be paused at breakpoints until new matchers are registered. Returns the number of matchers cleared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherClearResponse
            all matchers cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.remove_all_registered_breakpoint_matchers()
        """
        _response = self._raw_client.remove_all_registered_breakpoint_matchers(request_options=request_options)
        return _response.data

    def stop_running_process(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        only supported on Netty version

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

        client = FernApi()
        client.control.stop_running_process()
        """
        _response = self._raw_client.stop_running_process(request_options=request_options)
        return _response.data

    def readiness_probe(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetMockserverReadyResponse:
        """
        Readiness probe, distinct from the liveness/status endpoints, which answer 200 the instant the port binds. Stays 503 until the synchronous expectation initializers and any OpenAPI seeding have completed, so an orchestrator does not route traffic before the seeded expectations exist. This is the one control-plane endpoint with no authentication gate, so it remains usable as a Kubernetes readiness probe on an instance whose control plane requires credentials.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverReadyResponse
            initialization complete, ready to serve

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.readiness_probe()
        """
        _response = self._raw_client.readiness_probe(request_options=request_options)
        return _response.data

    def retrieve_the_effective_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns every configuration property with its resolved value and the source tier that supplied it, so an operator can see which of the property file, system properties, environment variables or defaults won. Values detected as sensitive are redacted. Distinct from `/mockserver/configuration`, which reads and writes the mutable runtime configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            effective configuration returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_the_effective_configuration()
        """
        _response = self._raw_client.retrieve_the_effective_configuration(request_options=request_options)
        return _response.data

    def retrieve_client_proxy_setup_details(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverProxyConfigurationResponse:
        """
        Returns everything a client needs to route through this instance as a proxy: the CA certificate (path and PEM), the proxy URL, and ready-to-paste environment-variable snippets for Unix shells and PowerShell. Send `Accept: text/plain` to get the copy-paste snippet on its own instead of the JSON document.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverProxyConfigurationResponse
            proxy configuration returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_client_proxy_setup_details()
        """
        _response = self._raw_client.retrieve_client_proxy_setup_details(request_options=request_options)
        return _response.data

    def retrieve_experimental_http3quic_listener_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverHttp3StatusResponse:
        """
        Reports whether the experimental HTTP/3 listener is enabled, the UDP port it is bound to, and how many QUIC connections are currently active. When the running server is not an HTTP/3-capable instance, `enabled` is false and `port` is -1.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverHttp3StatusResponse
            HTTP/3 status returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.control.retrieve_experimental_http3quic_listener_status()
        """
        _response = self._raw_client.retrieve_experimental_http3quic_listener_status(request_options=request_options)
        return _response.data


class AsyncControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawControlClient
        """
        return self._raw_client

    async def clears_expectations_and_recorded_requests_that_match_the_request_matcher(
        self,
        *,
        request: PutMockserverClearRequestBody,
        type: typing.Optional[PutMockserverClearRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : PutMockserverClearRequestBody

        type : typing.Optional[PutMockserverClearRequestType]
            specifies the type of information to clear, default if not specified is "all", supported values are "all", "log", "expectations"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExpectationId

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.clears_expectations_and_recorded_requests_that_match_the_request_matcher(
                request=ExpectationId(
                    id="id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clears_expectations_and_recorded_requests_that_match_the_request_matcher(
            request=request, type=type, request_options=request_options
        )
        return _response.data

    async def clears_all_expectations_and_recorded_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.clears_all_expectations_and_recorded_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.clears_all_expectations_and_recorded_requests(
            request_options=request_options
        )
        return _response.data

    async def retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
        self,
        *,
        request: PutMockserverRetrieveRequestBody,
        format: typing.Optional[PutMockserverRetrieveRequestFormat] = None,
        type: typing.Optional[PutMockserverRetrieveRequestType] = None,
        correlation_id: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        fan_in_local_only: typing.Optional[bool] = None,
        forward_unmatched_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverRetrieveResponse:
        """
        Parameters
        ----------
        request : PutMockserverRetrieveRequestBody

        format : typing.Optional[PutMockserverRetrieveRequestFormat]
            changes response format, default if not specified is "json". Not every format is valid for every "type" - the combinations are constrained, and an inapplicable pairing is rejected: the code-generation formats ("java", "javascript", "python", "go", "csharp", "ruby", "rust", "php") apply to "recorded_expectations" and "active_expectations" only and are rejected for "requests" and "request_responses"; the export formats ("openapi", "postman", "bruno") apply to "active_expectations" only; "curl" applies to "requests" and "request_responses" only. "json", "log_entries" and "har" are unconstrained.

        type : typing.Optional[PutMockserverRetrieveRequestType]
            specifies the type of object that is retrieve, default if not specified is "requests", supported values are "logs", "requests", "request_responses", "recorded_expectations", "active_expectations", "metrics"

        correlation_id : typing.Optional[str]
            only return entries whose log correlation id matches this value

        namespace : typing.Optional[str]
            tenant filter applied to "active_expectations" retrieval - returns only that namespace's expectations plus global (no-namespace) expectations. When omitted the namespace is taken from the request header named by the matchNamespaceHeader configuration property, if set; when neither is present the retrieval spans all namespaces.

        fan_in_local_only : typing.Optional[bool]
            when true serve only this node's log rather than aggregating peers. Set by peer nodes on cluster fan-in queries as an infinite-recursion guard; callers do not normally set it. Only affects "requests" and "request_responses" retrieval, and only when cluster fan-in is enabled and configured.

        forward_unmatched_to : typing.Optional[str]
            arms record-and-forward for the session - subsequent requests matching no expectation are forwarded to this upstream and captured as recorded expectations, which this and later retrievals return in the requested format. Only arms recording; it does not synthesise traffic, so a retrieval made before any traffic arrives returns nothing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverRetrieveResponse
            recorded requests or active expectations returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExpectationId

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
                request=ExpectationId(
                    id="id",
                ),
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.retrieve_recorded_requests_active_expectations_recorded_expectations_or_log_messages(
                request=request,
                format=format,
                type=type,
                correlation_id=correlation_id,
                namespace=namespace,
                fan_in_local_only=fan_in_local_only,
                forward_unmatched_to=forward_unmatched_to,
                request_options=request_options,
            )
        )
        return _response.data

    async def return_listening_ports(self, *, request_options: typing.Optional[RequestOptions] = None) -> Ports:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ports
            MockServer is running and listening on the listed ports

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.return_listening_ports()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_listening_ports(request_options=request_options)
        return _response.data

    async def bind_additional_listening_ports(
        self,
        *,
        ports: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ports:
        """
        only supported on Netty version

        Parameters
        ----------
        ports : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ports
            listening on additional requested ports, note: the response ony contains ports added for the request, to list all ports use /status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.bind_additional_listening_ports(
                ports=[1090.0],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bind_additional_listening_ports(ports=ports, request_options=request_options)
        return _response.data

    async def retrieve_the_open_api_specification_for_mock_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        returns the OpenAPI specification describing the MockServer REST API in YAML format

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_the_open_api_specification_for_mock_server()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_open_api_specification_for_mock_server(
            request_options=request_options
        )
        return _response.data

    async def retrieve_the_current_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns the current MockServer configuration as JSON

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            current configuration returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_the_current_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_current_configuration(request_options=request_options)
        return _response.data

    async def update_the_current_configuration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        updates MockServer configuration properties at runtime, only non-null fields in the request body are applied

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            configuration updated successfully, returns the full updated configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.update_the_current_configuration(
                request={"logLevel": "INFO"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_the_current_configuration(
            request=request, request_options=request_options
        )
        return _response.data

    async def retrieve_the_current_server_clock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClockStatus:
        """
        Returns the current instant, epoch milliseconds, and whether the clock is frozen.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClockStatus
            current clock status returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_the_current_server_clock_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_current_server_clock_status(request_options=request_options)
        return _response.data

    async def control_the_server_clock_for_deterministic_time_based_testing(
        self,
        *,
        action: ClockRequestAction,
        instant: typing.Optional[dt.datetime] = OMIT,
        duration_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClockResponse:
        """
        Freeze, advance, or reset MockServer's internal clock. The controllable clock affects response template date/time helpers (now_iso_8601, now_epoch, now_rfc_1123, dates.*) and expectation TimeToLive expiry. Event-log timestamps and JWT issuance are not affected.

        Parameters
        ----------
        action : ClockRequestAction
            freeze: freeze the clock at the given instant (or current time if instant is omitted); advance: advance the frozen clock by durationMillis (freezes first if not already frozen); reset: reset the clock to real wall-clock time

        instant : typing.Optional[dt.datetime]
            ISO-8601 instant to freeze at (only used with action 'freeze'; omit to freeze at current time)

        duration_millis : typing.Optional[int]
            number of milliseconds to advance the clock by (required when action is 'advance')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClockResponse
            clock action applied successfully

        Examples
        --------
        import asyncio
        import datetime

        from fern.control import ClockRequestAction

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.control_the_server_clock_for_deterministic_time_based_testing(
                action=ClockRequestAction.FREEZE,
                instant=datetime.datetime.fromisoformat(
                    "2026-01-15 10:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.control_the_server_clock_for_deterministic_time_based_testing(
            action=action, instant=instant, duration_millis=duration_millis, request_options=request_options
        )
        return _response.data

    async def retrieve_the_current_proxy_mock_operating_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverModeResponse:
        """
        returns the current operating mode and whether unmatched requests are proxied

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverModeResponse
            current mode returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_the_current_proxy_mock_operating_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_current_proxy_mock_operating_mode(
            request_options=request_options
        )
        return _response.data

    async def set_the_proxy_mock_operating_mode(
        self, *, mode: PutMockserverModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverModeResponse:
        """
        Sets the operating mode that controls how unmatched requests are handled. SIMULATE matches expectations and returns a 404 for unmatched requests; SPY matches expectations but forwards (and records) unmatched requests to the real downstream; CAPTURE forwards and records all traffic (the same proxy-on-no-match behaviour as SPY).

        Parameters
        ----------
        mode : PutMockserverModeRequestMode
            the operating mode to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverModeResponse
            mode set successfully

        Examples
        --------
        import asyncio

        from fern.control import PutMockserverModeRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.set_the_proxy_mock_operating_mode(
                mode=PutMockserverModeRequestMode.SIMULATE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_the_proxy_mock_operating_mode(mode=mode, request_options=request_options)
        return _response.data

    async def list_registered_cassettes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverCassettesResponse:
        """
        returns all registered cassettes held in the in-memory cassette registry

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverCassettesResponse
            registered cassettes returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.list_registered_cassettes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_registered_cassettes(request_options=request_options)
        return _response.data

    async def register_or_update_a_record_replay_cassette(
        self,
        *,
        path: str,
        filename: typing.Optional[str] = OMIT,
        expectation_count: typing.Optional[int] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverCassettesResponse:
        """
        Registers (or updates) a cassette entry in the in-memory cassette registry from a JSON body. The 'path' field is required; 'filename', 'expectationCount' and 'origin' are optional.

        Parameters
        ----------
        path : str
            cassette path (required, used as the registry key)

        filename : typing.Optional[str]

        expectation_count : typing.Optional[int]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverCassettesResponse
            cassette registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.register_or_update_a_record_replay_cassette(
                path="/api/users",
                filename="users-cassette.json",
                expectation_count=3,
                origin="test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_or_update_a_record_replay_cassette(
            path=path,
            filename=filename,
            expectation_count=expectation_count,
            origin=origin,
            request_options=request_options,
        )
        return _response.data

    async def remove_a_registered_cassette(
        self,
        *,
        path: typing.Optional[str] = None,
        delete_mockserver_cassettes_request_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteMockserverCassettesResponse:
        """
        removes a cassette by path, supplied either as the 'path' query parameter or a JSON body with a 'path' field

        Parameters
        ----------
        path : typing.Optional[str]
            path of the cassette to remove (alternatively supply 'path' in the request body)

        delete_mockserver_cassettes_request_path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverCassettesResponse
            removal processed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.remove_a_registered_cassette(
                delete_mockserver_cassettes_request_path="/api/users",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_registered_cassette(
            path=path,
            delete_mockserver_cassettes_request_path=delete_mockserver_cassettes_request_path,
            request_options=request_options,
        )
        return _response.data

    async def replay_a_previously_recorded_request_to_its_original_target(
        self,
        *,
        secure: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[bool] = OMIT,
        method: typing.Optional[StringOrJsonSchema] = OMIT,
        path: typing.Optional[StringOrJsonSchema] = OMIT,
        path_parameters: typing.Optional[KeyToMultiValue] = OMIT,
        query_string_parameters: typing.Optional[KeyToMultiValue] = OMIT,
        body: typing.Optional[Body] = OMIT,
        headers: typing.Optional[KeyToMultiValue] = OMIT,
        cookies: typing.Optional[KeyToValue] = OMIT,
        socket_address: typing.Optional[SocketAddress] = OMIT,
        protocol: typing.Optional[Protocol] = OMIT,
        jwt: typing.Optional[Jwt] = OMIT,
        not_: typing.Optional[bool] = OMIT,
        respond_before_body: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse:
        """
        Re-issues a previously recorded or proxied HTTP request to its upstream target and returns the upstream response. The target host/port is resolved from the socketAddress field or the Host header in the submitted HttpRequest JSON. Subject to the SSRF policy (mockserver.forwardProxyBlockPrivateNetworks) and a 10 MB body-size cap on both the outbound request and the upstream response.

        Parameters
        ----------
        secure : typing.Optional[bool]

        keep_alive : typing.Optional[bool]

        method : typing.Optional[StringOrJsonSchema]

        path : typing.Optional[StringOrJsonSchema]

        path_parameters : typing.Optional[KeyToMultiValue]

        query_string_parameters : typing.Optional[KeyToMultiValue]

        body : typing.Optional[Body]

        headers : typing.Optional[KeyToMultiValue]

        cookies : typing.Optional[KeyToValue]

        socket_address : typing.Optional[SocketAddress]

        protocol : typing.Optional[Protocol]

        jwt : typing.Optional[Jwt]

        not_ : typing.Optional[bool]

        respond_before_body : typing.Optional[bool]
            If true, MockServer responds to a matching request before consuming its body and may close the connection. Required: the matcher must not specify a body matcher, and the action must be RESPONSE or ERROR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse
            upstream response returned successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KeyToMultiValueZeroItem

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.replay_a_previously_recorded_request_to_its_original_target(
                method="PUT",
                path="/mockserver/status",
                headers=[KeyToMultiValueZeroItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replay_a_previously_recorded_request_to_its_original_target(
            secure=secure,
            keep_alive=keep_alive,
            method=method,
            path=path,
            path_parameters=path_parameters,
            query_string_parameters=query_string_parameters,
            body=body,
            headers=headers,
            cookies=cookies,
            socket_address=socket_address,
            protocol=protocol,
            jwt=jwt,
            not_=not_,
            respond_before_body=respond_before_body,
            request_options=request_options,
        )
        return _response.data

    async def register_a_breakpoint_matcher(
        self,
        *,
        http_request: HttpRequest,
        phases: typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem],
        client_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverBreakpointMatcherResponse:
        """
        Registers a request matcher that activates breakpoints for forwarded/proxied exchanges. When a proxied request matches the httpRequest definition, the exchange is paused at each specified phase. Returns the assigned matcher id and the registered phases. The clientId field is required — paused items are dispatched over the callback WebSocket (/_mockserver_callback_websocket) to the owning client for interactive resolution.

        Parameters
        ----------
        http_request : HttpRequest
            request matcher — same fields as an expectation request matcher

        phases : typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem]
            phases at which matching exchanges will be paused

        client_id : str
            Required. The callback WebSocket client id to dispatch paused items to for interactive resolution. Must be a connected callback client.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherResponse
            matcher registered successfully

        Examples
        --------
        import asyncio

        from fern.control import PutMockserverBreakpointMatcherRequestPhasesItem

        from fern import AsyncFernApi, HttpRequest

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.register_a_breakpoint_matcher(
                http_request=HttpRequest(
                    method="GET",
                    path="/api/test",
                ),
                phases=[PutMockserverBreakpointMatcherRequestPhasesItem.REQUEST],
                client_id="test-client-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_breakpoint_matcher(
            http_request=http_request, phases=phases, client_id=client_id, request_options=request_options
        )
        return _response.data

    async def list_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverBreakpointMatchersResponse:
        """
        Returns all currently registered breakpoint matchers. Each entry includes the matcher id, the httpRequest definition, the set of phases, and the clientId.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverBreakpointMatchersResponse
            list of registered matchers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.list_all_registered_breakpoint_matchers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registered_breakpoint_matchers(request_options=request_options)
        return _response.data

    async def list_all_registered_breakpoint_matchers_put_variant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatchersResponse:
        """
        Same as GET /mockserver/breakpoint/matchers. The PUT variant exists for consistency with other control-plane endpoints that use PUT for idempotent queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatchersResponse
            list of registered matchers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.list_all_registered_breakpoint_matchers_put_variant()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registered_breakpoint_matchers_put_variant(
            request_options=request_options
        )
        return _response.data

    async def remove_a_registered_breakpoint_matcher(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatcherRemoveResponse:
        """
        Removes a previously registered breakpoint matcher by id. Returns status "removed" on success or 404 if no matcher with the given id exists.

        Parameters
        ----------
        id : str
            the matcher id to remove

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherRemoveResponse
            matcher removed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.remove_a_registered_breakpoint_matcher(
                id="78fa44ff-5989-467a-ba44-ff5989667a71",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_registered_breakpoint_matcher(
            id=id, request_options=request_options
        )
        return _response.data

    async def remove_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverBreakpointMatcherClearResponse:
        """
        Removes all registered breakpoint matchers. After this call, no exchanges will be paused at breakpoints until new matchers are registered. Returns the number of matchers cleared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverBreakpointMatcherClearResponse
            all matchers cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.remove_all_registered_breakpoint_matchers()


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_all_registered_breakpoint_matchers(request_options=request_options)
        return _response.data

    async def stop_running_process(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        only supported on Netty version

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.stop_running_process()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_running_process(request_options=request_options)
        return _response.data

    async def readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverReadyResponse:
        """
        Readiness probe, distinct from the liveness/status endpoints, which answer 200 the instant the port binds. Stays 503 until the synchronous expectation initializers and any OpenAPI seeding have completed, so an orchestrator does not route traffic before the seeded expectations exist. This is the one control-plane endpoint with no authentication gate, so it remains usable as a Kubernetes readiness probe on an instance whose control plane requires credentials.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverReadyResponse
            initialization complete, ready to serve

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.readiness_probe()


        asyncio.run(main())
        """
        _response = await self._raw_client.readiness_probe(request_options=request_options)
        return _response.data

    async def retrieve_the_effective_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns every configuration property with its resolved value and the source tier that supplied it, so an operator can see which of the property file, system properties, environment variables or defaults won. Values detected as sensitive are redacted. Distinct from `/mockserver/configuration`, which reads and writes the mutable runtime configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            effective configuration returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_the_effective_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_effective_configuration(request_options=request_options)
        return _response.data

    async def retrieve_client_proxy_setup_details(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverProxyConfigurationResponse:
        """
        Returns everything a client needs to route through this instance as a proxy: the CA certificate (path and PEM), the proxy URL, and ready-to-paste environment-variable snippets for Unix shells and PowerShell. Send `Accept: text/plain` to get the copy-paste snippet on its own instead of the JSON document.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverProxyConfigurationResponse
            proxy configuration returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_client_proxy_setup_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_client_proxy_setup_details(request_options=request_options)
        return _response.data

    async def retrieve_experimental_http3quic_listener_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverHttp3StatusResponse:
        """
        Reports whether the experimental HTTP/3 listener is enabled, the UDP port it is bound to, and how many QUIC connections are currently active. When the running server is not an HTTP/3-capable instance, `enabled` is false and `port` is -1.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverHttp3StatusResponse
            HTTP/3 status returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.control.retrieve_experimental_http3quic_listener_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_experimental_http3quic_listener_status(
            request_options=request_options
        )
        return _response.data
