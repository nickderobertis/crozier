

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.question import Question
from .get_form_submission_response_submission import GetFormSubmissionResponseSubmission


class GetFormSubmissionResponse(UniversalBaseModel):
    questions: typing.Optional[typing.List[Question]] = pydantic.Field(default=None)
    """
    List of form questions with their fields
    """

    submission: typing.Optional[GetFormSubmissionResponseSubmission] = pydantic.Field(default=None)
    """
    The form submission with responses
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
