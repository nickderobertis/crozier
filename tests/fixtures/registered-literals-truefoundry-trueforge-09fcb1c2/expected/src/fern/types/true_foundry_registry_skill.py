

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TrueFoundryRegistrySkill(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    Concise guidance for when the agent should use the skill.
    """

    display_name: str
    name: str
    repository_name: str = pydantic.Field()
    """
    Repo where the skill is registered.
    """

    version: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
