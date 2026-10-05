

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .glitchtip_user import GlitchtipUser


class GlitchtipTeam(UniversalBaseModel):
    """
    Desired state for a single Glitchtip team.
    """

    name: str = pydantic.Field()
    """
    Team name (slug will be derived)
    """

    users: typing.Optional[typing.List[GlitchtipUser]] = pydantic.Field(default=None)
    """
    Desired members of this team
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
