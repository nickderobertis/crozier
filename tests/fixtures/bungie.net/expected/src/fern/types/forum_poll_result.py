

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ForumPollResult(UniversalBaseModel):
    answer_slot: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="answerSlot"), pydantic.Field(alias="answerSlot")
    ] = None
    answer_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="answerText"), pydantic.Field(alias="answerText")
    ] = None
    last_vote_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastVoteDate"), pydantic.Field(alias="lastVoteDate")
    ] = None
    requesting_user_voted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requestingUserVoted"), pydantic.Field(alias="requestingUserVoted")
    ] = None
    votes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
