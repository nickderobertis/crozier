

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NewPasswordRequestDataAttributes(UniversalBaseModel):
    email: typing.Optional[str] = None
    password: typing.Optional[str] = None
    password_confirmation: typing.Optional[str] = None
    token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
