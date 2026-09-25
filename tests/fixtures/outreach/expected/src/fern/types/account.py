

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_attributes import AccountAttributes


class Account(UniversalBaseModel):
    type: typing.Optional[str] = None
    id: typing.Optional[int] = None
    attributes: typing.Optional[AccountAttributes] = None
    relationships: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
