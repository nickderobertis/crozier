

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserStatus(UniversalBaseModel):
    """
    Observed user state derived by the application.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Public permalink of the user's profile or author page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
