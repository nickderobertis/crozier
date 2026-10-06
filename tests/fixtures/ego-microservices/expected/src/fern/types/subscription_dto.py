

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubscriptionDto(UniversalBaseModel):
    """
    Модель подписок/подписчиков
    """

    user_id: int = pydantic.Field()
    """
    Айди подпичсика
    """

    first_name: str = pydantic.Field()
    """
    Имя пользователя
    """

    last_name: str = pydantic.Field()
    """
    Фамилия пользователя
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    Аватар пользователя
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Показывает удален ли пользователь
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
