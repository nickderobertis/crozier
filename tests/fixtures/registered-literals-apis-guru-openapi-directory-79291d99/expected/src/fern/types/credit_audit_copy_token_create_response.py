

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class CreditAuditCopyTokenCreateResponse(UniversalBaseModel):
    """
    CreditAuditCopyTokenCreateResponse defines the response schema for `/credit/audit_copy_token/get`
    """

    audit_copy_token: str = pydantic.Field()
    """
    A token that can be shared with a third party auditor, which allows them to fetch the Asset Reports attached to the token. This token should be stored securely.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
