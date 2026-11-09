

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from .lemur_base_params import LemurBaseParams
from .lemur_question import LemurQuestion


class LemurQuestionAnswerParams(LemurBaseParams):
    questions: typing.List[LemurQuestion] = pydantic.Field()
    """
    A list of questions to ask
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
