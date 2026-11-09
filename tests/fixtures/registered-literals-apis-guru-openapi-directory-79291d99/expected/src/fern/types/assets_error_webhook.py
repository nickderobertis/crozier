

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class AssetsErrorWebhook(UniversalBaseModel):
    """
    Fired when Asset Report generation has failed. The resulting `error` will have an `error_type` of `ASSET_REPORT_ERROR`.
    """

    asset_report_id: str = pydantic.Field()
    """
    The ID associated with the Asset Report.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    webhook_code: str = pydantic.Field()
    """
    `ERROR`
    """

    webhook_type: str = pydantic.Field()
    """
    `ASSETS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
