

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_revision_response_code import DocVersionsRevisionResponseCode
from .doc_versions_revision_response_name import DocVersionsRevisionResponseName


class DocVersionsRevisionResponse(UniversalBaseModel):
    name: DocVersionsRevisionResponseName
    code: DocVersionsRevisionResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
