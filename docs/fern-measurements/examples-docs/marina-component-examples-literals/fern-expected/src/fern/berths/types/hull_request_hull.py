

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HullRequestHull_Steel(UniversalBaseModel):
    material: typing.Literal["steel"] = "steel"
    length_m: int
    beam_m: int
    draft_cm: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class HullRequestHull_Timber(UniversalBaseModel):
    material: typing.Literal["timber"] = "timber"
    length_m: int
    beam_m: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


HullRequestHull = typing_extensions.Annotated[
    typing.Union[HullRequestHull_Steel, HullRequestHull_Timber], pydantic.Field(discriminator="material")
]
