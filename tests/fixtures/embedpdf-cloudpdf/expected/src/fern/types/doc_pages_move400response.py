

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_move400response_code import DocPagesMove400ResponseCode
from .doc_pages_move400response_name import DocPagesMove400ResponseName


class DocPagesMove400Response(UniversalBaseModel):
    name: DocPagesMove400ResponseName
    code: DocPagesMove400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
