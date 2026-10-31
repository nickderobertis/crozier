

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PickUserNameOrEmailOrUsernameOrNewpassword(UniversalBaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """

    name: str
    email: str
    username: str
    newpassword: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
