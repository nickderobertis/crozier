

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PasswordResetErrorResponse(UniversalBaseModel):
    """
    Discriminated error envelope emitted by writePasswordResetError.
    `code` is one of `reset_token_invalid` / `reset_token_expired` /
    `password_too_weak`; `message` is a server-localized RU string the
    frontend renders as-is when no i18n catalog entry matches.
    """

    code: str
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
