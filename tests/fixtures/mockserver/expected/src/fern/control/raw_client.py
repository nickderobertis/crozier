

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse
from ..core.http_response import HttpResponse as core_http_response_HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_acceptable_error import NotAcceptableError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.bad_gateway_error_body import BadGatewayErrorBody
from ..types.body import Body
from ..types.clock_response import ClockResponse
from ..types.clock_status import ClockStatus
from ..types.content_too_large_error_body import ContentTooLargeErrorBody
from ..types.http_request import HttpRequest
from ..types.http_response import HttpResponse as types_http_response_HttpResponse
from ..types.jwt import Jwt
from ..types.key_to_multi_value import KeyToMultiValue
from ..types.key_to_value import KeyToValue
from ..types.ports import Ports
from ..types.protocol import Protocol
from ..types.socket_address import SocketAddress
from ..types.string_or_json_schema import StringOrJsonSchema
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def clears_expectations_and_recorded_requests_that_match_the_request_matcher(
        self,
        *,
        request: PutMockserverClearRequestBody,
        type: typing.Optional[PutMockserverClearRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[None]:
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
        core_http_response_HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/clear",
            method="PUT",
            params={
                "type": type,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutMockserverClearRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return core_http_response_HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def clears_all_expectations_and_recorded_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/reset",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return core_http_response_HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> core_http_response_HttpResponse[PutMockserverRetrieveResponse]:
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
        core_http_response_HttpResponse[PutMockserverRetrieveResponse]
            recorded requests or active expectations returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/retrieve",
            method="PUT",
            params={
                "format": format,
                "type": type,
                "correlationId": correlation_id,
                "namespace": namespace,
                "fanInLocalOnly": fan_in_local_only,
                "forwardUnmatchedTo": forward_unmatched_to,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutMockserverRetrieveRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverRetrieveResponse,
                    parse_obj_as(
                        type_=PutMockserverRetrieveResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def return_listening_ports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[Ports]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[Ports]
            MockServer is running and listening on the listed ports
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/status",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ports,
                    parse_obj_as(
                        type_=Ports,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bind_additional_listening_ports(
        self,
        *,
        ports: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[Ports]:
        """
        only supported on Netty version

        Parameters
        ----------
        ports : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[Ports]
            listening on additional requested ports, note: the response ony contains ports added for the request, to list all ports use /status
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/bind",
            method="PUT",
            json={
                "ports": ports,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ports,
                    parse_obj_as(
                        type_=Ports,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    def retrieve_the_open_api_specification_for_mock_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[None]:
        """
        returns the OpenAPI specification describing the MockServer REST API in YAML format

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/openapi.yaml",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return core_http_response_HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_the_current_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns the current MockServer configuration as JSON

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[typing.Dict[str, typing.Any]]
            current configuration returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_the_current_configuration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[typing.Dict[str, typing.Any]]:
        """
        updates MockServer configuration properties at runtime, only non-null fields in the request body are applied

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[typing.Dict[str, typing.Any]]
            configuration updated successfully, returns the full updated configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/configuration",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_the_current_server_clock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[ClockStatus]:
        """
        Returns the current instant, epoch milliseconds, and whether the clock is frozen.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[ClockStatus]
            current clock status returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/clock",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClockStatus,
                    parse_obj_as(
                        type_=ClockStatus,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def control_the_server_clock_for_deterministic_time_based_testing(
        self,
        *,
        action: ClockRequestAction,
        instant: typing.Optional[dt.datetime] = OMIT,
        duration_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[ClockResponse]:
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
        core_http_response_HttpResponse[ClockResponse]
            clock action applied successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/clock",
            method="PUT",
            json={
                "action": action,
                "instant": instant,
                "durationMillis": duration_millis,
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
                    ClockResponse,
                    parse_obj_as(
                        type_=ClockResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_the_current_proxy_mock_operating_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverModeResponse]:
        """
        returns the current operating mode and whether unmatched requests are proxied

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverModeResponse]
            current mode returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/mode",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverModeResponse,
                    parse_obj_as(
                        type_=GetMockserverModeResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_the_proxy_mock_operating_mode(
        self, *, mode: PutMockserverModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[PutMockserverModeResponse]:
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
        core_http_response_HttpResponse[PutMockserverModeResponse]
            mode set successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/mode",
            method="PUT",
            params={
                "mode": mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverModeResponse,
                    parse_obj_as(
                        type_=PutMockserverModeResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_registered_cassettes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverCassettesResponse]:
        """
        returns all registered cassettes held in the in-memory cassette registry

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverCassettesResponse]
            registered cassettes returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverCassettesResponse,
                    parse_obj_as(
                        type_=GetMockserverCassettesResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_or_update_a_record_replay_cassette(
        self,
        *,
        path: str,
        filename: typing.Optional[str] = OMIT,
        expectation_count: typing.Optional[int] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[PutMockserverCassettesResponse]:
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
        core_http_response_HttpResponse[PutMockserverCassettesResponse]
            cassette registered
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="PUT",
            json={
                "path": path,
                "filename": filename,
                "expectationCount": expectation_count,
                "origin": origin,
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
                    PutMockserverCassettesResponse,
                    parse_obj_as(
                        type_=PutMockserverCassettesResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_a_registered_cassette(
        self,
        *,
        path: typing.Optional[str] = None,
        delete_mockserver_cassettes_request_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[DeleteMockserverCassettesResponse]:
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
        core_http_response_HttpResponse[DeleteMockserverCassettesResponse]
            removal processed
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="DELETE",
            params={
                "path": path,
            },
            json={
                "path": delete_mockserver_cassettes_request_path,
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
                    DeleteMockserverCassettesResponse,
                    parse_obj_as(
                        type_=DeleteMockserverCassettesResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> core_http_response_HttpResponse[types_http_response_HttpResponse]:
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
        core_http_response_HttpResponse[types_http_response_HttpResponse]
            upstream response returned successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/replay",
            method="PUT",
            json={
                "secure": secure,
                "keepAlive": keep_alive,
                "method": convert_and_respect_annotation_metadata(
                    object_=method, annotation=StringOrJsonSchema, direction="write"
                ),
                "path": convert_and_respect_annotation_metadata(
                    object_=path, annotation=StringOrJsonSchema, direction="write"
                ),
                "pathParameters": convert_and_respect_annotation_metadata(
                    object_=path_parameters, annotation=KeyToMultiValue, direction="write"
                ),
                "queryStringParameters": convert_and_respect_annotation_metadata(
                    object_=query_string_parameters, annotation=KeyToMultiValue, direction="write"
                ),
                "body": convert_and_respect_annotation_metadata(object_=body, annotation=Body, direction="write"),
                "headers": convert_and_respect_annotation_metadata(
                    object_=headers, annotation=KeyToMultiValue, direction="write"
                ),
                "cookies": convert_and_respect_annotation_metadata(
                    object_=cookies, annotation=KeyToValue, direction="write"
                ),
                "socketAddress": convert_and_respect_annotation_metadata(
                    object_=socket_address, annotation=SocketAddress, direction="write"
                ),
                "protocol": protocol,
                "jwt": convert_and_respect_annotation_metadata(object_=jwt, annotation=Jwt, direction="write"),
                "not": not_,
                "respondBeforeBody": respond_before_body,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    types_http_response_HttpResponse,
                    parse_obj_as(
                        type_=types_http_response_HttpResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContentTooLargeErrorBody,
                        parse_obj_as(
                            type_=ContentTooLargeErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    def register_a_breakpoint_matcher(
        self,
        *,
        http_request: HttpRequest,
        phases: typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem],
        client_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> core_http_response_HttpResponse[PutMockserverBreakpointMatcherResponse]:
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
        core_http_response_HttpResponse[PutMockserverBreakpointMatcherResponse]
            matcher registered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher",
            method="PUT",
            json={
                "httpRequest": convert_and_respect_annotation_metadata(
                    object_=http_request, annotation=HttpRequest, direction="write"
                ),
                "phases": phases,
                "clientId": client_id,
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
                    PutMockserverBreakpointMatcherResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverBreakpointMatchersResponse]:
        """
        Returns all currently registered breakpoint matchers. Each entry includes the matcher id, the httpRequest definition, the set of phases, and the clientId.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverBreakpointMatchersResponse]
            list of registered matchers
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matchers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverBreakpointMatchersResponse,
                    parse_obj_as(
                        type_=GetMockserverBreakpointMatchersResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_registered_breakpoint_matchers_put_variant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[PutMockserverBreakpointMatchersResponse]:
        """
        Same as GET /mockserver/breakpoint/matchers. The PUT variant exists for consistency with other control-plane endpoints that use PUT for idempotent queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[PutMockserverBreakpointMatchersResponse]
            list of registered matchers
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matchers",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverBreakpointMatchersResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatchersResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_a_registered_breakpoint_matcher(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[PutMockserverBreakpointMatcherRemoveResponse]:
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
        core_http_response_HttpResponse[PutMockserverBreakpointMatcherRemoveResponse]
            matcher removed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher/remove",
            method="PUT",
            json={
                "id": id,
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
                    PutMockserverBreakpointMatcherRemoveResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherRemoveResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[PutMockserverBreakpointMatcherClearResponse]:
        """
        Removes all registered breakpoint matchers. After this call, no exchanges will be paused at breakpoints until new matchers are registered. Returns the number of matchers cleared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[PutMockserverBreakpointMatcherClearResponse]
            all matchers cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher/clear",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverBreakpointMatcherClearResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherClearResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def stop_running_process(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[None]:
        """
        only supported on Netty version

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/stop",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return core_http_response_HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverReadyResponse]:
        """
        Readiness probe, distinct from the liveness/status endpoints, which answer 200 the instant the port binds. Stays 503 until the synchronous expectation initializers and any OpenAPI seeding have completed, so an orchestrator does not route traffic before the seeded expectations exist. This is the one control-plane endpoint with no authentication gate, so it remains usable as a Kubernetes readiness probe on an instance whose control plane requires credentials.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverReadyResponse]
            initialization complete, ready to serve
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/ready",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverReadyResponse,
                    parse_obj_as(
                        type_=GetMockserverReadyResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def retrieve_the_effective_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns every configuration property with its resolved value and the source tier that supplied it, so an operator can see which of the property file, system properties, environment variables or defaults won. Values detected as sensitive are redacted. Distinct from `/mockserver/configuration`, which reads and writes the mutable runtime configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[typing.Dict[str, typing.Any]]
            effective configuration returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_client_proxy_setup_details(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverProxyConfigurationResponse]:
        """
        Returns everything a client needs to route through this instance as a proxy: the CA certificate (path and PEM), the proxy URL, and ready-to-paste environment-variable snippets for Unix shells and PowerShell. Send `Accept: text/plain` to get the copy-paste snippet on its own instead of the JSON document.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverProxyConfigurationResponse]
            proxy configuration returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/proxyConfiguration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverProxyConfigurationResponse,
                    parse_obj_as(
                        type_=GetMockserverProxyConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_experimental_http3quic_listener_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> core_http_response_HttpResponse[GetMockserverHttp3StatusResponse]:
        """
        Reports whether the experimental HTTP/3 listener is enabled, the UDP port it is bound to, and how many QUIC connections are currently active. When the running server is not an HTTP/3-capable instance, `enabled` is false and `port` is -1.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        core_http_response_HttpResponse[GetMockserverHttp3StatusResponse]
            HTTP/3 status returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/http3status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverHttp3StatusResponse,
                    parse_obj_as(
                        type_=GetMockserverHttp3StatusResponse,
                        object_=_response.json(),
                    ),
                )
                return core_http_response_HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def clears_expectations_and_recorded_requests_that_match_the_request_matcher(
        self,
        *,
        request: PutMockserverClearRequestBody,
        type: typing.Optional[PutMockserverClearRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/clear",
            method="PUT",
            params={
                "type": type,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutMockserverClearRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def clears_all_expectations_and_recorded_requests(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/reset",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PutMockserverRetrieveResponse]:
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
        AsyncHttpResponse[PutMockserverRetrieveResponse]
            recorded requests or active expectations returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/retrieve",
            method="PUT",
            params={
                "format": format,
                "type": type,
                "correlationId": correlation_id,
                "namespace": namespace,
                "fanInLocalOnly": fan_in_local_only,
                "forwardUnmatchedTo": forward_unmatched_to,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutMockserverRetrieveRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverRetrieveResponse,
                    parse_obj_as(
                        type_=PutMockserverRetrieveResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def return_listening_ports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ports]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ports]
            MockServer is running and listening on the listed ports
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/status",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ports,
                    parse_obj_as(
                        type_=Ports,
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

    async def bind_additional_listening_ports(
        self,
        *,
        ports: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ports]:
        """
        only supported on Netty version

        Parameters
        ----------
        ports : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ports]
            listening on additional requested ports, note: the response ony contains ports added for the request, to list all ports use /status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/bind",
            method="PUT",
            json={
                "ports": ports,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ports,
                    parse_obj_as(
                        type_=Ports,
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    async def retrieve_the_open_api_specification_for_mock_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        returns the OpenAPI specification describing the MockServer REST API in YAML format

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/openapi.yaml",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_the_current_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns the current MockServer configuration as JSON

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            current configuration returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def update_the_current_configuration(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        updates MockServer configuration properties at runtime, only non-null fields in the request body are applied

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            configuration updated successfully, returns the full updated configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/configuration",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_the_current_server_clock_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClockStatus]:
        """
        Returns the current instant, epoch milliseconds, and whether the clock is frozen.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClockStatus]
            current clock status returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/clock",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClockStatus,
                    parse_obj_as(
                        type_=ClockStatus,
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

    async def control_the_server_clock_for_deterministic_time_based_testing(
        self,
        *,
        action: ClockRequestAction,
        instant: typing.Optional[dt.datetime] = OMIT,
        duration_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClockResponse]:
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
        AsyncHttpResponse[ClockResponse]
            clock action applied successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/clock",
            method="PUT",
            json={
                "action": action,
                "instant": instant,
                "durationMillis": duration_millis,
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
                    ClockResponse,
                    parse_obj_as(
                        type_=ClockResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_the_current_proxy_mock_operating_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverModeResponse]:
        """
        returns the current operating mode and whether unmatched requests are proxied

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverModeResponse]
            current mode returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/mode",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverModeResponse,
                    parse_obj_as(
                        type_=GetMockserverModeResponse,
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

    async def set_the_proxy_mock_operating_mode(
        self, *, mode: PutMockserverModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverModeResponse]:
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
        AsyncHttpResponse[PutMockserverModeResponse]
            mode set successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/mode",
            method="PUT",
            params={
                "mode": mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverModeResponse,
                    parse_obj_as(
                        type_=PutMockserverModeResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_registered_cassettes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverCassettesResponse]:
        """
        returns all registered cassettes held in the in-memory cassette registry

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverCassettesResponse]
            registered cassettes returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverCassettesResponse,
                    parse_obj_as(
                        type_=GetMockserverCassettesResponse,
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

    async def register_or_update_a_record_replay_cassette(
        self,
        *,
        path: str,
        filename: typing.Optional[str] = OMIT,
        expectation_count: typing.Optional[int] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverCassettesResponse]:
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
        AsyncHttpResponse[PutMockserverCassettesResponse]
            cassette registered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="PUT",
            json={
                "path": path,
                "filename": filename,
                "expectationCount": expectation_count,
                "origin": origin,
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
                    PutMockserverCassettesResponse,
                    parse_obj_as(
                        type_=PutMockserverCassettesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_a_registered_cassette(
        self,
        *,
        path: typing.Optional[str] = None,
        delete_mockserver_cassettes_request_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteMockserverCassettesResponse]:
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
        AsyncHttpResponse[DeleteMockserverCassettesResponse]
            removal processed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/cassettes",
            method="DELETE",
            params={
                "path": path,
            },
            json={
                "path": delete_mockserver_cassettes_request_path,
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
                    DeleteMockserverCassettesResponse,
                    parse_obj_as(
                        type_=DeleteMockserverCassettesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[types_http_response_HttpResponse]:
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
        AsyncHttpResponse[types_http_response_HttpResponse]
            upstream response returned successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/replay",
            method="PUT",
            json={
                "secure": secure,
                "keepAlive": keep_alive,
                "method": convert_and_respect_annotation_metadata(
                    object_=method, annotation=StringOrJsonSchema, direction="write"
                ),
                "path": convert_and_respect_annotation_metadata(
                    object_=path, annotation=StringOrJsonSchema, direction="write"
                ),
                "pathParameters": convert_and_respect_annotation_metadata(
                    object_=path_parameters, annotation=KeyToMultiValue, direction="write"
                ),
                "queryStringParameters": convert_and_respect_annotation_metadata(
                    object_=query_string_parameters, annotation=KeyToMultiValue, direction="write"
                ),
                "body": convert_and_respect_annotation_metadata(object_=body, annotation=Body, direction="write"),
                "headers": convert_and_respect_annotation_metadata(
                    object_=headers, annotation=KeyToMultiValue, direction="write"
                ),
                "cookies": convert_and_respect_annotation_metadata(
                    object_=cookies, annotation=KeyToValue, direction="write"
                ),
                "socketAddress": convert_and_respect_annotation_metadata(
                    object_=socket_address, annotation=SocketAddress, direction="write"
                ),
                "protocol": protocol,
                "jwt": convert_and_respect_annotation_metadata(object_=jwt, annotation=Jwt, direction="write"),
                "not": not_,
                "respondBeforeBody": respond_before_body,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    types_http_response_HttpResponse,
                    parse_obj_as(
                        type_=types_http_response_HttpResponse,
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContentTooLargeErrorBody,
                        parse_obj_as(
                            type_=ContentTooLargeErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    async def register_a_breakpoint_matcher(
        self,
        *,
        http_request: HttpRequest,
        phases: typing.Sequence[PutMockserverBreakpointMatcherRequestPhasesItem],
        client_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverBreakpointMatcherResponse]:
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
        AsyncHttpResponse[PutMockserverBreakpointMatcherResponse]
            matcher registered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher",
            method="PUT",
            json={
                "httpRequest": convert_and_respect_annotation_metadata(
                    object_=http_request, annotation=HttpRequest, direction="write"
                ),
                "phases": phases,
                "clientId": client_id,
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
                    PutMockserverBreakpointMatcherResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverBreakpointMatchersResponse]:
        """
        Returns all currently registered breakpoint matchers. Each entry includes the matcher id, the httpRequest definition, the set of phases, and the clientId.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverBreakpointMatchersResponse]
            list of registered matchers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matchers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverBreakpointMatchersResponse,
                    parse_obj_as(
                        type_=GetMockserverBreakpointMatchersResponse,
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

    async def list_all_registered_breakpoint_matchers_put_variant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverBreakpointMatchersResponse]:
        """
        Same as GET /mockserver/breakpoint/matchers. The PUT variant exists for consistency with other control-plane endpoints that use PUT for idempotent queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverBreakpointMatchersResponse]
            list of registered matchers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matchers",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverBreakpointMatchersResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatchersResponse,
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

    async def remove_a_registered_breakpoint_matcher(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverBreakpointMatcherRemoveResponse]:
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
        AsyncHttpResponse[PutMockserverBreakpointMatcherRemoveResponse]
            matcher removed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher/remove",
            method="PUT",
            json={
                "id": id,
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
                    PutMockserverBreakpointMatcherRemoveResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherRemoveResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_all_registered_breakpoint_matchers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverBreakpointMatcherClearResponse]:
        """
        Removes all registered breakpoint matchers. After this call, no exchanges will be paused at breakpoints until new matchers are registered. Returns the number of matchers cleared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverBreakpointMatcherClearResponse]
            all matchers cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/breakpoint/matcher/clear",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverBreakpointMatcherClearResponse,
                    parse_obj_as(
                        type_=PutMockserverBreakpointMatcherClearResponse,
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

    async def stop_running_process(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        only supported on Netty version

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/stop",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverReadyResponse]:
        """
        Readiness probe, distinct from the liveness/status endpoints, which answer 200 the instant the port binds. Stays 503 until the synchronous expectation initializers and any OpenAPI seeding have completed, so an orchestrator does not route traffic before the seeded expectations exist. This is the one control-plane endpoint with no authentication gate, so it remains usable as a Kubernetes readiness probe on an instance whose control plane requires credentials.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverReadyResponse]
            initialization complete, ready to serve
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/ready",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverReadyResponse,
                    parse_obj_as(
                        type_=GetMockserverReadyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def retrieve_the_effective_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns every configuration property with its resolved value and the source tier that supplied it, so an operator can see which of the property file, system properties, environment variables or defaults won. Values detected as sensitive are redacted. Distinct from `/mockserver/configuration`, which reads and writes the mutable runtime configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            effective configuration returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def retrieve_client_proxy_setup_details(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverProxyConfigurationResponse]:
        """
        Returns everything a client needs to route through this instance as a proxy: the CA certificate (path and PEM), the proxy URL, and ready-to-paste environment-variable snippets for Unix shells and PowerShell. Send `Accept: text/plain` to get the copy-paste snippet on its own instead of the JSON document.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverProxyConfigurationResponse]
            proxy configuration returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/proxyConfiguration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverProxyConfigurationResponse,
                    parse_obj_as(
                        type_=GetMockserverProxyConfigurationResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_experimental_http3quic_listener_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverHttp3StatusResponse]:
        """
        Reports whether the experimental HTTP/3 listener is enabled, the UDP port it is bound to, and how many QUIC connections are currently active. When the running server is not an HTTP/3-capable instance, `enabled` is false and `port` is -1.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverHttp3StatusResponse]
            HTTP/3 status returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/http3status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverHttp3StatusResponse,
                    parse_obj_as(
                        type_=GetMockserverHttp3StatusResponse,
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
