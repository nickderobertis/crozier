

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2Folder(UniversalBaseModel):
    """
    A canonical workspace folder.
    """

    name: str = pydantic.Field()
    """
    Folder name.
    """

    path: str = pydantic.Field()
    """
    Canonical folder path used as the public folder identifier.
    """

    parent_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="parentPath"),
        pydantic.Field(alias="parentPath", description="Canonical parent path; `/` is the root."),
    ]
    """
    Canonical parent path; `/` is the root.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 timestamp when the folder was created."),
    ]
    """
    ISO 8601 timestamp when the folder was created.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 timestamp when the folder was last updated."),
    ]
    """
    ISO 8601 timestamp when the folder was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
