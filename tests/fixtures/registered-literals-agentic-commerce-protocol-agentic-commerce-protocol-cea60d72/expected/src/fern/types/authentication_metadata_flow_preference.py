

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_flow_preference_type import AuthenticationMetadataFlowPreferenceType


class AuthenticationMetadataFlowPreference(UniversalBaseModel):
    type: AuthenticationMetadataFlowPreferenceType
    challenge: typing.Optional[typing.Dict[str, typing.Any]] = None
    frictionless: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
