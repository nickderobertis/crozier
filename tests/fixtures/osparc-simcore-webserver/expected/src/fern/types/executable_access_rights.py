

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExecutableAccessRights(UniversalBaseModel):
    write: bool = pydantic.Field()
    """
    can change executable settings
    """

    execute: bool = pydantic.Field()
    """
    can run executable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
