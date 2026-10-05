

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GithubOwnerActionAddOwner(UniversalBaseModel):
    """
    Action: Add a user as an org admin (owner).

    Note: Owner removal is intentionally NOT supported. The integration only
    adds owners and never removes them, preserving the behavior of the original
    github-owners reconcile integration. This is a deliberate safety decision —
    removing org admins is a high-impact operation that requires explicit manual
    review rather than automated removal.
    """

    org_name: str = pydantic.Field()
    """
    GitHub organization name
    """

    username: str = pydantic.Field()
    """
    GitHub username to add as org admin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
