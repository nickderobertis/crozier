

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DevListUsersResponseDirectUsersItem(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the dev user.
    """

    realm_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the dev user's organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
