

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .wizard_api_set_policy_async_request_wizard_config_policy import WizardApiSetPolicyAsyncRequestWizardConfigPolicy
from .wizard_api_set_policy_async_request_wizard_config_schemas_item import (
    WizardApiSetPolicyAsyncRequestWizardConfigSchemasItem,
)
from .wizard_api_set_policy_async_request_wizard_config_trust_chain_item import (
    WizardApiSetPolicyAsyncRequestWizardConfigTrustChainItem,
)


class WizardApiSetPolicyAsyncRequestWizardConfig(UniversalBaseModel):
    roles: typing.List[str]
    policy: WizardApiSetPolicyAsyncRequestWizardConfigPolicy
    schemas: typing.List[WizardApiSetPolicyAsyncRequestWizardConfigSchemasItem]
    trust_chain: typing_extensions.Annotated[
        typing.List[WizardApiSetPolicyAsyncRequestWizardConfigTrustChainItem],
        FieldMetadata(alias="trustChain"),
        pydantic.Field(alias="trustChain"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
