

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ignored_parameters_unsupported import IgnoredParametersUnsupported


class DeleteAvatarResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the current user's profile picture, which
    now uses the organization's default style for profile
    pictures. Its format depends on whether that style is
    the default abstract design or Gravatar.
    """

    ignored_parameters_unsupported: typing.Optional[IgnoredParametersUnsupported] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
