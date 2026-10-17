

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_address_request_data_relationships_country import UpdateAddressRequestDataRelationshipsCountry
from .update_address_request_data_relationships_customer import UpdateAddressRequestDataRelationshipsCustomer


class UpdateAddressRequestDataRelationships(UniversalBaseModel):
    country: typing.Optional[UpdateAddressRequestDataRelationshipsCountry] = None
    customer: typing.Optional[UpdateAddressRequestDataRelationshipsCustomer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
