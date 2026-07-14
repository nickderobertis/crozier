

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResolveWebhookResponse(UniversalBaseModel):
    request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the request received
    """

    status: str = pydantic.Field()
    """
    HTTP Response Status
    """

    status_code: int = pydantic.Field()
    """
    HTTP Response Status Code
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO Datetime webhook event was received
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
