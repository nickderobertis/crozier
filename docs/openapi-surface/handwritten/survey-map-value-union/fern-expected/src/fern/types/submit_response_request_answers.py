

import typing

from .submit_response_request_answers_zero_value import SubmitResponseRequestAnswersZeroValue

SubmitResponseRequestAnswers = typing.Union[
    typing.Dict[str, typing.Optional[SubmitResponseRequestAnswersZeroValue]], str
]
