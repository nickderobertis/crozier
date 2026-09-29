

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bip_indicators import BipIndicators
from .usage_counts import UsageCounts


class Indicator(UniversalBaseModel):
    citation_impact: typing_extensions.Annotated[
        typing.Optional[BipIndicators], FieldMetadata(alias="citationImpact"), pydantic.Field(alias="citationImpact")
    ] = None
    usage_counts: typing_extensions.Annotated[
        typing.Optional[UsageCounts], FieldMetadata(alias="usageCounts"), pydantic.Field(alias="usageCounts")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
