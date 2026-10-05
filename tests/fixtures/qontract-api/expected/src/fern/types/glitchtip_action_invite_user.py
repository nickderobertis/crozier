

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionInviteUser(UniversalBaseModel):
    """
    Action: Invite a user to an organization.
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

    role: str = pydantic.Field()
    """
    Organization role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
