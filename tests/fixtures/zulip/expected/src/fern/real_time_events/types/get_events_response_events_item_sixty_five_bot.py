

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemSixtyFiveBot(UniversalBaseModel):
    """
    Object containing details about the deactivated bot.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the deactivated bot.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
