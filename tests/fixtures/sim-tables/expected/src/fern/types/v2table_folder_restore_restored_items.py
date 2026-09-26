

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2TableFolderRestoreRestoredItems(UniversalBaseModel):
    """
    What the restore brought back.
    """

    folders: int = pydantic.Field()
    """
    Folders restored, including the one addressed.
    """

    tables: int = pydantic.Field()
    """
    Tables restored inside the folder tree.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
