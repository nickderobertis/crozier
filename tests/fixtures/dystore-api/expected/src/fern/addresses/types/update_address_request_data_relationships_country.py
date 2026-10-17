

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_address_request_data_relationships_country_data import UpdateAddressRequestDataRelationshipsCountryData


class UpdateAddressRequestDataRelationshipsCountry(UniversalBaseModel):
    data: typing.Optional[UpdateAddressRequestDataRelationshipsCountryData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
