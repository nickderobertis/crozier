

import typing

from .amazon_ads_connector_config import AmazonAdsConnectorConfig
from .amazon_spapi_connector_config import AmazonSpapiConnectorConfig
from .shopify_connector_config import ShopifyConnectorConfig

ConnectorUpdateRequestConfig = typing.Union[
    ShopifyConnectorConfig, AmazonSpapiConnectorConfig, AmazonAdsConnectorConfig
]
