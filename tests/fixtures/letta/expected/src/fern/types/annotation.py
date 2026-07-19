

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotation_type import AnnotationType
from .annotation_url_citation import AnnotationUrlCitation


class Annotation(UniversalBaseModel):
    """
    A URL citation when using web search.
    """

    type: AnnotationType
    url_citation: AnnotationUrlCitation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
