

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_create404response_code import DocAnnotationsCreate404ResponseCode
from .doc_annotations_create404response_name import DocAnnotationsCreate404ResponseName


class DocAnnotationsCreate404Response(UniversalBaseModel):
    name: DocAnnotationsCreate404ResponseName
    code: DocAnnotationsCreate404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
