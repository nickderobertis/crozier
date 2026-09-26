

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_metadata_get404response_code import DocMetadataGet404ResponseCode
from .doc_metadata_get404response_name import DocMetadataGet404ResponseName


class DocMetadataGet404Response(UniversalBaseModel):
    name: DocMetadataGet404ResponseName
    code: DocMetadataGet404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
