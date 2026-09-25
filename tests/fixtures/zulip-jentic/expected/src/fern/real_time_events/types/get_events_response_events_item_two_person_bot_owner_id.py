

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonBotOwnerId(UniversalBaseModel):
    """
    When the owner of a bot changes.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user/bot whose owner has changed.
    """

    bot_owner_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the new bot owner.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
