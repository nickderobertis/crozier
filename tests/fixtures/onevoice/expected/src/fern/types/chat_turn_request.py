

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_turn_request_selected_platforms_item import ChatTurnRequestSelectedPlatformsItem


class ChatTurnRequest(UniversalBaseModel):
    message: typing.Optional[str] = None
    model: typing.Optional[str] = None
    locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    BCP-47 language tag (e.g. "ru", "en") for the LLM response language. Takes precedence over the Accept-Language header, which browsers cannot set on fetch. Empty falls back to Accept-Language.
    """

    selected_platforms: typing.Optional[typing.List[ChatTurnRequestSelectedPlatformsItem]] = pydantic.Field(
        default=None
    )
    """
    Optional closed guided-compose publication scope. Omission preserves ordinary chat behavior; when present, only these freshly active platform integrations may be offered or dispatched.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
