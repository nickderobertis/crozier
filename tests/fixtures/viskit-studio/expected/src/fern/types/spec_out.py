

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detail_section_out import DetailSectionOut
from .hero_section_out import HeroSectionOut
from .selling_point_in import SellingPointIn
from .sku_meta_in import SkuMetaIn
from .spec_out_locale import SpecOutLocale


class SpecOut(UniversalBaseModel):
    detail_sections: typing.List[DetailSectionOut]
    hero_sections: typing.List[HeroSectionOut]
    locale: SpecOutLocale
    selling_points: typing.List[SellingPointIn]
    sku_meta: SkuMetaIn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
