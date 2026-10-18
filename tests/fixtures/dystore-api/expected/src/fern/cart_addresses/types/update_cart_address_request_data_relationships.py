

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cart_address_request_data_relationships_cart import UpdateCartAddressRequestDataRelationshipsCart
from .update_cart_address_request_data_relationships_country import UpdateCartAddressRequestDataRelationshipsCountry


class UpdateCartAddressRequestDataRelationships(UniversalBaseModel):
    cart: typing.Optional[UpdateCartAddressRequestDataRelationshipsCart] = None
    country: typing.Optional[UpdateCartAddressRequestDataRelationshipsCountry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
