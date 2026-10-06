

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokensResponse(UniversalBaseModel):
    """
    Выдача токенов
    """

    access_token: str = pydantic.Field()
    """
    Jwt для авторизации
    """

    refresh_token: str = pydantic.Field()
    """
    Рефреш токен для обнавления jwt
    """

    access_token_expires: int = pydantic.Field()
    """
    Время, сколько активен jwt
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
