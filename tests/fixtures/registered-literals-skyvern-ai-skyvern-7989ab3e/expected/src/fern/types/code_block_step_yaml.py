

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeBlockStepYaml(UniversalBaseModel):
    description: typing.Optional[str] = None
    action_type: typing.Optional[str] = None
    line_start: typing.Optional[int] = None
    line_end: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
