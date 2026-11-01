

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .handover_one_of_const_mode import HandoverOneOfConstMode
from .handover_one_of_const_slots_value import HandoverOneOfConstSlotsValue


class HandoverOneOfConst(UniversalBaseModel):
    mode: typing.Optional[HandoverOneOfConstMode] = None
    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Collection region, chosen at pickup.
    """

    slots: typing.Optional[typing.Dict[str, HandoverOneOfConstSlotsValue]] = None
    courier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
