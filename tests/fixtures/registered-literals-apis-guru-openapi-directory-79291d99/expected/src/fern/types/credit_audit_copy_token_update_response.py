

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class CreditAuditCopyTokenUpdateResponse(UniversalBaseModel):
    """
    CreditAuditCopyTokenUpdateResponse defines the response schema for `/credit/audit_copy_token/update`
    """

    request_id: RequestId
    updated: bool = pydantic.Field()
    """
    `true` if the Audit Copy Token was successfully updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
