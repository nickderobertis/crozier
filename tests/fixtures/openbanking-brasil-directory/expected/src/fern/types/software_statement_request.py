

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_webhook_status_enum import NotificationWebhookStatusEnum
from .sns_notification_webhook_uri import SnsNotificationWebhookUri
from .software_statement_request_mode import SoftwareStatementRequestMode


class SoftwareStatementRequest(UniversalBaseModel):
    additional_software_metadata: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AdditionalSoftwareMetadata"),
        pydantic.Field(
            alias="AdditionalSoftwareMetadata",
            description="Extra metadata defined by the org admins to be loaded into the software statement and made avaiable during introspection",
        ),
    ] = None
    """
    Extra metadata defined by the org admins to be loaded into the software statement and made avaiable during introspection
    """

    client_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ClientName"),
        pydantic.Field(alias="ClientName", description="Software Statement client name"),
    ]
    """
    Software Statement client name
    """

    client_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ClientUri"),
        pydantic.Field(alias="ClientUri", description="The Software Statement compliant client URI"),
    ]
    """
    The Software Statement compliant client URI
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Software Statement description"),
    ] = None
    """
    Software Statement description
    """

    environment: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Environment"),
        pydantic.Field(
            alias="Environment",
            description="The additional check for software statement, this field can avoid environment checks.",
        ),
    ] = None
    """
    The additional check for software statement, this field can avoid environment checks.
    """

    logo_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogoUri"),
        pydantic.Field(alias="LogoUri", description="The Software Statement compliant logo URI"),
    ]
    """
    The Software Statement compliant logo URI
    """

    mode: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementRequestMode],
        FieldMetadata(alias="Mode"),
        pydantic.Field(
            alias="Mode", description="The additional check to see if the environment reflected above is live or test."
        ),
    ] = None
    """
    The additional check to see if the environment reflected above is live or test.
    """

    notification_webhook: typing_extensions.Annotated[
        typing.Optional[SnsNotificationWebhookUri],
        FieldMetadata(alias="NotificationWebhook"),
        pydantic.Field(alias="NotificationWebhook"),
    ] = None
    notification_webhook_status: typing_extensions.Annotated[
        typing.Optional[NotificationWebhookStatusEnum],
        FieldMetadata(alias="NotificationWebhookStatus"),
        pydantic.Field(alias="NotificationWebhookStatus"),
    ] = None
    on_behalf_of: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OnBehalfOf"),
        pydantic.Field(
            alias="OnBehalfOf",
            description="A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another",
        ),
    ] = None
    """
    A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another
    """

    policy_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PolicyUri"),
        pydantic.Field(alias="PolicyUri", description="The Software Statement compliant policy URI"),
    ] = None
    """
    The Software Statement compliant policy URI
    """

    redirect_uri: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="RedirectUri"),
        pydantic.Field(alias="RedirectUri", description="The Software Statement redirect URIs"),
    ]
    """
    The Software Statement redirect URIs
    """

    terms_of_service_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TermsOfServiceUri"),
        pydantic.Field(alias="TermsOfServiceUri", description="The Software Statement terms of service compliant URI"),
    ] = None
    """
    The Software Statement terms of service compliant URI
    """

    version: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="Version"),
        pydantic.Field(alias="Version", description="Software Statement version as provided by the organisation's PTC"),
    ]
    """
    Software Statement version as provided by the organisation's PTC
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
