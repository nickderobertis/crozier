

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cart_address_country_action_request_data_relationships_country import (
    UpdateCartAddressCountryActionRequestDataRelationshipsCountry,
)


class UpdateCartAddressCountryActionRequestDataRelationships(UniversalBaseModel):
    country: typing.Optional[UpdateCartAddressCountryActionRequestDataRelationshipsCountry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
