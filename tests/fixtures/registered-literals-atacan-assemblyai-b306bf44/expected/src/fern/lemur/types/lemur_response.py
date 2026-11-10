

import typing

from .lemur_question_answer_response import LemurQuestionAnswerResponse
from .lemur_string_response import LemurStringResponse

LemurResponse = typing.Union[LemurStringResponse, LemurQuestionAnswerResponse]
