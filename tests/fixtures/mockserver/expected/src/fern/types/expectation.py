

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .after_action import AfterAction
from .binary_response import BinaryResponse
from .capture_rule import CaptureRule
from .dns_response import DnsResponse
from .expectation_cross_protocol_scenarios_item import ExpectationCrossProtocolScenariosItem
from .expectation_response_mode import ExpectationResponseMode
from .expectation_step import ExpectationStep
from .grpc_bidi_response import GrpcBidiResponse
from .grpc_stream_response import GrpcStreamResponse
from .http_chaos_profile import HttpChaosProfile
from .http_class_callback import HttpClassCallback
from .http_error import HttpError
from .http_forward import HttpForward
from .http_forward_validate_action import HttpForwardValidateAction
from .http_forward_with_fallback import HttpForwardWithFallback
from .http_llm_response import HttpLlmResponse
from .http_object_callback import HttpObjectCallback
from .http_override_forwarded_request import HttpOverrideForwardedRequest
from .http_sse_response import HttpSseResponse
from .http_template import HttpTemplate
from .http_web_socket_response import HttpWebSocketResponse
from .rate_limit import RateLimit
from .time_to_live import TimeToLive
from .times import Times


class Expectation(UniversalBaseModel):
    """
    expectation
    """

    id: typing.Optional[str] = None
    priority: typing.Optional[int] = None
    rate_limit: typing_extensions.Annotated[
        typing.Optional[RateLimit], FieldMetadata(alias="rateLimit"), pydantic.Field(alias="rateLimit")
    ] = None
    http_request: typing_extensions.Annotated[
        typing.Optional["RequestDefinition"], FieldMetadata(alias="httpRequest"), pydantic.Field(alias="httpRequest")
    ] = None
    http_response: typing_extensions.Annotated[
        typing.Optional["HttpResponse"], FieldMetadata(alias="httpResponse"), pydantic.Field(alias="httpResponse")
    ] = None
    http_response_template: typing_extensions.Annotated[
        typing.Optional[HttpTemplate],
        FieldMetadata(alias="httpResponseTemplate"),
        pydantic.Field(alias="httpResponseTemplate"),
    ] = None
    http_response_class_callback: typing_extensions.Annotated[
        typing.Optional[HttpClassCallback],
        FieldMetadata(alias="httpResponseClassCallback"),
        pydantic.Field(alias="httpResponseClassCallback"),
    ] = None
    http_response_object_callback: typing_extensions.Annotated[
        typing.Optional[HttpObjectCallback],
        FieldMetadata(alias="httpResponseObjectCallback"),
        pydantic.Field(alias="httpResponseObjectCallback"),
    ] = None
    http_forward: typing_extensions.Annotated[
        typing.Optional[HttpForward], FieldMetadata(alias="httpForward"), pydantic.Field(alias="httpForward")
    ] = None
    http_forward_template: typing_extensions.Annotated[
        typing.Optional[HttpTemplate],
        FieldMetadata(alias="httpForwardTemplate"),
        pydantic.Field(alias="httpForwardTemplate"),
    ] = None
    http_forward_class_callback: typing_extensions.Annotated[
        typing.Optional[HttpClassCallback],
        FieldMetadata(alias="httpForwardClassCallback"),
        pydantic.Field(alias="httpForwardClassCallback"),
    ] = None
    http_forward_object_callback: typing_extensions.Annotated[
        typing.Optional[HttpObjectCallback],
        FieldMetadata(alias="httpForwardObjectCallback"),
        pydantic.Field(alias="httpForwardObjectCallback"),
    ] = None
    http_override_forwarded_request: typing_extensions.Annotated[
        typing.Optional[HttpOverrideForwardedRequest],
        FieldMetadata(alias="httpOverrideForwardedRequest"),
        pydantic.Field(alias="httpOverrideForwardedRequest"),
    ] = None
    http_error: typing_extensions.Annotated[
        typing.Optional[HttpError], FieldMetadata(alias="httpError"), pydantic.Field(alias="httpError")
    ] = None
    times: typing.Optional[Times] = None
    time_to_live: typing_extensions.Annotated[
        typing.Optional[TimeToLive], FieldMetadata(alias="timeToLive"), pydantic.Field(alias="timeToLive")
    ] = None
    percentage: typing.Optional[int] = None
    chaos: typing.Optional[HttpChaosProfile] = None
    http_sse_response: typing_extensions.Annotated[
        typing.Optional[HttpSseResponse],
        FieldMetadata(alias="httpSseResponse"),
        pydantic.Field(alias="httpSseResponse"),
    ] = None
    http_web_socket_response: typing_extensions.Annotated[
        typing.Optional[HttpWebSocketResponse],
        FieldMetadata(alias="httpWebSocketResponse"),
        pydantic.Field(alias="httpWebSocketResponse"),
    ] = None
    http_llm_response: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponse],
        FieldMetadata(alias="httpLlmResponse"),
        pydantic.Field(alias="httpLlmResponse"),
    ] = None
    grpc_stream_response: typing_extensions.Annotated[
        typing.Optional[GrpcStreamResponse],
        FieldMetadata(alias="grpcStreamResponse"),
        pydantic.Field(alias="grpcStreamResponse"),
    ] = None
    grpc_bidi_response: typing_extensions.Annotated[
        typing.Optional[GrpcBidiResponse],
        FieldMetadata(alias="grpcBidiResponse"),
        pydantic.Field(alias="grpcBidiResponse"),
    ] = None
    binary_response: typing_extensions.Annotated[
        typing.Optional[BinaryResponse], FieldMetadata(alias="binaryResponse"), pydantic.Field(alias="binaryResponse")
    ] = None
    dns_response: typing_extensions.Annotated[
        typing.Optional[DnsResponse], FieldMetadata(alias="dnsResponse"), pydantic.Field(alias="dnsResponse")
    ] = None
    http_forward_validate_action: typing_extensions.Annotated[
        typing.Optional[HttpForwardValidateAction],
        FieldMetadata(alias="httpForwardValidateAction"),
        pydantic.Field(alias="httpForwardValidateAction"),
    ] = None
    http_forward_with_fallback: typing_extensions.Annotated[
        typing.Optional[HttpForwardWithFallback],
        FieldMetadata(alias="httpForwardWithFallback"),
        pydantic.Field(alias="httpForwardWithFallback"),
    ] = None
    before_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[AfterAction]],
        FieldMetadata(alias="beforeActions"),
        pydantic.Field(alias="beforeActions", description="actions run before the expectation's own action"),
    ] = None
    """
    actions run before the expectation's own action
    """

    after_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[AfterAction]],
        FieldMetadata(alias="afterActions"),
        pydantic.Field(alias="afterActions", description="actions run after the expectation's own action"),
    ] = None
    """
    actions run after the expectation's own action
    """

    steps: typing.Optional[typing.List[ExpectationStep]] = pydantic.Field(default=None)
    """
    ordered steps for a multi-step expectation
    """

    capture: typing.Optional[typing.List[CaptureRule]] = pydantic.Field(default=None)
    """
    rules extracting values from the matched request into scenario state
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional namespace (tenant) this expectation belongs to; when set, the expectation only matches requests carrying the configured matchNamespaceHeader with this value, isolated from other namespaces
    """

    scenario_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scenarioName"), pydantic.Field(alias="scenarioName")
    ] = None
    scenario_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scenarioState"), pydantic.Field(alias="scenarioState")
    ] = None
    new_scenario_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newScenarioState"), pydantic.Field(alias="newScenarioState")
    ] = None
    http_responses: typing_extensions.Annotated[
        typing.Optional[typing.List["HttpResponse"]],
        FieldMetadata(alias="httpResponses"),
        pydantic.Field(alias="httpResponses"),
    ] = None
    response_mode: typing_extensions.Annotated[
        typing.Optional[ExpectationResponseMode],
        FieldMetadata(alias="responseMode"),
        pydantic.Field(alias="responseMode"),
    ] = None
    response_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="responseWeights"),
        pydantic.Field(alias="responseWeights"),
    ] = None
    switch_after: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="switchAfter"), pydantic.Field(alias="switchAfter")
    ] = None
    cross_protocol_scenarios: typing_extensions.Annotated[
        typing.Optional[typing.List[ExpectationCrossProtocolScenariosItem]],
        FieldMetadata(alias="crossProtocolScenarios"),
        pydantic.Field(alias="crossProtocolScenarios"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conditional_request_definition import ConditionalRequestDefinition
from .request_definition import RequestDefinition
from .http_response import HttpResponse
from .recover_after import RecoverAfter

update_forward_refs(
    Expectation,
    ConditionalRequestDefinition=ConditionalRequestDefinition,
    HttpResponse=HttpResponse,
    RecoverAfter=RecoverAfter,
    RequestDefinition=RequestDefinition,
)
