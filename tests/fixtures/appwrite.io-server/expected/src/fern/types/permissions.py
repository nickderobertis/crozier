

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Permissions(UniversalBaseModel):
    """
    Permissions
    """

    read: typing.List[str] = pydantic.Field()
    """
    Read permissions.
    """

    write: typing.List[str] = pydantic.Field()
    """
    Write permissions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
