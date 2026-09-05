

import typing

from .chat_completion_content_part_image_with_title_image_url_detail_one import (
    ChatCompletionContentPartImageWithTitleImageUrlDetailOne,
)
from .chat_completion_content_part_image_with_title_image_url_detail_two import (
    ChatCompletionContentPartImageWithTitleImageUrlDetailTwo,
)
from .chat_completion_content_part_image_with_title_image_url_detail_zero import (
    ChatCompletionContentPartImageWithTitleImageUrlDetailZero,
)

ChatCompletionContentPartImageWithTitleImageUrlDetail = typing.Union[
    ChatCompletionContentPartImageWithTitleImageUrlDetailZero,
    ChatCompletionContentPartImageWithTitleImageUrlDetailOne,
    ChatCompletionContentPartImageWithTitleImageUrlDetailTwo,
]
