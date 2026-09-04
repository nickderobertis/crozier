

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .annotations_file_labels import AnnotationsFileLabels
from .annotations_file_space import AnnotationsFileSpace
from .annotations_file_tools import AnnotationsFileTools


class AnnotationsFile(UniversalBaseModel):
    schema_version: typing_extensions.Annotated[
        float, FieldMetadata(alias="schemaVersion"), pydantic.Field(alias="schemaVersion")
    ]
    space: AnnotationsFileSpace
    labels: typing.Optional[AnnotationsFileLabels] = None
    tools: AnnotationsFileTools

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
