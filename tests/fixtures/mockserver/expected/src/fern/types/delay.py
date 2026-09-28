

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay_distribution import DelayDistribution
from .delay_template_type import DelayTemplateType
from .delay_time_unit import DelayTimeUnit


class Delay(UniversalBaseModel):
    """
    response delay
    """

    time_unit: typing_extensions.Annotated[
        typing.Optional[DelayTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None
    value: typing.Optional[int] = None
    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    opt-in template rendered against the request whose output is parsed as a millisecond delay (e.g. respond more slowly for larger payloads); falls back to value/timeUnit on a non-numeric or blank result
    """

    template_type: typing_extensions.Annotated[
        typing.Optional[DelayTemplateType],
        FieldMetadata(alias="templateType"),
        pydantic.Field(
            alias="templateType",
            description="template engine used to evaluate the delay template; only VELOCITY and MUSTACHE are supported",
        ),
    ] = None
    """
    template engine used to evaluate the delay template; only VELOCITY and MUSTACHE are supported
    """

    distribution: typing.Optional[DelayDistribution] = pydantic.Field(default=None)
    """
    distribution for variable delays: UNIFORM requires min and max, LOG_NORMAL requires median and p99, GAUSSIAN requires mean and stdDev
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
