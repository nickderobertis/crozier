

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay_distribution_type import DelayDistributionType


class DelayDistribution(UniversalBaseModel):
    """
    distribution for variable delays: UNIFORM requires min and max, LOG_NORMAL requires median and p99, GAUSSIAN requires mean and stdDev
    """

    type: DelayDistributionType
    min: typing.Optional[int] = None
    max: typing.Optional[int] = None
    median: typing.Optional[int] = None
    p99: typing.Optional[int] = None
    mean: typing.Optional[int] = None
    std_dev: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="stdDev"), pydantic.Field(alias="stdDev")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
