

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.policy_config import PolicyConfig
from ...types.wizard_config import WizardConfig


class PostWizardPolicyIdConfigResponse(UniversalBaseModel):
    policy_config: typing_extensions.Annotated[
        typing.Optional[PolicyConfig], FieldMetadata(alias="policyConfig"), pydantic.Field(alias="policyConfig")
    ] = None
    wizard_config: typing_extensions.Annotated[
        typing.Optional[WizardConfig], FieldMetadata(alias="wizardConfig"), pydantic.Field(alias="wizardConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
