

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MatchedObject(UniversalBaseModel):
    highlight_snippet: typing_extensions.Annotated[
        str, FieldMetadata(alias="highlightSnippet"), pydantic.Field(alias="highlightSnippet")
    ]
    matched_object_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="matchedObjectAPI"), pydantic.Field(alias="matchedObjectAPI")
    ]
    matched_object_attribute: typing_extensions.Annotated[
        str, FieldMetadata(alias="matchedObjectAttribute"), pydantic.Field(alias="matchedObjectAttribute")
    ]
    matched_object_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="matchedObjectId"), pydantic.Field(alias="matchedObjectId")
    ]
    matched_object_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="matchedObjectName"), pydantic.Field(alias="matchedObjectName")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
