

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lemur_question_context import LemurQuestionContext


class LemurQuestion(UniversalBaseModel):
    question: str = pydantic.Field()
    """
    The question you wish to ask. For more complex questions use default model.
    """

    context: typing.Optional[LemurQuestionContext] = pydantic.Field(default=None)
    """
    Any context about the transcripts you wish to provide. This can be a string or any object.
    """

    answer_format: typing.Optional[str] = pydantic.Field(default=None)
    """
    How you want the answer to be returned. This can be any text. Can't be used with answer_options. Examples: "short sentence", "bullet points"
    """

    answer_options: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    What discrete options to return. Useful for precise responses. Can't be used with answer_format. Example: ["Yes", "No"]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
