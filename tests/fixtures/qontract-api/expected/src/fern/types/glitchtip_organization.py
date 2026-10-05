

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .glitchtip_project import GlitchtipProject


class GlitchtipOrganization(UniversalBaseModel):
    """
    Desired state for a single Glitchtip organization's projects.
    """

    name: str = pydantic.Field()
    """
    Organization name
    """

    projects: typing.Optional[typing.List[GlitchtipProject]] = pydantic.Field(default=None)
    """
    Projects within this organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
