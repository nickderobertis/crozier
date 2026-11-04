

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsUsersListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the user entity.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the user's profile page on the OSF.
    """

    profile_image: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the user's profile image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
