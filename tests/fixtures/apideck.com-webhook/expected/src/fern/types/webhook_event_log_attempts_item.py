

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookEventLogAttemptsItem(UniversalBaseModel):
    execution_attempt: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of attempts webhook endpoint was called before a success was returned or eventually failed
    """

    status_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP Status code that was returned.
    """

    success: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the request was successful.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO Date and time when the request was made.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
