

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cart_address_country_action_request_data_relationships import (
    UpdateCartAddressCountryActionRequestDataRelationships,
)


class UpdateCartAddressCountryActionRequestData(UniversalBaseModel):
    id: typing.Optional[str] = None
    relationships: typing.Optional[UpdateCartAddressCountryActionRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
