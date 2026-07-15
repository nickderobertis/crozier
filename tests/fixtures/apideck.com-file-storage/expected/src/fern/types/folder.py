

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .linked_folder import LinkedFolder
from .owner import Owner
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Folder(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the folder
    """

    id: typing.Optional[Id] = None
    name: str = pydantic.Field()
    """
    The name of the folder
    """

    owner: typing.Optional[Owner] = None
    parent_folders: typing.List[LinkedFolder] = pydantic.Field()
    """
    The parent folders of the file, starting from the root
    """

    parent_folders_complete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the list of parent folder is complete. Some connectors only return the direct parent of a folder
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full path of the folder (includes the folder name)
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the folder in bytes
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
