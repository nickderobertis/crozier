

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_update404response_code import DocAnnotationsUpdate404ResponseCode
from .doc_annotations_update404response_name import DocAnnotationsUpdate404ResponseName


class DocAnnotationsUpdate404Response(UniversalBaseModel):
    name: DocAnnotationsUpdate404ResponseName
    code: DocAnnotationsUpdate404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
