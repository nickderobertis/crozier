

import typing

from .failed_assertion import FailedAssertion
from .successful_assertion import SuccessfulAssertion

AssertionResult = typing.Union[FailedAssertion, SuccessfulAssertion]
