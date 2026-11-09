

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class AssetsProductReadyWebhook(UniversalBaseModel):
    """
    Fired when the Asset Report has been generated and `/asset_report/get` is ready to be called.  If you attempt to retrieve an Asset Report before this webhook has fired, you’ll receive a response with the HTTP status code 400 and a Plaid error code of `PRODUCT_NOT_READY`.
    """

    asset_report_id: str = pydantic.Field()
    """
    The `asset_report_id` corresponding to the Asset Report the webhook has fired for.
    """

    environment: WebhookEnvironmentValues
    report_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The report type, indicating whether the Asset Report is a `full` or `fast` report.
    """

    webhook_code: str = pydantic.Field()
    """
    `PRODUCT_READY`
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
