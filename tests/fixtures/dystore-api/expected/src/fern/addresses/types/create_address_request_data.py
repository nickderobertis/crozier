

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_address_request_data_attributes import CreateAddressRequestDataAttributes
from .create_address_request_data_relationships import CreateAddressRequestDataRelationships


class CreateAddressRequestData(UniversalBaseModel):
    attributes: typing.Optional[CreateAddressRequestDataAttributes] = None
    relationships: typing.Optional[CreateAddressRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
