

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .scopes import Scopes


class ScopesNullable(Scopes):
    """
    The scopes object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
