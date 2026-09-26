

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tokens_issue_request_tenant_scope_item import TokensIssueRequestTenantScopeItem


class TokensIssueRequestTenant(UniversalBaseModel):
    sub: str
    scope: typing.List[TokensIssueRequestTenantScopeItem]
    expires_in: typing_extensions.Annotated[int, FieldMetadata(alias="expiresIn"), pydantic.Field(alias="expiresIn")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
