

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionUpdateProject(UniversalBaseModel):
    """
    Action: Update a project's settings.
    """

    event_throttle_rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    Event throttle rate (0 = unlimited)
    """

    instance: str = pydantic.Field()
    """
    Glitchtip instance name
    """

    name: str = pydantic.Field()
    """
    Project name
    """

    organization: str = pydantic.Field()
    """
    Organization name
    """

    platform: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project platform
    """

    project_slug: str = pydantic.Field()
    """
    Project slug
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
