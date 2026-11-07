

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_transcript_questions_response_items_item import ListTranscriptQuestionsResponseItemsItem


class ListTranscriptQuestionsResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    items: typing.Optional[typing.List[ListTranscriptQuestionsResponseItemsItem]] = None
    meta: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
