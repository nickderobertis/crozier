

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_form_submission_response_submission_responses_item import GetFormSubmissionResponseSubmissionResponsesItem


class GetFormSubmissionResponseSubmission(UniversalBaseModel):
    """
    The form submission with responses
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Submission ID
    """

    form_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="formId"), pydantic.Field(alias="formId", description="Form ID")
    ] = None
    """
    Form ID
    """

    is_completed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCompleted"),
        pydantic.Field(alias="isCompleted", description="Whether the submission is completed"),
    ] = None
    """
    Whether the submission is completed
    """

    submitted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="submittedAt"),
        pydantic.Field(alias="submittedAt", description="When the submission was submitted"),
    ] = None
    """
    When the submission was submitted
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the submission was created"),
    ] = None
    """
    When the submission was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="When the submission was last updated"),
    ] = None
    """
    When the submission was last updated
    """

    responses: typing.Optional[typing.List[GetFormSubmissionResponseSubmissionResponsesItem]] = pydantic.Field(
        default=None
    )
    """
    List of responses to form questions. Note: Only questions that have been answered will appear in this array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
