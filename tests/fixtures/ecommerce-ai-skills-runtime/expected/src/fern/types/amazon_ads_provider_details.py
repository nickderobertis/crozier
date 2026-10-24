

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_ads_provider_details_region import AmazonAdsProviderDetailsRegion


class AmazonAdsProviderDetails(UniversalBaseModel):
    region: AmazonAdsProviderDetailsRegion
    profile_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
