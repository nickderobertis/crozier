

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowVideoEssenceParametersFrameRate(UniversalBaseModel):
    """
    The fixed number of frames per second. MUST be set if `vfr` is `false` or omitted. MUST NOT be set if `vfr` is `true`.
    """

    numerator: int = pydantic.Field()
    """
    numerator
    """

    denominator: typing.Optional[int] = pydantic.Field(default=None)
    """
    denominator
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
