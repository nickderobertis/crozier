

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_signature_contents_response_code import DocVersionsSignatureContentsResponseCode
from .doc_versions_signature_contents_response_name import DocVersionsSignatureContentsResponseName


class DocVersionsSignatureContentsResponse(UniversalBaseModel):
    name: DocVersionsSignatureContentsResponseName
    code: DocVersionsSignatureContentsResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
