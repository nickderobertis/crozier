

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .axis_scale import AxisScale


class Axis(UniversalBaseModel):
    """
    A chart axis.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label of the axis.
    """

    scale: typing.Optional[AxisScale] = pydantic.Field(default=None)
    """
    The axis scale. By default, a linear scale is used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
