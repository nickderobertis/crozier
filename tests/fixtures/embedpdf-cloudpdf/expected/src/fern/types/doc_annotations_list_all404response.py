

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all404response_code import DocAnnotationsListAll404ResponseCode
from .doc_annotations_list_all404response_name import DocAnnotationsListAll404ResponseName


class DocAnnotationsListAll404Response(UniversalBaseModel):
    name: DocAnnotationsListAll404ResponseName
    code: DocAnnotationsListAll404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
