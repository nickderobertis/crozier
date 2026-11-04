

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TestDescriptorPerformancePrediction(UniversalBaseModel):
    """
    This attribute provides the capability to predict KQIs and KPIs.
    """

    availability: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of KQIs and KPIs available for monitoring
    """

    frequency: typing.Optional[int] = pydantic.Field(default=None)
    """
    Seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
