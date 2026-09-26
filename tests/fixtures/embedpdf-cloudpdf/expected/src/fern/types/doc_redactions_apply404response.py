

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_redactions_apply404response_code import DocRedactionsApply404ResponseCode
from .doc_redactions_apply404response_name import DocRedactionsApply404ResponseName


class DocRedactionsApply404Response(UniversalBaseModel):
    name: DocRedactionsApply404ResponseName
    code: DocRedactionsApply404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
