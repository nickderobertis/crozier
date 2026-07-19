

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowCoreSegmentDuration(UniversalBaseModel):
    """
    The target Flow Segment duration in seconds. The duration for each Segment may vary around this target value. See also the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote for how this property can be used to calculate buffer sizes.
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
