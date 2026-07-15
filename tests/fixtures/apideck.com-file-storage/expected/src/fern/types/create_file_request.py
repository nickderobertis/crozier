

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parent_folder_id import ParentFolderId


class CreateFileRequest(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the file.
    """

    drive_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the drive to upload to.
    """

    name: str = pydantic.Field()
    """
    The name of the file.
    """

    parent_folder_id: ParentFolderId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
