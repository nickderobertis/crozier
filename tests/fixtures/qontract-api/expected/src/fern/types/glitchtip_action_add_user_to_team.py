

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionAddUserToTeam(UniversalBaseModel):
    """
    Action: Add a user to a team.
    """

    email: str = pydantic.Field()
    """
    User email
    """

    instance: str = pydantic.Field()
    """
    Glitchtip instance name
    """

    organization: str = pydantic.Field()
    """
    Organization name
    """

    pk: typing.Optional[int] = pydantic.Field(default=None)
    """
    User primary key (None when user is being invited in the same run)
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
