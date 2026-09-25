

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lights import Lights


class LightingSystemBase(UniversalBaseModel):
    """
    Expresses the Directional, Fog and Position vehicle lights.
    """

    turn: typing.Optional[Lights] = None
    fog: typing.Optional[Lights] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
