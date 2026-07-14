

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .policy_rule import PolicyRule


class Policy(UniversalBaseModel):
    comment: typing.Optional[str] = None
    id: str
    name: typing.Optional[str] = None
    rules: typing.Optional[typing.List[PolicyRule]] = None
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
