

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .v1update_jit_access_config_response_unavailable_reason_state import (
    V1UpdateJitAccessConfigResponseUnavailableReasonState,
)
from .v1update_jit_access_config_response_unavailable_reason_unavailable_reason import (
    V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason,
)


class V1UpdateJitAccessConfigResponseUnavailableReason(UniversalBaseModel):
    state: V1UpdateJitAccessConfigResponseUnavailableReasonState
    unavailable_reason: typing_extensions.Annotated[
        V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason,
        FieldMetadata(alias="unavailableReason"),
        pydantic.Field(alias="unavailableReason"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
