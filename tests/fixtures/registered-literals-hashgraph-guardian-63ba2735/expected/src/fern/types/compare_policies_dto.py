

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComparePoliciesDto(UniversalBaseModel):
    blocks: typing.Dict[str, typing.Any]
    groups: typing.Dict[str, typing.Any]
    left: typing.Dict[str, typing.Any]
    right: typing.Dict[str, typing.Any]
    roles: typing.Dict[str, typing.Any]
    tokens: typing.Dict[str, typing.Any]
    topics: typing.Dict[str, typing.Any]
    total: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
