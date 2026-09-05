

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PatchOrganizationMembersRemoveUsers(UniversalBaseModel):
    """
    Users to remove from the organization
    """

    ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of users to remove
    """

    emails: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Emails of users to remove
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
