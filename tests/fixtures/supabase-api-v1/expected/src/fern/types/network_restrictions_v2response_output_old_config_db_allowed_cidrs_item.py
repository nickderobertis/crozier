

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .network_restrictions_v2response_output_old_config_db_allowed_cidrs_item_type import (
    NetworkRestrictionsV2ResponseOutputOldConfigDbAllowedCidrsItemType,
)


class NetworkRestrictionsV2ResponseOutputOldConfigDbAllowedCidrsItem(UniversalBaseModel):
    address: str
    type: NetworkRestrictionsV2ResponseOutputOldConfigDbAllowedCidrsItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
