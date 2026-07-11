

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Account(UniversalBaseModel):
    id: typing.Optional[str] = None
    username: str
    password: typing.Optional[str] = None
    age: typing.Optional[int] = None
    balance: typing.Optional[float] = None
    tags: typing.Optional[typing.List[str]] = None
    legacy_id: typing.Optional[int] = None
    role: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
