

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .draft_type import DraftType


class Draft(UniversalBaseModel):
    """
    A dictionary for representing a message draft.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the draft. It will only used whenever the drafts are
    fetched. This field should not be specified when the draft is being
    created or edited.
    """

    type: DraftType = pydantic.Field()
    """
    The type of the draft. Either unaddressed (empty string), `"stream"`,
    or `"private"` (for one-on-one and group direct messages).
    """

    to: typing.List[int] = pydantic.Field()
    """
    An array of the tentative target audience IDs. For channel
    messages, this should contain exactly 1 ID, the ID of the
    target channel. For direct messages, this should be an array
    of target user IDs. For unaddressed drafts, this is ignored,
    and clients should send an empty array.
    """

    topic: str = pydantic.Field()
    """
    For channel message drafts, the tentative topic name. For direct
    or unaddressed messages, this will be ignored and should ideally
    be the empty string. Should not contain null bytes.
    """

    content: str = pydantic.Field()
    """
    The body of the draft. Should not contain null bytes.
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    A Unix timestamp (seconds only) representing when the draft was
    last edited. When creating a draft, this key need not be present
    and it will be filled in automatically by the server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
