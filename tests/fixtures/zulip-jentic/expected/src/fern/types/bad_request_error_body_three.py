

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyThree(UniversalBaseModel):
    """
    An example JSON error response for when the message was rejected because
    the message contains a topic wildcard mention, but the user doesn't have
    permission to use such a mention in this topic as the user is not present
    in `can_mention_many_users_group` and the topic contains a large number
    of participants.

    **Changes**: New in Zulip 8.0 (feature level 229). Previously,
    `wildcard_mention_policy` was not enforced for topic mentions.
    """

    result: typing.Any
    msg: typing.Any
    code: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
