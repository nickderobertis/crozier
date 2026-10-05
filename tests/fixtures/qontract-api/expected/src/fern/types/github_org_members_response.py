

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GithubOrgMembersResponse(UniversalBaseModel):
    """
    Response with all members of a GitHub organization.
    """

    members: typing.List[str] = pydantic.Field()
    """
    GitHub usernames (original case) of all organization members
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
