

import typing

from .post_a2a_request_params_history_length import PostA2ARequestParamsHistoryLength
from .post_a2a_request_params_message import PostA2ARequestParamsMessage
from .post_a2a_request_params_two import PostA2ARequestParamsTwo

PostA2ARequestParams = typing.Union[
    PostA2ARequestParamsMessage, PostA2ARequestParamsHistoryLength, PostA2ARequestParamsTwo
]
