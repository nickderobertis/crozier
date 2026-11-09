

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .upload import Upload


class SearchResults(UniversalBaseModel):
    upload: typing.Optional[Upload] = None
    upload_tree_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uploadTreeId"),
        pydantic.Field(alias="uploadTreeId", description="Upload tree ID"),
    ] = None
    """
    Upload tree ID
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filename of the treeItem
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
