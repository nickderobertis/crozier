

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .u_folder import UFolder


class UFolderUpdate(UniversalBaseModel):
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    folder_update: typing_extensions.Annotated[
        UFolder, FieldMetadata(alias="folderUpdate"), pydantic.Field(alias="folderUpdate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
