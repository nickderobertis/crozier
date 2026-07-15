

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClassLevelClassSpecificWildShapeFly(UniversalBaseModel):
    """
    Druid Class Specific Features
    """

    wild_shape_fly: typing.Optional[bool] = None
    wild_shape_max_cr: typing.Optional[float] = None
    wild_shape_swim: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
