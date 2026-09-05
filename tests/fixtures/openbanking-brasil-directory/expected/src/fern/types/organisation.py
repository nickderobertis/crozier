

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organisation_id import OrganisationId
from .organisation_status import OrganisationStatus


class Organisation(UniversalBaseModel):
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

    company_register: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CompanyRegister"),
        pydantic.Field(
            alias="CompanyRegister", description="Legal company register for the country, i.e. Companies House"
        ),
    ] = None
    """
    Legal company register for the country, i.e. Companies House
    """

    country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Country"), pydantic.Field(alias="Country", description="Country")
    ] = None
    """
    Country
    """

    country_of_registration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CountryOfRegistration"),
        pydantic.Field(alias="CountryOfRegistration", description="Country of registration for the org"),
    ] = None
    """
    Country of registration for the org
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CreatedOn"),
        pydantic.Field(alias="CreatedOn", description="JSONDatetime of organisation creation."),
    ] = None
    """
    JSONDatetime of organisation creation.
    """

    legal_entity_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LegalEntityName"),
        pydantic.Field(
            alias="LegalEntityName", description="Legal Entity name for the org. Usually the same as org name"
        ),
    ] = None
    """
    Legal Entity name for the org. Usually the same as org name
    """

    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    organisation_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrganisationName"),
        pydantic.Field(alias="OrganisationName", description="Name of the organisation."),
    ] = None
    """
    Name of the organisation.
    """

    parent_organisation_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ParentOrganisationReference"),
        pydantic.Field(alias="ParentOrganisationReference", description="Parent Organisation Reference"),
    ] = None
    """
    Parent Organisation Reference
    """

    postcode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Postcode"), pydantic.Field(alias="Postcode", description="Postcode")
    ] = None
    """
    Postcode
    """

    registered_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RegisteredName"), pydantic.Field(alias="RegisteredName")
    ] = None
    registration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationId"),
        pydantic.Field(
            alias="RegistrationId", description="Registered ID for the organisation i.e. Legal Entity identifier number"
        ),
    ] = None
    """
    Registered ID for the organisation i.e. Legal Entity identifier number
    """

    registration_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationNumber"),
        pydantic.Field(
            alias="RegistrationNumber",
            description="Company registration number from company register i.e. Companies House registration number",
        ),
    ] = None
    """
    Company registration number from company register i.e. Companies House registration number
    """

    requires_participant_terms_and_conditions_signing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="RequiresParticipantTermsAndConditionsSigning"),
        pydantic.Field(
            alias="RequiresParticipantTermsAndConditionsSigning",
            description="true - this organisation requires terms and conditions to be signed. false - this organisation does not require terms and conditions to be signed",
        ),
    ] = None
    """
    true - this organisation requires terms and conditions to be signed. false - this organisation does not require terms and conditions to be signed
    """

    size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Size"),
        pydantic.Field(alias="Size", description="Size of the organisation"),
    ] = None
    """
    Size of the organisation
    """

    status: typing_extensions.Annotated[
        typing.Optional[OrganisationStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Status of the directory registration of an organisation"),
    ] = None
    """
    Status of the directory registration of an organisation
    """

    tags: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Tags"),
        pydantic.Field(alias="Tags", description="Tags to describe or classify an organisation"),
    ] = None
    """
    Tags to describe or classify an organisation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
