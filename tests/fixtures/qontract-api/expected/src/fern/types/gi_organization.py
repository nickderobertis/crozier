

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gi_project import GiProject
from .glitchtip_team import GlitchtipTeam
from .glitchtip_user import GlitchtipUser


class GiOrganization(UniversalBaseModel):
    """
    Desired state for a single Glitchtip organization.
    """

    name: str = pydantic.Field()
    """
    Organization name
    """

    projects: typing.Optional[typing.List[GiProject]] = pydantic.Field(default=None)
    """
    Desired projects in this organization
    """

    teams: typing.Optional[typing.List[GlitchtipTeam]] = pydantic.Field(default=None)
    """
    Desired teams in this organization
    """

    users: typing.Optional[typing.List[GlitchtipUser]] = pydantic.Field(default=None)
    """
    Desired members of this organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
