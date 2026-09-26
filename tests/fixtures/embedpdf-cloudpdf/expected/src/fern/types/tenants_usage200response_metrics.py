

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TenantsUsage200ResponseMetrics(UniversalBaseModel):
    pdf_views: typing_extensions.Annotated[float, FieldMetadata(alias="pdf.views"), pydantic.Field(alias="pdf.views")]
    pdf_uploads: typing_extensions.Annotated[
        float, FieldMetadata(alias="pdf.uploads"), pydantic.Field(alias="pdf.uploads")
    ]
    storage_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="storage.bytes"), pydantic.Field(alias="storage.bytes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
