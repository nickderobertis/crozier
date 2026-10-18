

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_address_request_data_attributes import UpdateAddressRequestDataAttributes
from .update_address_request_data_relationships import UpdateAddressRequestDataRelationships


class UpdateAddressRequestData(UniversalBaseModel):
    attributes: typing.Optional[UpdateAddressRequestDataAttributes] = None
    id: typing.Optional[str] = None
    relationships: typing.Optional[UpdateAddressRequestDataRelationships] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
