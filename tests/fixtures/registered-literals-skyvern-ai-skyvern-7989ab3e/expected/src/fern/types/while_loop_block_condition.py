

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WhileLoopBlockCondition_Jinja2Template(UniversalBaseModel):
    criteria_type: typing.Literal["jinja2_template"] = "jinja2_template"
    expression: str
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WhileLoopBlockCondition_Prompt(UniversalBaseModel):
    criteria_type: typing.Literal["prompt"] = "prompt"
    expression: str
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WhileLoopBlockCondition = typing_extensions.Annotated[
    typing.Union[WhileLoopBlockCondition_Jinja2Template, WhileLoopBlockCondition_Prompt],
    pydantic.Field(discriminator="criteria_type"),
]
