

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_information_preferred_contact_method import ContactInformationPreferredContactMethod


class ContactInformation(UniversalBaseModel):
    primary_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="primaryEmail"),
        pydantic.Field(alias="primaryEmail", description="Primäre E-Mail-Adresse"),
    ] = None
    """
    Primäre E-Mail-Adresse
    """

    secondary_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="secondaryEmail"),
        pydantic.Field(alias="secondaryEmail", description="Sekundäre E-Mail-Adresse"),
    ] = None
    """
    Sekundäre E-Mail-Adresse
    """

    mobile_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mobilePhone"),
        pydantic.Field(alias="mobilePhone", description="Mobiltelefonnummer (E.164 Format)"),
    ] = None
    """
    Mobiltelefonnummer (E.164 Format)
    """

    landline_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="landlinePhone"),
        pydantic.Field(alias="landlinePhone", description="Festnetznummer"),
    ] = None
    """
    Festnetznummer
    """

    preferred_contact_method: typing_extensions.Annotated[
        typing.Optional[ContactInformationPreferredContactMethod],
        FieldMetadata(alias="preferredContactMethod"),
        pydantic.Field(alias="preferredContactMethod"),
    ] = None
    communication_language: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="communicationLanguage"),
        pydantic.Field(alias="communicationLanguage", description="Kommunikationssprache"),
    ] = None
    """
    Kommunikationssprache
    """

    availability_hours: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="availabilityHours"),
        pydantic.Field(alias="availabilityHours", description="Verfügbarkeitszeiten"),
    ] = None
    """
    Verfügbarkeitszeiten
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
