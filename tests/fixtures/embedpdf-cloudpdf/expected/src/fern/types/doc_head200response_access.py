

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_head200response_access_reasons_item import DocHead200ResponseAccessReasonsItem


class DocHead200ResponseAccess(UniversalBaseModel):
    required: bool
    reasons: typing.List[DocHead200ResponseAccessReasonsItem]
    endpoint: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
