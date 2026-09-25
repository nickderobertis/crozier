

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemEmojiIdData(UniversalBaseModel):
    """
    And object containing the properties that have changed.
    """

    deactivated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the custom emoji has been deactivated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
