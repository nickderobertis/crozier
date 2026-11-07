

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_name import ResourceName


class SkillManifest_Git(UniversalBaseModel):
    type: typing.Literal["git"] = "git"
    description: str
    name: ResourceName
    path: typing.Optional[str] = None
    ref: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SkillManifest_Truefoundry(UniversalBaseModel):
    type: typing.Literal["truefoundry"] = "truefoundry"
    description: str
    display_name: str
    name: str
    repository_name: str
    version: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SkillManifest = typing_extensions.Annotated[
    typing.Union[SkillManifest_Git, SkillManifest_Truefoundry], pydantic.Field(discriminator="type")
]
