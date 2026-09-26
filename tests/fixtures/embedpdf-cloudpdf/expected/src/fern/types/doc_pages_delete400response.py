

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_delete400response_code import DocPagesDelete400ResponseCode
from .doc_pages_delete400response_name import DocPagesDelete400ResponseName


class DocPagesDelete400Response(UniversalBaseModel):
    name: DocPagesDelete400ResponseName
    code: DocPagesDelete400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
