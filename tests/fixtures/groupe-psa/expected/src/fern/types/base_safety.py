

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .base_safety_auto_e_call_triggering import BaseSafetyAutoECallTriggering
from .belt_status import BeltStatus


class BaseSafety(UniversalBaseModel):
    belt_status: typing_extensions.Annotated[
        typing.Optional[typing.List[BeltStatus]], FieldMetadata(alias="beltStatus"), pydantic.Field(alias="beltStatus")
    ] = None
    auto_e_call_triggering: typing_extensions.Annotated[
        typing.Optional[BaseSafetyAutoECallTriggering],
        FieldMetadata(alias="autoECallTriggering"),
        pydantic.Field(alias="autoECallTriggering"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
