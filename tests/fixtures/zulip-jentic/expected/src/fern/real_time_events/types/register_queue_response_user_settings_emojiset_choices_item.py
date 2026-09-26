

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseUserSettingsEmojisetChoicesItem(UniversalBaseModel):
    """
    Object describing a emoji set.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key or the name of the emoji set which will be the value
    of `emojiset` if this emoji set is chosen.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text describing the emoji set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
