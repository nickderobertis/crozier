

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_address_request_data_relationships_country_data import CreateAddressRequestDataRelationshipsCountryData


class CreateAddressRequestDataRelationshipsCountry(UniversalBaseModel):
    data: typing.Optional[CreateAddressRequestDataRelationshipsCountryData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
