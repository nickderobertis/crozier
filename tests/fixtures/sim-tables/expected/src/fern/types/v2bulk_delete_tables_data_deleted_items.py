

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2BulkDeleteTablesDataDeletedItems(UniversalBaseModel):
    """
    Totals across the explicit archives and every folder cascade they triggered.
    """

    tables: int = pydantic.Field()
    """
    Tables archived, including folder cascades.
    """

    folders: int = pydantic.Field()
    """
    Folders deleted, including nested folders.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
