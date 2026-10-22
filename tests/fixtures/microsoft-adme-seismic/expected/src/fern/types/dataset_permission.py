

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetPermission(UniversalBaseModel):
    read: bool = pydantic.Field()
    """
    True if the user has read permission on the dataset.
    """

    write: bool = pydantic.Field()
    """
    True if the user has write permission on the dataset.
    """

    delete: bool = pydantic.Field()
    """
    True if the user has delete permission on the dataset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
