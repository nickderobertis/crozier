

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NsiMissionCriticalSupport(UniversalBaseModel):
    """
    Mission-critical (MC) leads to a priority of the network slice relative to others, for C-plane and U-plane decisions.
    """

    availability: typing.Optional[bool] = None
    mc_service: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    This attribute specifies whether or not the network slice supports MC push-to-talk, MC data, MC video, Isolated E-UTRAN Operation for Public Safety or MC interworking.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
