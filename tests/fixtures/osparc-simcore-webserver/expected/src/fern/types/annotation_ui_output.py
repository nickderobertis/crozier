

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotation_ui_output_type import AnnotationUiOutputType


class AnnotationUiOutput(UniversalBaseModel):
    type: AnnotationUiOutputType
    color: typing.Optional[str] = None
    attributes: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    svg attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
