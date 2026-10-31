

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RoomCorrGetResponseEqBandItem(UniversalBaseModel):
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the EQ band.
    """

    param_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the parameter for this band (e.g., "a_mode", "a_freq", "a_q", "a_gain").
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    The value of the parameter for this band.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
