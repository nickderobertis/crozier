

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .glitchtip_project_alert import GlitchtipProjectAlert


class GlitchtipProject(UniversalBaseModel):
    """
    Desired state for a single Glitchtip project's alerts.
    """

    alerts: typing.Optional[typing.List[GlitchtipProjectAlert]] = pydantic.Field(default=None)
    """
    Desired alerts for this project
    """

    name: str = pydantic.Field()
    """
    Project name
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project slug (URL-friendly identifier). Defaults to slugified name if not provided.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
