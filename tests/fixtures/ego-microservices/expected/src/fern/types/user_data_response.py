

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserDataResponse(UniversalBaseModel):
    """
    Модель ответа получения пользоватлея
    """

    user_id: int = pydantic.Field()
    """
    Айди профиля
    """

    first_name: str = pydantic.Field()
    """
    Имя пользователя
    """

    last_name: str = pydantic.Field()
    """
    Фамилия пользователя
    """

    gender: str = pydantic.Field()
    """
    Пол пользователя
    """

    birthday: dt.date = pydantic.Field()
    """
    День рождения пользователя
    """

    avatar_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Аватарка пользователя
    """

    count_of_subscriptions: int = pydantic.Field()
    """
    Кол-во подписок
    """

    count_of_subscribers: int = pydantic.Field()
    """
    Кол-во подписчиков
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Пользователь удален/неудален
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
