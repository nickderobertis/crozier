

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_list200response_signatures_item_lock_action import (
    DocSignaturesList200ResponseSignaturesItemLockAction,
)


class DocSignaturesList200ResponseSignaturesItemLock(UniversalBaseModel):
    action: DocSignaturesList200ResponseSignaturesItemLockAction
    fields: typing.List[str]
    permission: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
