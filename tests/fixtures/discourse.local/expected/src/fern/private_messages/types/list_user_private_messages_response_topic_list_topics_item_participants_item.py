

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUserPrivateMessagesResponseTopicListTopicsItemParticipantsItem(UniversalBaseModel):
    description: typing.Optional[str] = None
    extras: typing.Optional[str] = None
    primary_group_id: typing.Optional[str] = None
    user_id: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
