

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_flatten404response_code import DocAnnotationsFlatten404ResponseCode
from .doc_annotations_flatten404response_name import DocAnnotationsFlatten404ResponseName


class DocAnnotationsFlatten404Response(UniversalBaseModel):
    name: DocAnnotationsFlatten404ResponseName
    code: DocAnnotationsFlatten404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
