

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ivcs_webhook_type import IvcsWebhookType


class IvcsWebhook(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Webhook creation date"),
    ] = None
    """
    Webhook creation date
    """

    customer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="customerName"), pydantic.Field(alias="customerName", description="Customer Prisma ID")
    ]
    """
    Customer Prisma ID
    """

    domain: str = pydantic.Field()
    """
    Webhook URL domain
    """

    id: str = pydantic.Field()
    """
    VCS App ID
    """

    is_ssl_verification_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isSSLVerificationEnabled"),
        pydantic.Field(alias="isSSLVerificationEnabled", description="Webhook SSL verification enabled/disabled"),
    ] = None
    """
    Webhook SSL verification enabled/disabled
    """

    name: str = pydantic.Field()
    """
    VCS App name
    """

    node_created_timestamp: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="nodeCreatedTimestamp"),
        pydantic.Field(alias="nodeCreatedTimestamp"),
    ] = None
    timestamp: float
    triggers: typing.List[str] = pydantic.Field()
    """
    Webhook events triggers
    """

    type: IvcsWebhookType
    url: str = pydantic.Field()
    """
    Webhook URL
    """

    vendor_created_timestamp: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="vendorCreatedTimestamp"),
        pydantic.Field(alias="vendorCreatedTimestamp", description="Webhook creation date"),
    ] = None
    """
    Webhook creation date
    """

    webhook_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="webhookType"), pydantic.Field(alias="webhookType", description="Webhook type")
    ]
    """
    Webhook type
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="VCS workspace/integration ID"),
    ] = None
    """
    VCS workspace/integration ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
