

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_cart_address_request_data_attributes import CreateCartAddressRequestDataAttributes
from .create_cart_address_request_data_relationships import CreateCartAddressRequestDataRelationships


class CreateCartAddressRequestData(UniversalBaseModel):
    attributes: typing.Optional[CreateCartAddressRequestDataAttributes] = None
    relationships: typing.Optional[CreateCartAddressRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
