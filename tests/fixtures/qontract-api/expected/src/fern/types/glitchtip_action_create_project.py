

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionCreateProject(UniversalBaseModel):
    """
    Action: Create a project in an organization.
    """

    event_throttle_rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    Event throttle rate (0 = unlimited)
    """

    instance: str = pydantic.Field()
    """
    Glitchtip instance name
    """

    organization: str = pydantic.Field()
    """
    Organization name
    """

    platform: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project platform
    """

    project_name: str = pydantic.Field()
    """
    Project name
    """

    teams: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Team slugs to associate with the project (first team used for creation)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
