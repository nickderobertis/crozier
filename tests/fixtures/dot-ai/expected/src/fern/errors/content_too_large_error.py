

import typing

from ..core.api_error import ApiError
from ..types.prompts_sources_post_error413 import PromptsSourcesPostError413


class ContentTooLargeError(ApiError):
    def __init__(self, body: PromptsSourcesPostError413, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=413, headers=headers, body=body)
