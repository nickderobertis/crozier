

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apollo_federation_config_enable import ApolloFederationConfigEnable


class ApolloFederationConfig(UniversalBaseModel):
    enable: ApolloFederationConfigEnable = pydantic.Field()
    """
    enable takes the version of apollo federation. Supported value is v1 only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
