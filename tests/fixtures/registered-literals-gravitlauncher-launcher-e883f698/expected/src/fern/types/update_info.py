

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hashed_dir import HashedDir


class UpdateInfo(UniversalBaseModel):
    """
    Update information for a specific named directory.
    """

    dir: HashedDir
    base_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="baseUrl"),
        pydantic.Field(alias="baseUrl", description="Base URL from which update files are downloaded."),
    ]
    """
    Base URL from which update files are downloaded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
