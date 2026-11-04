

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsersAddonsReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the user addon entity.
    """

    user_has_auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the user has access to this user addon.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
