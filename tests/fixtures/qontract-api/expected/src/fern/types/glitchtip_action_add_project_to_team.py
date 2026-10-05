

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionAddProjectToTeam(UniversalBaseModel):
    """
    Action: Add a project to a team.
    """

    instance: str = pydantic.Field()
    """
    Glitchtip instance name
    """

    organization: str = pydantic.Field()
    """
    Organization name
    """

    project_slug: str = pydantic.Field()
    """
    Project slug
    """

    team_slug: str = pydantic.Field()
    """
    Team slug
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
