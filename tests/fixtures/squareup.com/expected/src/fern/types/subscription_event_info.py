

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .info_code import InfoCode


class SubscriptionEventInfo(UniversalBaseModel):
    """
    Provides information about the subscription event.
    """

    code: typing.Optional[InfoCode] = None
    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable explanation for the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
