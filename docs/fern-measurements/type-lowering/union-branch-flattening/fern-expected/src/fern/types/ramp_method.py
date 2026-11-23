

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ramp_method_direction import RampMethodDirection


class RampMethod(UniversalBaseModel):
    """
    Inline oneOf branches.
    """

    id: str
    direction: typing.Optional[RampMethodDirection] = None
    limit: typing.Optional[str] = None
    fiat: typing.Optional[str] = None
    chain: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
