

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectDocument(UniversalBaseModel):
    document_hash: str
    filename: typing.Optional[str] = None
    file_uri: typing.Optional[str] = None
    ref_uri: typing.Optional[str] = None
    number_pages: typing.Optional[int] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
