

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_address_request_data_relationships_country import CreateAddressRequestDataRelationshipsCountry
from .create_address_request_data_relationships_customer import CreateAddressRequestDataRelationshipsCustomer


class CreateAddressRequestDataRelationships(UniversalBaseModel):
    country: typing.Optional[CreateAddressRequestDataRelationshipsCountry] = None
    customer: typing.Optional[CreateAddressRequestDataRelationshipsCustomer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
