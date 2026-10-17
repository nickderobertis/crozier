

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .v1update_jit_access_config_response_applied_successfully_state import (
    V1UpdateJitAccessConfigResponseAppliedSuccessfullyState,
)


class V1UpdateJitAccessConfigResponseAppliedSuccessfully(UniversalBaseModel):
    state: V1UpdateJitAccessConfigResponseAppliedSuccessfullyState
    applied_successfully: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="appliedSuccessfully"), pydantic.Field(alias="appliedSuccessfully")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
