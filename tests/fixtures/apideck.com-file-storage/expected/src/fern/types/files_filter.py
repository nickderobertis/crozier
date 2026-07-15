

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FilesFilter(UniversalBaseModel):
    drive_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the drive to filter on
    """

    folder_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the folder to filter on. The root folder has an alias "root"
    """

    shared: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Only return files and folders that are shared
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
