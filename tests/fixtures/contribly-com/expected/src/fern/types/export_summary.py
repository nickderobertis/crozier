

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExportSummary(UniversalBaseModel):
    contributions: float = pydantic.Field()
    """
    The number of contributions selected for export.
    """

    estimated_size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="estimatedSize"),
        pydantic.Field(alias="estimatedSize", description="Human readable estimate of the export size. ie. '10MB'."),
    ] = None
    """
    Human readable estimate of the export size. ie. '10MB'.
    """

    media: float = pydantic.Field()
    """
    The number of media files included in this export.
    """

    total_media_size: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalMediaSize"),
        pydantic.Field(
            alias="totalMediaSize", description="The expected total size of the media files to be exported."
        ),
    ]
    """
    The expected total size of the media files to be exported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
