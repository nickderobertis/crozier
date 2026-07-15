

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Contact(UniversalBaseModel):
    email: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    id: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    linked_in: typing.Optional[str] = None
    name: str
    role: typing.Optional[str] = None
    twitter: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
