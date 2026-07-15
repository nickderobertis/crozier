

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookConfigRead(UniversalBaseModel):
    """
    the readable info for a webhook config; omits sensitive info e.g. auth token
    """

    id: str
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    human-readable name e.g. for display in UI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
