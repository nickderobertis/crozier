

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .question_option import QuestionOption


class QuestionInfo(UniversalBaseModel):
    question: str = pydantic.Field()
    """
    Complete question
    """

    header: str = pydantic.Field()
    """
    Very short label (max 30 chars)
    """

    options: typing.List[QuestionOption] = pydantic.Field()
    """
    Available choices
    """

    multiple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow selecting multiple choices
    """

    custom: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow typing a custom answer (default: true)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
