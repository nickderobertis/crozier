

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostDto(UniversalBaseModel):
    """
    Базовый класс DTO
    """

    post_id: str = pydantic.Field()
    """
    Айди поста
    """

    creator_id: int = pydantic.Field()
    """
    Айди создателя поста
    """

    text_content: str = pydantic.Field()
    """
    Текст поста
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Время создания поста
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
