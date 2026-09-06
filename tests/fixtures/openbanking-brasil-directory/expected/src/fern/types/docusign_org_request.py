

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .organisation_request import OrganisationRequest


class DocusignOrgRequest(OrganisationRequest):
    buss_contact_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BussContactEmail"),
        pydantic.Field(alias="BussContactEmail", description="Business contact email"),
    ] = None
    """
    Business contact email
    """

    buss_contact_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BussContactName"),
        pydantic.Field(alias="BussContactName", description="Business contact full name"),
    ] = None
    """
    Business contact full name
    """

    buss_contact_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BussContactPhone"),
        pydantic.Field(alias="BussContactPhone", description="Business contact phone number"),
    ] = None
    """
    Business contact phone number
    """

    cert_issuer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CertIssuer"),
        pydantic.Field(alias="CertIssuer", description="Certificate Issuer"),
    ] = None
    """
    Certificate Issuer
    """

    dialog_eq_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DialogEqId"),
        pydantic.Field(alias="DialogEqId", description="Dialog Eq Id"),
    ] = None
    """
    Dialog Eq Id
    """

    environment_startdate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EnvironmentStartdate"),
        pydantic.Field(alias="EnvironmentStartdate", description="Environment start date"),
    ] = None
    """
    Environment start date
    """

    first_point_of_contact: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FirstPointOfContact"),
        pydantic.Field(alias="FirstPointOfContact", description="First point of contact"),
    ] = None
    """
    First point of contact
    """

    legal_access_entity: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LegalAccessEntity"),
        pydantic.Field(alias="LegalAccessEntity", description="Legal Access Entity"),
    ] = None
    """
    Legal Access Entity
    """

    org_bank_line_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrgBankLineId"),
        pydantic.Field(alias="OrgBankLineId", description="Organisation Bankline Id"),
    ] = None
    """
    Organisation Bankline Id
    """

    org_individual_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrgIndividualId"),
        pydantic.Field(alias="OrgIndividualId", description="Organisation Invdividual Id"),
    ] = None
    """
    Organisation Invdividual Id
    """

    org_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrgNumber"),
        pydantic.Field(alias="OrgNumber", description="Organisation Number (BINM)"),
    ] = None
    """
    Organisation Number (BINM)
    """

    payment_sought: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PaymentSought"),
        pydantic.Field(alias="PaymentSought", description="Payment being sought"),
    ] = None
    """
    Payment being sought
    """

    platform_accessing: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PlatformAccessing"),
        pydantic.Field(alias="PlatformAccessing", description="Platform being accessed"),
    ] = None
    """
    Platform being accessed
    """

    platform_api_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PlatformApiType"),
        pydantic.Field(alias="PlatformApiType", description="Platform Api type"),
    ] = None
    """
    Platform Api type
    """

    project_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ProjectDescription"),
        pydantic.Field(alias="ProjectDescription", description="Project description"),
    ] = None
    """
    Project description
    """

    redirect_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RedirectUri"),
        pydantic.Field(alias="RedirectUri", description="Redirect Uri"),
    ] = None
    """
    Redirect Uri
    """

    security_profile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SecurityProfile"),
        pydantic.Field(alias="SecurityProfile", description="Security Profile"),
    ] = None
    """
    Security Profile
    """

    tech_contact_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TechContactEmail"),
        pydantic.Field(alias="TechContactEmail", description="Technical contact email"),
    ] = None
    """
    Technical contact email
    """

    tech_contact_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TechContactName"),
        pydantic.Field(alias="TechContactName", description="Technical contact name"),
    ] = None
    """
    Technical contact name
    """

    tech_contact_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TechContactPhone"),
        pydantic.Field(alias="TechContactPhone", description="Technical contact phone number"),
    ] = None
    """
    Technical contact phone number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
