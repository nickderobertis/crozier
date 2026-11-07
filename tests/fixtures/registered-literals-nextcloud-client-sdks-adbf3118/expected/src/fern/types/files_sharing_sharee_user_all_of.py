

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .files_sharing_sharee_user_all_of_status import FilesSharingShareeUserAllOfStatus
from .files_sharing_sharee_value import FilesSharingShareeValue


class FilesSharingShareeUserAllOf(UniversalBaseModel):
    subline: str
    icon: str
    share_with_display_name_unique: typing_extensions.Annotated[
        str, FieldMetadata(alias="shareWithDisplayNameUnique"), pydantic.Field(alias="shareWithDisplayNameUnique")
    ]
    status: FilesSharingShareeUserAllOfStatus
    value: FilesSharingShareeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
