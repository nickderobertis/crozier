

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_scale400response_code import DocPagesSetScale400ResponseCode
from .doc_pages_set_scale400response_name import DocPagesSetScale400ResponseName


class DocPagesSetScale400Response(UniversalBaseModel):
    name: DocPagesSetScale400ResponseName
    code: DocPagesSetScale400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
