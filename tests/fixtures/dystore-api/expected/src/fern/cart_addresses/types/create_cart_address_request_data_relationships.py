

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_cart_address_request_data_relationships_cart import CreateCartAddressRequestDataRelationshipsCart
from .create_cart_address_request_data_relationships_country import CreateCartAddressRequestDataRelationshipsCountry


class CreateCartAddressRequestDataRelationships(UniversalBaseModel):
    cart: typing.Optional[CreateCartAddressRequestDataRelationshipsCart] = None
    country: typing.Optional[CreateCartAddressRequestDataRelationshipsCountry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
