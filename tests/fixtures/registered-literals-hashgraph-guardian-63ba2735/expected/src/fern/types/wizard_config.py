

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wizard_config_policy import WizardConfigPolicy
from .wizard_config_schemas_item import WizardConfigSchemasItem
from .wizard_config_trust_chain_item import WizardConfigTrustChainItem


class WizardConfig(UniversalBaseModel):
    roles: typing.List[str]
    policy: WizardConfigPolicy
    schemas: typing.List[WizardConfigSchemasItem]
    trust_chain: typing_extensions.Annotated[
        typing.List[WizardConfigTrustChainItem], FieldMetadata(alias="trustChain"), pydantic.Field(alias="trustChain")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
