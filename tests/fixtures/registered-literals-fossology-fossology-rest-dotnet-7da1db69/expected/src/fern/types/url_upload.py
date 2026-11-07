

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UrlUpload(UniversalBaseModel):
    """
    To create an upload from a URL
    """

    url: str = pydantic.Field()
    """
    URL for file/folder to be uploaded
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Viewable name for this file or directory
    """

    accept: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated lists of file name suffixes or patterns to accpet
    """

    reject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated lists of file name suffixes or patterns to reject
    """

    max_recursion_depth: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxRecursionDepth"),
        pydantic.Field(alias="maxRecursionDepth", description="Maximum recursion depth for folders (0 for infinite)"),
    ] = None
    """
    Maximum recursion depth for folders (0 for infinite)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
