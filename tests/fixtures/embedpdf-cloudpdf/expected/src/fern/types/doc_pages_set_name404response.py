

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_name404response_code import DocPagesSetName404ResponseCode
from .doc_pages_set_name404response_name import DocPagesSetName404ResponseName


class DocPagesSetName404Response(UniversalBaseModel):
    name: DocPagesSetName404ResponseName
    code: DocPagesSetName404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
