

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .trust_rule_create_response_rule_origin import TrustRuleCreateResponseRuleOrigin
from .trust_rule_create_response_rule_risk import TrustRuleCreateResponseRuleRisk


class TrustRuleCreateResponseRule(UniversalBaseModel):
    id: str
    tool: str
    pattern: str
    risk: TrustRuleCreateResponseRuleRisk
    description: str
    origin: TrustRuleCreateResponseRuleOrigin
    user_modified: typing_extensions.Annotated[
        bool, FieldMetadata(alias="userModified"), pydantic.Field(alias="userModified")
    ]
    deleted: bool
    scope: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
