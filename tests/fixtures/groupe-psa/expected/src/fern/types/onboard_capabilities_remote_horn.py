

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .onboard_capabilities_remote_horn_scope_name import OnboardCapabilitiesRemoteHornScopeName


class OnboardCapabilitiesRemoteHorn(UniversalBaseModel):
    supported: bool = pydantic.Field()
    """
    true means remote horn is supported.
    """

    scope_name: typing_extensions.Annotated[
        OnboardCapabilitiesRemoteHornScopeName, FieldMetadata(alias="scopeName"), pydantic.Field(alias="scopeName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
