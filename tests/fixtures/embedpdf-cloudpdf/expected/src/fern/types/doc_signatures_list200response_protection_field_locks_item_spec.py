

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_list200response_protection_field_locks_item_spec_action import (
    DocSignaturesList200ResponseProtectionFieldLocksItemSpecAction,
)


class DocSignaturesList200ResponseProtectionFieldLocksItemSpec(UniversalBaseModel):
    action: DocSignaturesList200ResponseProtectionFieldLocksItemSpecAction
    fields: typing.List[str]
    permission: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
