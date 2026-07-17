

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderParametersServicePlan(UniversalBaseModel):
    provider_control_parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The provider specific parameters needed to provision this service. This might include namespaces, special keys
    """

    service_parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON object with provisioning parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
