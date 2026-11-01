

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .handover_any_of_const_mode import HandoverAnyOfConstMode
from .handover_any_of_const_slots_value import HandoverAnyOfConstSlotsValue


class HandoverAnyOfConst(UniversalBaseModel):
    mode: typing.Optional[HandoverAnyOfConstMode] = None
    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Collection region, chosen at pickup.
    """

    slots: typing.Optional[typing.Dict[str, HandoverAnyOfConstSlotsValue]] = None
    courier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
