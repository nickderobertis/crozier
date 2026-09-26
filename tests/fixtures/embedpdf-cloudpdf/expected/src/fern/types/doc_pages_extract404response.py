

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_extract404response_code import DocPagesExtract404ResponseCode
from .doc_pages_extract404response_name import DocPagesExtract404ResponseName


class DocPagesExtract404Response(UniversalBaseModel):
    name: DocPagesExtract404ResponseName
    code: DocPagesExtract404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
