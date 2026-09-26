

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_delete404response_code import DocAnnotationsDelete404ResponseCode
from .doc_annotations_delete404response_name import DocAnnotationsDelete404ResponseName


class DocAnnotationsDelete404Response(UniversalBaseModel):
    name: DocAnnotationsDelete404ResponseName
    code: DocAnnotationsDelete404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
