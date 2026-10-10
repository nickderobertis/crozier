

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_name import ResourceName
from .skill_type import SkillType


class CatalogSkill(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    Concise guidance for when the agent should use the skill.
    """

    name: ResourceName
    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to the skill directory within the repository. Omit to use the repository root.
    """

    ref: str = pydantic.Field()
    """
    Git ref — branch name, tag, or commit SHA.
    """

    type: SkillType
    url: str = pydantic.Field()
    """
    Full HTTPS URL of a GitHub or GitLab repository.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
