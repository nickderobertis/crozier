

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_signatures404response_code import DocVersionsSignatures404ResponseCode
from .doc_versions_signatures404response_name import DocVersionsSignatures404ResponseName


class DocVersionsSignatures404Response(UniversalBaseModel):
    name: DocVersionsSignatures404ResponseName
    code: DocVersionsSignatures404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
