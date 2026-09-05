

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .annotation_ui_output import AnnotationUiOutput
from .slideshow_ui import SlideshowUi
from .study_ui_output_mode import StudyUiOutputMode


class StudyUiOutput(UniversalBaseModel):
    slideshow: typing.Optional[typing.Dict[str, typing.Optional[SlideshowUi]]] = None
    current_node_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="currentNodeId"), pydantic.Field(alias="currentNodeId")
    ] = None
    annotations: typing.Optional[typing.Dict[str, typing.Optional[AnnotationUiOutput]]] = None
    mode: typing.Optional[StudyUiOutputMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
