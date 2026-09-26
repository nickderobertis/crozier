

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocSignaturesAnalysis200ResponseLater(UniversalBaseModel):
    revision_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="revisionCount"), pydantic.Field(alias="revisionCount")
    ]
    undone_object_numbers: typing_extensions.Annotated[
        typing.List[int], FieldMetadata(alias="undoneObjectNumbers"), pydantic.Field(alias="undoneObjectNumbers")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
