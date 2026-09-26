

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateBusinessRequest(UniversalBaseModel):
    name: str
    category: typing.Optional[str] = None
    address: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    website: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
