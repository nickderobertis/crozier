

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_folder_restore import V2TableFolderRestore


class V2RestoreTableFolderResponse(UniversalBaseModel):
    """
    The restored table folder and the counts of items it brought back.
    """

    data: V2TableFolderRestore = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
