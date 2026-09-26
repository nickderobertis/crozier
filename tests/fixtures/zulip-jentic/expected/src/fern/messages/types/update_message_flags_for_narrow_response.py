

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ignored_parameters_unsupported import IgnoredParametersUnsupported


class UpdateMessageFlagsForNarrowResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    processed_count: int = pydantic.Field()
    """
    The number of messages that were within the
    update range (at most `num_before + 1 +
    num_after`).
    """

    updated_count: int = pydantic.Field()
    """
    The number of messages where the flag's
    value was changed (at most
    `processed_count`).
    """

    first_processed_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the oldest message within the
    update range, or `null` if the range was
    empty.
    """

    last_processed_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the newest message within the
    update range, or `null` if the range was
    empty.
    """

    found_oldest: bool = pydantic.Field()
    """
    Whether the update range reached backward
    far enough to include very oldest message
    matching the narrow (used by clients doing a
    bulk update to decide whether to issue
    another request anchored at
    `first_processed_id`).
    """

    found_newest: bool = pydantic.Field()
    """
    Whether the update range reached forward far
    enough to include very oldest message
    matching the narrow (used by clients doing a
    bulk update to decide whether to issue
    another request anchored at
    `last_processed_id`).
    """

    ignored_because_not_subscribed_channels: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Only present if the flag is `read` and the operation is `remove`.
    
    Zulip has an invariant that all unread messages must be in channels
    the user is subscribed to. This field will contain a list of the
    channels whose messages were skipped to mark as unread because the
    user is not subscribed to them.
    
    **Changes**: New in Zulip 10.0 (feature level 355).
    """

    ignored_parameters_unsupported: typing.Optional[IgnoredParametersUnsupported] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
