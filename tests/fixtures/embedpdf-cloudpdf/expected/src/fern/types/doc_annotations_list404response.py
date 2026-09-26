

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list404response_code import DocAnnotationsList404ResponseCode
from .doc_annotations_list404response_name import DocAnnotationsList404ResponseName


class DocAnnotationsList404Response(UniversalBaseModel):
    name: DocAnnotationsList404ResponseName
    code: DocAnnotationsList404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
