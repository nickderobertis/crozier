

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .violation import Violation


class Decision(UniversalBaseModel):
    enabled_rules: typing.Optional[typing.List[str]] = None
    hard_failures: typing.Optional[typing.List[Violation]] = None
    reason: typing.Optional[str] = None
    soft_failures: typing.Optional[typing.List[Violation]] = None
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
