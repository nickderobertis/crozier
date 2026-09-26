

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_list200response_versions_item import DocVersionsList200ResponseVersionsItem


class DocVersionsList200Response(UniversalBaseModel):
    head: str
    versions: typing.List[DocVersionsList200ResponseVersionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
