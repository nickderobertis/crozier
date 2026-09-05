

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_deprecated_date import AuthDeprecatedDate
from .auth_retirement_date import AuthRetirementDate
from .auth_superseded_by_id import AuthSupersededById
from .authorisation_server_id import AuthorisationServerId
from .sns_notification_webhook_uri import SnsNotificationWebhookUri


class AuthorisationServerRequest(UniversalBaseModel):
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
        bool,
        FieldMetadata(alias="AutoRegistrationSupported"),
        pydantic.Field(
            alias="AutoRegistrationSupported",
            description="Flag to denote if this authorisation server supports the automatic onboarding of software statement clients",
        ),
    ]
    """
    Flag to denote if this authorisation server supports the automatic onboarding of software statement clients
    """

    customer_friendly_description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CustomerFriendlyDescription"),
        pydantic.Field(alias="CustomerFriendlyDescription", description="A customer friendly description"),
    ]
    """
    A customer friendly description
    """

    customer_friendly_logo_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CustomerFriendlyLogoUri"),
        pydantic.Field(alias="CustomerFriendlyLogoUri", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

    customer_friendly_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="CustomerFriendlyName"), pydantic.Field(alias="CustomerFriendlyName")
    ]
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

    notification_webhook: typing_extensions.Annotated[
        typing.Optional[SnsNotificationWebhookUri],
        FieldMetadata(alias="NotificationWebhook"),
        pydantic.Field(alias="NotificationWebhook"),
    ] = None
    open_id_discovery_document: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OpenIDDiscoveryDocument"),
        pydantic.Field(alias="OpenIDDiscoveryDocument", description="A compliant URI"),
    ] = None
    """
    A compliant URI
    """

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
