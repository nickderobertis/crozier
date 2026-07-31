

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1Deactivation(UniversalBaseModel):
    redirect_to: typing.Optional[str] = pydantic.Field(default=None)
    """
    Returns an authenticated url that redirects to a file containing the deactivated numbers for the requested day. This url is valid for up to two minutes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
