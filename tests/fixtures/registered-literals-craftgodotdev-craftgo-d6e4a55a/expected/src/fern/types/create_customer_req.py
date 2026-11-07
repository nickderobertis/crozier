

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .contact import Contact
from .email import Email


class CreateCustomerReq(UniversalBaseModel):
    bio: typing.Optional[str] = None
    contact: Contact
    email: Email
    name: str
    primary_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="primaryAddress"), pydantic.Field(alias="primaryAddress")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
