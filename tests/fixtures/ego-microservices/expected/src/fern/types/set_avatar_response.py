

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SetAvatarResponse(UniversalBaseModel):
    """
    Модель ответа отпарвки данных об аватарке
    """

    avatar_id: str = pydantic.Field()
    """
    Айди файла
    """

    avatar_type: str = pydantic.Field()
    """
    Формат файла
    """

    avatar_user_id: int = pydantic.Field()
    """
    Айди пользователя
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
