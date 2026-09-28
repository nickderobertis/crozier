

import typing

from ...types.expectation import Expectation
from ...types.http_request import HttpRequest
from ...types.http_request_and_http_response import HttpRequestAndHttpResponse

PutMockserverRetrieveResponse = typing.Union[
    typing.List[Expectation], typing.List[HttpRequest], typing.List[HttpRequestAndHttpResponse]
]
