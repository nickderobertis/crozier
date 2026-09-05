

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DownloadLink(UniversalBaseModel):
    """
    I/O port type to hold a generic download link to a file (e.g. S3 pre-signed link, etc)
    """

    download_link: typing_extensions.Annotated[
        str, FieldMetadata(alias="downloadLink"), pydantic.Field(alias="downloadLink")
    ]
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
