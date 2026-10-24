

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_spapi_provider_details_region import AmazonSpapiProviderDetailsRegion


class AmazonSpapiProviderDetails(UniversalBaseModel):
    region: AmazonSpapiProviderDetailsRegion
    marketplace_ids: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
