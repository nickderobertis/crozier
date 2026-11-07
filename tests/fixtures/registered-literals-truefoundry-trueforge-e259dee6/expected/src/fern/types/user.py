

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class User(UniversalBaseModel):
    display_name: str = pydantic.Field()
    """
    Human-readable name for the user.
    """

    email: str = pydantic.Field()
    """
    Email of the user.
    """

    id: str = pydantic.Field()
    """
    User id, unique within the tenant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
