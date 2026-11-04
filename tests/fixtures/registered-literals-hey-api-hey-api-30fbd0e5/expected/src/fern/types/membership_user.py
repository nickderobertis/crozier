

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MembershipUser(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the user
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username of the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
