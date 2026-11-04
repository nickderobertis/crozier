

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability_account_requirement_authorization_mode import CapabilityAccountRequirementAuthorizationMode
from .capability_account_requirement_requirement import CapabilityAccountRequirementRequirement
from .capability_account_requirement_retention_modes_item import CapabilityAccountRequirementRetentionModesItem


class CapabilityAccountRequirement(UniversalBaseModel):
    requirement: CapabilityAccountRequirementRequirement
    provider_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="providerLabel"), pydantic.Field(alias="providerLabel")
    ] = None
    provider_domain: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="providerDomain"), pydantic.Field(alias="providerDomain")
    ] = None
    retention_modes: typing_extensions.Annotated[
        typing.List[CapabilityAccountRequirementRetentionModesItem],
        FieldMetadata(alias="retentionModes"),
        pydantic.Field(alias="retentionModes"),
    ]
    scope_descriptions: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="scopeDescriptions"), pydantic.Field(alias="scopeDescriptions")
    ]
    authorization_mode: typing_extensions.Annotated[
        typing.Optional[CapabilityAccountRequirementAuthorizationMode],
        FieldMetadata(alias="authorizationMode"),
        pydantic.Field(alias="authorizationMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
