

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1DialingPermissionsDialingPermissionsSettings(UniversalBaseModel):
    dialing_permissions_inheritance: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if the sub-account will inherit voice dialing permissions from the Master Project; otherwise `false`.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of this resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
