

import typing

from .page_post_response_data_annotations import PagePostResponseDataAnnotations
from .page_post_response_data_one import PagePostResponseDataOne
from .page_post_response_data_two import PagePostResponseDataTwo

PagePostResponseData = typing.Union[
    PagePostResponseDataAnnotations, PagePostResponseDataOne, PagePostResponseDataTwo, typing.Optional[typing.Any]
]
