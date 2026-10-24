

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_ads_connector_config import AmazonAdsConnectorConfig
from .amazon_spapi_connector_config import AmazonSpapiConnectorConfig
from .shopify_connector_config import ShopifyConnectorConfig


class ConnectorRegistration_Shopify(UniversalBaseModel):
    provider: typing.Literal["shopify"] = "shopify"
    external_account_id: str
    config: ShopifyConnectorConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorRegistration_AmazonSpapi(UniversalBaseModel):
    provider: typing.Literal["amazon_spapi"] = "amazon_spapi"
    external_account_id: str
    config: AmazonSpapiConnectorConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorRegistration_AmazonAds(UniversalBaseModel):
    provider: typing.Literal["amazon_ads"] = "amazon_ads"
    external_account_id: str
    config: AmazonAdsConnectorConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConnectorRegistration = typing_extensions.Annotated[
    typing.Union[ConnectorRegistration_Shopify, ConnectorRegistration_AmazonSpapi, ConnectorRegistration_AmazonAds],
    pydantic.Field(discriminator="provider"),
]
