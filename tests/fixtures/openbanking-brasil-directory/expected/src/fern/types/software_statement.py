

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_webhook_status_enum import NotificationWebhookStatusEnum
from .organisation_id import OrganisationId
from .sns_notification_webhook_uri import SnsNotificationWebhookUri
from .software_statement_certification import SoftwareStatementCertification
from .software_statement_id import SoftwareStatementId
from .software_statement_mode import SoftwareStatementMode
from .software_statement_status import SoftwareStatementStatus


class SoftwareStatement(UniversalBaseModel):
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

    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientId"),
        pydantic.Field(alias="ClientId", description="Software Statement client Id"),
    ] = None
    """
    Software Statement client Id
    """

    client_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientName"),
        pydantic.Field(alias="ClientName", description="Software Statement client name"),
    ] = None
    """
    Software Statement client name
    """

    client_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientUri"),
        pydantic.Field(alias="ClientUri", description="The Software Statement client compliant URI"),
    ] = None
    """
    The Software Statement client compliant URI
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
            alias="Environment", description="The additional check for software statement, this field can avoid"
        ),
    ] = None
    """
    The additional check for software statement, this field can avoid
    """

    locked: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Locked"),
        pydantic.Field(
            alias="Locked",
            description="Flag shows if assertion has been generated on the software statement - will be set to true when assertion is generated",
        ),
    ] = None
    """
    Flag shows if assertion has been generated on the software statement - will be set to true when assertion is generated
    """

    logo_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LogoUri"),
        pydantic.Field(alias="LogoUri", description="The Software Statement logo compliant URI"),
    ] = None
    """
    The Software Statement logo compliant URI
    """

    mode: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementMode],
        FieldMetadata(alias="Mode"),
        pydantic.Field(alias="Mode", description="Software Statement mode"),
    ] = None
    """
    Software Statement mode
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

    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    policy_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PolicyUri"),
        pydantic.Field(alias="PolicyUri", description="The Software Statement policy compliant URI"),
    ] = None
    """
    The Software Statement policy compliant URI
    """

    redirect_uri: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="RedirectUri"),
        pydantic.Field(alias="RedirectUri", description="The Software Statement redirect compliant URI"),
    ] = None
    """
    The Software Statement redirect compliant URI
    """

    rts_client_created: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="RtsClientCreated"),
        pydantic.Field(alias="RtsClientCreated", description="Client created flag"),
    ] = None
    """
    Client created flag
    """

    software_statement_certifications: typing_extensions.Annotated[
        typing.Optional[typing.List[SoftwareStatementCertification]],
        FieldMetadata(alias="SoftwareStatementCertifications"),
        pydantic.Field(alias="SoftwareStatementCertifications"),
    ] = None
    software_statement_id: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementId],
        FieldMetadata(alias="SoftwareStatementId"),
        pydantic.Field(alias="SoftwareStatementId"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Is this software statement Active/Suspended/Inactive"),
    ] = None
    """
    Is this software statement Active/Suspended/Inactive
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
        typing.Optional[float],
        FieldMetadata(alias="Version"),
        pydantic.Field(alias="Version", description="Software Statement version as provided by the organisation's PTC"),
    ] = None
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
