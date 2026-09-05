

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_links import PageLinks
from .page_meta_info_limit_offset import PageMetaInfoLimitOffset
from .pricing_plan_get import PricingPlanGet


class PagePricingPlanGet(UniversalBaseModel):
    meta: typing_extensions.Annotated[
        PageMetaInfoLimitOffset, FieldMetadata(alias="_meta"), pydantic.Field(alias="_meta")
    ]
    links: typing_extensions.Annotated[PageLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    data: typing.List[PricingPlanGet]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
