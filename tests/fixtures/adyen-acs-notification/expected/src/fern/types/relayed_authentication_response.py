

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authentication_decision import AuthenticationDecision


class RelayedAuthenticationResponse(UniversalBaseModel):
    authentication_decision: typing_extensions.Annotated[
        AuthenticationDecision,
        FieldMetadata(alias="authenticationDecision"),
        pydantic.Field(alias="authenticationDecision", description="The decision regarding the authentication."),
    ]
    """
    The decision regarding the authentication.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
