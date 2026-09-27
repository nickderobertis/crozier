

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_categories_updated_webhook_data import AccountCategoriesUpdatedWebhookData


class AccountCategoriesUpdatedWebhook(UniversalBaseModel):
    """
    Webhook request body for account categories updated.
    """

    alert_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="alertId"),
        pydantic.Field(alias="alertId", description="Unique identifier of the alert."),
    ] = None
    """
    Unique identifier of the alert.
    """

    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="Unique identifier for your client in Codat."),
    ] = None
    """
    Unique identifier for your client in Codat.
    """

    client_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientName"),
        pydantic.Field(alias="clientName", description="Name of your client in Codat."),
    ] = None
    """
    Name of your client in Codat.
    """

    company_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="companyId"),
        pydantic.Field(alias="companyId", description="Unique identifier for your SMB in Codat."),
    ] = None
    """
    Unique identifier for your SMB in Codat.
    """

    data: typing.Optional[AccountCategoriesUpdatedWebhookData] = None
    data_connection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dataConnectionId"),
        pydantic.Field(alias="dataConnectionId", description="Unique identifier for a company's data connection."),
    ] = None
    """
    Unique identifier for a company's data connection.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human readable message about the webhook.
    """

    rule_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ruleId"),
        pydantic.Field(alias="ruleId", description="Unique identifier for the rule."),
    ] = None
    """
    Unique identifier for the rule.
    """

    rule_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ruleType"),
        pydantic.Field(alias="ruleType", description="The type of rule."),
    ] = None
    """
    The type of rule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
