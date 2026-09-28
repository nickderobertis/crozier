

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2DeleteTableFolderDataDeletedItems(UniversalBaseModel):
    """
    Deleted resource counts.
    """

    folders: int = pydantic.Field()
    """
    Number of deleted folders.
    """

    tables: int = pydantic.Field()
    """
    Number of deleted tables.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
