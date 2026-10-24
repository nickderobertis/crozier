

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_spapi_connector_config import AmazonSpapiConnectorConfig


class AmazonSpapiConnectorRegistration(UniversalBaseModel):
    external_account_id: str
    config: AmazonSpapiConnectorConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
