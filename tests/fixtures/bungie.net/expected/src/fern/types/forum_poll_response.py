

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .forum_poll_result import ForumPollResult


class ForumPollResponse(UniversalBaseModel):
    results: typing.Optional[typing.List[ForumPollResult]] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None
    total_votes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalVotes"), pydantic.Field(alias="totalVotes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
