

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cart_address_request_data_attributes import UpdateCartAddressRequestDataAttributes
from .update_cart_address_request_data_relationships import UpdateCartAddressRequestDataRelationships


class UpdateCartAddressRequestData(UniversalBaseModel):
    attributes: typing.Optional[UpdateCartAddressRequestDataAttributes] = None
    id: typing.Optional[str] = None
    relationships: typing.Optional[UpdateCartAddressRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
