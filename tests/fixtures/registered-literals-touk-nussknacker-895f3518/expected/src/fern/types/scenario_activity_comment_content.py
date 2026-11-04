

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScenarioActivityCommentContent_Available(UniversalBaseModel):
    status: typing.Literal["AVAILABLE"] = "AVAILABLE"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ScenarioActivityCommentContent_NotAvailable(UniversalBaseModel):
    status: typing.Literal["NOT_AVAILABLE"] = "NOT_AVAILABLE"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ScenarioActivityCommentContent = typing_extensions.Annotated[
    typing.Union[ScenarioActivityCommentContent_Available, ScenarioActivityCommentContent_NotAvailable],
    pydantic.Field(discriminator="status"),
]
