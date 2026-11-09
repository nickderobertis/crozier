

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extracted_fields import ExtractedFields
from .raw_ordered_data import RawOrderedData


class SourceStructuredData(UniversalBaseModel):
    extracted_fields: typing_extensions.Annotated[
        typing.Optional[ExtractedFields],
        FieldMetadata(alias="extractedFields"),
        pydantic.Field(alias="extractedFields"),
    ] = None
    raw_ordered_data_array: typing_extensions.Annotated[
        typing.List[typing.Optional[RawOrderedData]],
        FieldMetadata(alias="rawOrderedDataArray"),
        pydantic.Field(alias="rawOrderedDataArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
