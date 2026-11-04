

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_capability import SandboxCapability
from .settings_capability import SettingsCapability
from .skill_capability import SkillCapability
from .web_search_capability import WebSearchCapability


class CapabilitiesData(UniversalBaseModel):
    sandbox: SandboxCapability
    settings: SettingsCapability
    skill: SkillCapability
    web_search: WebSearchCapability

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
