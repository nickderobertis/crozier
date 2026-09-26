

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all409response_code import DocAnnotationsListAll409ResponseCode
from .doc_annotations_list_all409response_name import DocAnnotationsListAll409ResponseName


class DocAnnotationsListAll409Response(UniversalBaseModel):
    name: DocAnnotationsListAll409ResponseName
    code: DocAnnotationsListAll409ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
