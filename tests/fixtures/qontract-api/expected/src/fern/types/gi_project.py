

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GiProject(UniversalBaseModel):
    """
    Desired state for a single Glitchtip project.
    """

    event_throttle_rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    Event throttle rate (0 = no throttle)
    """

    name: str = pydantic.Field()
    """
    Project name
    """

    platform: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project platform
    """

    slug: str = pydantic.Field()
    """
    Project slug (URL-friendly identifier)
    """

    teams: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Team slugs this project belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
