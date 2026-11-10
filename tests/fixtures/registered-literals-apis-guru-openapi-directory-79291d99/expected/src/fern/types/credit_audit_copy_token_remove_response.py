

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class CreditAuditCopyTokenRemoveResponse(UniversalBaseModel):
    """
    CreditAuditCopyTokenRemoveResponse defines the response schema for `/credit/audit_copy_token/remove`
    """

    removed: bool = pydantic.Field()
    """
    `true` if the Audit Copy was successfully removed.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
