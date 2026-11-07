

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .files_sharing_sharee_circle_all_of_value_all_of import FilesSharingShareeCircleAllOfValueAllOf
from .files_sharing_sharee_value import FilesSharingShareeValue


class FilesSharingShareeCircleAllOfValue(FilesSharingShareeValue, FilesSharingShareeCircleAllOfValueAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
