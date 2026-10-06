

import typing

from .bad_request_error_body_message_one_item import BadRequestErrorBodyMessageOneItem

BadRequestErrorBodyMessage = typing.Union[str, typing.List[BadRequestErrorBodyMessageOneItem]]
