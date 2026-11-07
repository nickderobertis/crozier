

import typing

from .expression_assertion import ExpressionAssertion
from .predicate_assertion import PredicateAssertion

Assertion = typing.Union[ExpressionAssertion, PredicateAssertion]
