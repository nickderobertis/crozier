

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2LogFile(UniversalBaseModel):
    """
    A file produced by the run this log records.
    """

    id: str = pydantic.Field()
    """
    Identifier to address this file by on the download endpoint.
    """

    name: str = pydantic.Field()
    """
    File name, including its extension.
    """

    size: int = pydantic.Field()
    """
    File size in bytes.
    """

    type: str = pydantic.Field()
    """
    MIME type recorded for the file.
    """

    download_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="downloadPath"),
        pydantic.Field(
            alias="downloadPath", description="Path to fetch this file's bytes from, relative to the API host."
        ),
    ]
    """
    Path to fetch this file's bytes from, relative to the API host.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
