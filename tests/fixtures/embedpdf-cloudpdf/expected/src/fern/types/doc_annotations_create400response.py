

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_create400response_code import DocAnnotationsCreate400ResponseCode
from .doc_annotations_create400response_name import DocAnnotationsCreate400ResponseName


class DocAnnotationsCreate400Response(UniversalBaseModel):
    name: DocAnnotationsCreate400ResponseName
    code: DocAnnotationsCreate400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
