

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_address_request_data_relationships_customer_data import UpdateAddressRequestDataRelationshipsCustomerData


class UpdateAddressRequestDataRelationshipsCustomer(UniversalBaseModel):
    data: typing.Optional[UpdateAddressRequestDataRelationshipsCustomerData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
