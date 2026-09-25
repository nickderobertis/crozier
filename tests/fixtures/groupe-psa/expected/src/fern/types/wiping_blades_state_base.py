

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wiping_blades_state_base_speed import WipingBladesStateBaseSpeed


class WipingBladesStateBase(UniversalBaseModel):
    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Either active (true) or not (false).
    """

    speed: typing.Optional[WipingBladesStateBaseSpeed] = pydantic.Field(default=None)
    """
    Wiping speed. This field is present only if active field is set to true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
