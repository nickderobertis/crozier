

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ask_detect_intelligence_question_response_item_status import AskDetectIntelligenceQuestionResponseItemStatus


class AskDetectIntelligenceQuestionResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="UUID of the question"),
    ] = None
    """
    UUID of the question
    """

    detect_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the associated detection report
    """

    query: typing.Optional[str] = pydantic.Field(default=None)
    """
    The submitted question
    """

    answer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The generated answer (null until completed)
    """

    status: typing.Optional[AskDetectIntelligenceQuestionResponseItemStatus] = pydantic.Field(default=None)
    """
    Current status of the question
    """

    error_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error details when status is failed
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
