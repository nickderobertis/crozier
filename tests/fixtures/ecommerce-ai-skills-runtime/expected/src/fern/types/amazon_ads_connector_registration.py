

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_ads_connector_config import AmazonAdsConnectorConfig


class AmazonAdsConnectorRegistration(UniversalBaseModel):
    external_account_id: str
    config: AmazonAdsConnectorConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
