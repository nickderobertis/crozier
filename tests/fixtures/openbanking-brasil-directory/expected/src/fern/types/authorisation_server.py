

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_resource import ApiResource
from .auth_deprecated_date import AuthDeprecatedDate
from .auth_retirement_date import AuthRetirementDate
from .auth_superseded_by_id import AuthSupersededById
from .authorisation_server_certification import AuthorisationServerCertification
from .authorisation_server_id import AuthorisationServerId
from .notification_webhook_status_enum import NotificationWebhookStatusEnum
from .organisation_id import OrganisationId
from .sns_notification_webhook_uri import SnsNotificationWebhookUri


class AuthorisationServer(UniversalBaseModel):
    api_resources: typing_extensions.Annotated[
        typing.Optional[typing.List[ApiResource]],
        FieldMetadata(alias="ApiResources"),
        pydantic.Field(alias="ApiResources"),
    ] = None
    authorisation_server_certifications: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorisationServerCertification]],
        FieldMetadata(alias="AuthorisationServerCertifications"),
        pydantic.Field(alias="AuthorisationServerCertifications"),
    ] = None
    authorisation_server_id: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerId],
        FieldMetadata(alias="AuthorisationServerId"),
        pydantic.Field(alias="AuthorisationServerId"),
    ] = None
    auto_registration_notification_webhook: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AutoRegistrationNotificationWebhook"),
        pydantic.Field(
            alias="AutoRegistrationNotificationWebhook",
            description="A compliant URI to subscribe to the software statement onboarding webhook",
        ),
    ] = None
    """
    A compliant URI to subscribe to the software statement onboarding webhook
    """

    auto_registration_supported: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AutoRegistrationSupported"),
        pydantic.Field(
            alias="AutoRegistrationSupported",
            description="Flag to denote if this authorisation server supports the automatic onboarding of software statement clients",
        ),
    ] = None
    """
    Flag to denote if this authorisation server supports the automatic onboarding of software statement clients
    """

    customer_friendly_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CustomerFriendlyDescription"),
        pydantic.Field(alias="CustomerFriendlyDescription"),
    ] = None
    customer_friendly_logo_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CustomerFriendlyLogoUri"),
        pydantic.Field(alias="CustomerFriendlyLogoUri", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    customer_friendly_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CustomerFriendlyName"), pydantic.Field(alias="CustomerFriendlyName")
    ] = None
    deprecated_date: typing_extensions.Annotated[
        typing.Optional[AuthDeprecatedDate],
        FieldMetadata(alias="DeprecatedDate"),
        pydantic.Field(alias="DeprecatedDate"),
    ] = None
    developer_portal_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DeveloperPortalUri"),
        pydantic.Field(alias="DeveloperPortalUri", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    issuer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Issuer"),
        pydantic.Field(alias="Issuer", description="An issuer value pulled from the well-known endpoint"),
    ] = None
    """
    An issuer value pulled from the well-known endpoint
    """

    notification_webhook: typing_extensions.Annotated[
        typing.Optional[SnsNotificationWebhookUri],
        FieldMetadata(alias="NotificationWebhook"),
        pydantic.Field(alias="NotificationWebhook"),
    ] = None
    notification_webhook_added_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="NotificationWebhookAddedDate"),
        pydantic.Field(alias="NotificationWebhookAddedDate", description="Creation date"),
    ] = None
    """
    Creation date
    """

    notification_webhook_status: typing_extensions.Annotated[
        typing.Optional[NotificationWebhookStatusEnum],
        FieldMetadata(alias="NotificationWebhookStatus"),
        pydantic.Field(alias="NotificationWebhookStatus"),
    ] = None
    open_id_discovery_document: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OpenIDDiscoveryDocument"),
        pydantic.Field(alias="OpenIDDiscoveryDocument", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    parent_authorisation_server_id: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerId],
        FieldMetadata(alias="ParentAuthorisationServerId"),
        pydantic.Field(alias="ParentAuthorisationServerId"),
    ] = None
    payload_signing_cert_location_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayloadSigningCertLocationUri"),
        pydantic.Field(alias="PayloadSigningCertLocationUri", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    retirement_date: typing_extensions.Annotated[
        typing.Optional[AuthRetirementDate],
        FieldMetadata(alias="RetirementDate"),
        pydantic.Field(alias="RetirementDate"),
    ] = None
    superseded_by_authorisation_server_id: typing_extensions.Annotated[
        typing.Optional[AuthSupersededById],
        FieldMetadata(alias="SupersededByAuthorisationServerId"),
        pydantic.Field(alias="SupersededByAuthorisationServerId"),
    ] = None
    supports_ciba: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="SupportsCiba"), pydantic.Field(alias="SupportsCiba")
    ] = None
    supports_dcr: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="SupportsDCR"), pydantic.Field(alias="SupportsDCR")
    ] = None
    terms_of_service_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TermsOfServiceUri"),
        pydantic.Field(alias="TermsOfServiceUri", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
