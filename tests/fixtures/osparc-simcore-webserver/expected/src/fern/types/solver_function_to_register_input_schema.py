

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SolverFunctionToRegisterInputSchema_ApplicationSchemaJson(UniversalBaseModel):
    schema_class: typing.Literal["application/schema+json"] = "application/schema+json"
    schema_content: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SolverFunctionToRegisterInputSchema = SolverFunctionToRegisterInputSchema_ApplicationSchemaJson
