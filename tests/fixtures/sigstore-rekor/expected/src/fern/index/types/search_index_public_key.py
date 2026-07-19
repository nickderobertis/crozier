

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_index_public_key_format import SearchIndexPublicKeyFormat


class SearchIndexPublicKey(UniversalBaseModel):
    content: typing.Optional[str] = None
    format: SearchIndexPublicKeyFormat
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
