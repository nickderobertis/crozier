

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bad_responses_fault_config import BadResponsesFaultConfig
from .large_request_fault_config import LargeRequestFaultConfig
from .large_response_fault_config import LargeResponseFaultConfig
from .latency_injection_fault_config import LatencyInjectionFaultConfig


class ChaosConfig(UniversalBaseModel):
    """
    Configuration for the faults that can be injected in requests
    """

    bad_responses_fault_config: typing_extensions.Annotated[
        typing.Optional[BadResponsesFaultConfig], FieldMetadata(alias="badResponsesFaultConfig")
    ] = None
    enabled: bool = pydantic.Field()
    """
    Whether or not this config is enabled
    """

    large_request_fault_config: typing_extensions.Annotated[
        typing.Optional[LargeRequestFaultConfig], FieldMetadata(alias="largeRequestFaultConfig")
    ] = None
    large_response_fault_config: typing_extensions.Annotated[
        typing.Optional[LargeResponseFaultConfig], FieldMetadata(alias="largeResponseFaultConfig")
    ] = None
    latency_injection_fault_config: typing_extensions.Annotated[
        typing.Optional[LatencyInjectionFaultConfig], FieldMetadata(alias="latencyInjectionFaultConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
