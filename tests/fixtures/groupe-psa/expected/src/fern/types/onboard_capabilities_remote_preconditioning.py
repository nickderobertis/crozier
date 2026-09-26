

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .onboard_capabilities_remote_preconditioning_parameters import OnboardCapabilitiesRemotePreconditioningParameters
from .onboard_capabilities_remote_preconditioning_scope_name import OnboardCapabilitiesRemotePreconditioningScopeName


class OnboardCapabilitiesRemotePreconditioning(UniversalBaseModel):
    supported: bool = pydantic.Field()
    """
    true means remote preconditioning is supported.
    """

    scope_name: typing_extensions.Annotated[
        OnboardCapabilitiesRemotePreconditioningScopeName,
        FieldMetadata(alias="scopeName"),
        pydantic.Field(alias="scopeName"),
    ]
    parameters: OnboardCapabilitiesRemotePreconditioningParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
