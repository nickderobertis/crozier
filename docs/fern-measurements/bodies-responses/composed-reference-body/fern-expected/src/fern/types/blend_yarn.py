

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BlendYarn(UniversalBaseModel):
    yarn: typing.Optional[str] = None
    gauge: typing.Optional[int] = pydantic.Field(default=None)
    """
    The yarn's gauge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
