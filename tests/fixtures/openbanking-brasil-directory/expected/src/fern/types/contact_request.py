

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_request_contact_type import ContactRequestContactType


class ContactRequest(UniversalBaseModel):
    additional_information: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AdditionalInformation"),
        pydantic.Field(alias="AdditionalInformation", description="Any additional user information"),
    ] = None
    """
    Any additional user information
    """

    address_line1: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AddressLine1"),
        pydantic.Field(alias="AddressLine1", description="Address line 1"),
    ] = None
    """
    Address line 1
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AddressLine2"),
        pydantic.Field(alias="AddressLine2", description="Address line 2"),
    ] = None
    """
    Address line 2
    """

    city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="City"), pydantic.Field(alias="City", description="City")
    ] = None
    """
    City
    """

    contact_type: typing_extensions.Annotated[
        ContactRequestContactType,
        FieldMetadata(alias="ContactType"),
        pydantic.Field(alias="ContactType", description="The type of Contact, default contact type is Business."),
    ]
    """
    The type of Contact, default contact type is Business.
    """

    country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Country"), pydantic.Field(alias="Country", description="Country")
    ] = None
    """
    Country
    """

    department: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Department"), pydantic.Field(alias="Department")
    ] = None
    email_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="EmailAddress"), pydantic.Field(alias="EmailAddress")
    ]
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="FirstName"), pydantic.Field(alias="FirstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LastName"), pydantic.Field(alias="LastName")
    ] = None
    pgp_public_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PgpPublicKey"),
        pydantic.Field(alias="PgpPublicKey", description="A PGP Public Key in text form"),
    ] = None
    """
    A PGP Public Key in text form
    """

    phone_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PhoneNumber"), pydantic.Field(alias="PhoneNumber")
    ] = None
    postcode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Postcode"), pydantic.Field(alias="Postcode", description="Postcode")
    ] = None
    """
    Postcode
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
