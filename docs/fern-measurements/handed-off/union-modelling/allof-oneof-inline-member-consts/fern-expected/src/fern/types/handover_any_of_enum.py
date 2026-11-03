

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .handover_any_of_enum_mode import HandoverAnyOfEnumMode
from .handover_any_of_enum_slots_value import HandoverAnyOfEnumSlotsValue


class HandoverAnyOfEnum(UniversalBaseModel):
    mode: typing.Optional[HandoverAnyOfEnumMode] = None
    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Collection region, chosen at pickup.
    """

    slots: typing.Optional[typing.Dict[str, HandoverAnyOfEnumSlotsValue]] = None
    courier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
