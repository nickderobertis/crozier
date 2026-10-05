

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionUpdateUserRole(UniversalBaseModel):
    """
    Action: Update a user's role in an organization.
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

    pk: int = pydantic.Field()
    """
    User primary key (resolved at planning time)
    """

    role: str = pydantic.Field()
    """
    New role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
