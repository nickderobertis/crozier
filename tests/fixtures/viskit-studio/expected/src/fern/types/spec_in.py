

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detail_section_in import DetailSectionIn
from .hero_section_in import HeroSectionIn
from .selling_point_in import SellingPointIn
from .sku_meta_in import SkuMetaIn
from .spec_in_locale import SpecInLocale


class SpecIn(UniversalBaseModel):
    detail_sections: typing.List[DetailSectionIn]
    hero_sections: typing.List[HeroSectionIn]
    locale: SpecInLocale
    selling_points: typing.List[SellingPointIn]
    sku_meta: SkuMetaIn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
