

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_form_submissions_response_submissions_item_responses_item_answer import (
    ListFormSubmissionsResponseSubmissionsItemResponsesItemAnswer,
)


class ListFormSubmissionsResponseSubmissionsItemResponsesItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Response ID
    """

    form_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="formId"), pydantic.Field(alias="formId", description="Form ID")
    ]
    """
    Form ID
    """

    question_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="questionId"), pydantic.Field(alias="questionId", description="Question ID")
    ]
    """
    Question ID
    """

    respondent_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="respondentId"), pydantic.Field(alias="respondentId", description="Respondent ID")
    ]
    """
    Respondent ID
    """

    submission_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="submissionId"),
        pydantic.Field(alias="submissionId", description="Submission ID"),
    ] = None
    """
    Submission ID
    """

    session_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="sessionUuid"), pydantic.Field(alias="sessionUuid", description="Session UUID")
    ]
    """
    Session UUID
    """

    answer: typing.Optional[ListFormSubmissionsResponseSubmissionsItemResponsesItemAnswer] = pydantic.Field(
        default=None
    )
    """
    The answer value for this question. Type varies based on question type.
    """

    formatted_answer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="formattedAnswer"),
        pydantic.Field(
            alias="formattedAnswer", description="Formatted answer (e.g., for number inputs with custom formatting)"
        ),
    ] = None
    """
    Formatted answer (e.g., for number inputs with custom formatting)
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the response was created"),
    ]
    """
    When the response was created
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="When the response was last updated"),
    ]
    """
    When the response was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
