

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilterDocumentsDto(UniversalBaseModel):
    document_id1: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentId1"), pydantic.Field(alias="documentId1")
    ]
    document_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentId2"), pydantic.Field(alias="documentId2")
    ]
    document_ids: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentIds"), pydantic.Field(alias="documentIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
