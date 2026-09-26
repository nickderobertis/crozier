

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_flatten400response_code import DocAnnotationsFlatten400ResponseCode
from .doc_annotations_flatten400response_name import DocAnnotationsFlatten400ResponseName


class DocAnnotationsFlatten400Response(UniversalBaseModel):
    name: DocAnnotationsFlatten400ResponseName
    code: DocAnnotationsFlatten400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
