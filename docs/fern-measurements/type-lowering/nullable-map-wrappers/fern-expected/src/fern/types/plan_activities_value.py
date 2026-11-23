

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PlanActivitiesValue_Inline(UniversalBaseModel):
    kind: typing.Literal["inline"] = "inline"
    body: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PlanActivitiesValue_Git(UniversalBaseModel):
    kind: typing.Literal["git"] = "git"
    repo: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PlanActivitiesValue = typing_extensions.Annotated[
    typing.Union[PlanActivitiesValue_Inline, PlanActivitiesValue_Git], pydantic.Field(discriminator="kind")
]
