

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class ScreeningStatusUpdatedWebhook(UniversalBaseModel):
    """
    Fired when an individual screening status has changed, which can occur manually via the dashboard or during ongoing monitoring.
    """

    environment: WebhookEnvironmentValues
    screening_id: str = pydantic.Field()
    """
    The ID of the associated screening.
    """

    webhook_code: str = pydantic.Field()
    """
    `STATUS_UPDATED`
    """

    webhook_type: str = pydantic.Field()
    """
    `SCREENING`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
