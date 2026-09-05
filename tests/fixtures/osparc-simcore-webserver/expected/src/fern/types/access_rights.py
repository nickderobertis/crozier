

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccessRights(UniversalBaseModel):
    read: bool = pydantic.Field()
    """
    has read access
    """

    write: bool = pydantic.Field()
    """
    has write access
    """

    delete: bool = pydantic.Field()
    """
    has deletion rights
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
