

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operator_webhook_dbt_cloud import OperatorWebhookDbtCloud
from .operator_webhook_webhook_type import OperatorWebhookWebhookType


class OperatorWebhook(UniversalBaseModel):
    dbt_cloud: typing_extensions.Annotated[
        typing.Optional[OperatorWebhookDbtCloud], FieldMetadata(alias="dbtCloud"), pydantic.Field(alias="dbtCloud")
    ] = None
    execution_body: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="executionBody"),
        pydantic.Field(alias="executionBody", description="DEPRECATED. Populate dbtCloud instead."),
    ] = None
    """
    DEPRECATED. Populate dbtCloud instead.
    """

    execution_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="executionUrl"),
        pydantic.Field(alias="executionUrl", description="DEPRECATED. Populate dbtCloud instead."),
    ] = None
    """
    DEPRECATED. Populate dbtCloud instead.
    """

    webhook_config_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookConfigId"),
        pydantic.Field(alias="webhookConfigId", description="The id of the webhook configs to use from the workspace."),
    ] = None
    """
    The id of the webhook configs to use from the workspace.
    """

    webhook_type: typing_extensions.Annotated[
        typing.Optional[OperatorWebhookWebhookType],
        FieldMetadata(alias="webhookType"),
        pydantic.Field(alias="webhookType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
