

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .skill_card_response_scope import SkillCardResponseScope
from .skill_card_response_trust import SkillCardResponseTrust


class SkillCardResponse(UniversalBaseModel):
    """
    Bounded Skill discovery metadata — no instructions body.
    """

    id: str
    name: str
    description: str
    scope: SkillCardResponseScope
    version: str
    trust: SkillCardResponseTrust
    affordances: typing.List[str]
    resources_available: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
