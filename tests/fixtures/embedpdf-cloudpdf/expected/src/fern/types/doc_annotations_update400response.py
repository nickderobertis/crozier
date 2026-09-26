

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_update400response_code import DocAnnotationsUpdate400ResponseCode
from .doc_annotations_update400response_name import DocAnnotationsUpdate400ResponseName


class DocAnnotationsUpdate400Response(UniversalBaseModel):
    name: DocAnnotationsUpdate400ResponseName
    code: DocAnnotationsUpdate400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
