

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_manifest404response_code import DocManifest404ResponseCode
from .doc_manifest404response_name import DocManifest404ResponseName


class DocManifest404Response(UniversalBaseModel):
    name: DocManifest404ResponseName
    code: DocManifest404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
