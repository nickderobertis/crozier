

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .files_sharing_sharee_circle_all_of_value import FilesSharingShareeCircleAllOfValue


class FilesSharingShareeCircleAllOf(UniversalBaseModel):
    share_with_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="shareWithDescription"), pydantic.Field(alias="shareWithDescription")
    ]
    value: FilesSharingShareeCircleAllOfValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
