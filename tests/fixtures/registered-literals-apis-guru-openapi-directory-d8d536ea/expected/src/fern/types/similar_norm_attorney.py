

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bar_record_preview import BarRecordPreview


class SimilarNormAttorney(UniversalBaseModel):
    bar_record_preview_array: typing_extensions.Annotated[
        typing.List[BarRecordPreview],
        FieldMetadata(alias="barRecordPreviewArray"),
        pydantic.Field(alias="barRecordPreviewArray"),
    ]
    name: str
    norm_attorney_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyAPI"), pydantic.Field(alias="normAttorneyAPI")
    ]
    norm_attorney_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyId"), pydantic.Field(alias="normAttorneyId")
    ]
    norm_attorney_similarity_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="normAttorneySimilarityScore"), pydantic.Field(alias="normAttorneySimilarityScore")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
