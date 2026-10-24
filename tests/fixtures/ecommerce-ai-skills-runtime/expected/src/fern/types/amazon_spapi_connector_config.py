

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_spapi_connector_config_region import AmazonSpapiConnectorConfigRegion


class AmazonSpapiConnectorConfig(UniversalBaseModel):
    region: AmazonSpapiConnectorConfigRegion
    marketplace_ids: typing.List[str]
    lwa_client_id_ref: str
    lwa_client_secret_ref: str
    lwa_refresh_token_ref: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
