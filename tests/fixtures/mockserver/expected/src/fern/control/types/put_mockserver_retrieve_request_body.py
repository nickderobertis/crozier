

import typing

from ...types.expectation_id import ExpectationId
from ...types.request_definition import RequestDefinition

PutMockserverRetrieveRequestBody = typing.Union[RequestDefinition, ExpectationId]
