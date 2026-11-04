

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AvailableSkill(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    Concise guidance for when the agent should use the skill.
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional skill metadata.
    """

    name: str = pydantic.Field()
    """
    Skill name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
