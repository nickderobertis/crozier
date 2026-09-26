

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoadElectricEnergy(UniversalBaseModel):
    capacity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Electric battery total capacity (expressed in Wh).
    """

    residual: typing.Optional[int] = pydantic.Field(default=None)
    """
    Residual electric energy (expressed in Wh)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
