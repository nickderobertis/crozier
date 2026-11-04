

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .contact import Contact
from .email import Email
from .non_empty_id import NonEmptyId


class Customer(UniversalBaseModel):
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    billing_address: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="billingAddress"), pydantic.Field(alias="billingAddress")
    ] = None
    bio: typing.Optional[str] = None
    contact: Contact
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    email: Email
    id: NonEmptyId
    loyalty_points: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="loyaltyPoints"), pydantic.Field(alias="loyaltyPoints")
    ] = None
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
