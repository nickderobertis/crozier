

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .email import Email
from .phone import Phone


class Contact(UniversalBaseModel):
    """
    Contact object data schema.
    """

    address_array: typing_extensions.Annotated[
        typing.Optional[typing.List[Address]],
        FieldMetadata(alias="addressArray"),
        pydantic.Field(alias="addressArray", description="List of available addresses."),
    ] = None
    """
    List of available addresses.
    """

    email_array: typing_extensions.Annotated[
        typing.Optional[typing.List[Email]],
        FieldMetadata(alias="emailArray"),
        pydantic.Field(alias="emailArray", description="List of available emails."),
    ] = None
    """
    List of available emails.
    """

    object: str
    phone_number_array: typing_extensions.Annotated[
        typing.Optional[typing.List[Phone]],
        FieldMetadata(alias="phoneNumberArray"),
        pydantic.Field(alias="phoneNumberArray", description="List of available phone numbers."),
    ] = None
    """
    List of available phone numbers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
