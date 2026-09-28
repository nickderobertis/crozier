

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2delete_table_folder_data import V2DeleteTableFolderData


class V2DeleteTableFolderResponse(UniversalBaseModel):
    """
    Folder deletion acknowledgement and deleted resource counts.
    """

    data: V2DeleteTableFolderData = pydantic.Field()
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
