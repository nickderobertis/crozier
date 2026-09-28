

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_next_models_ng_minimal_route_backend_ref import OtoroshiNextModelsNgMinimalRouteBackendRef


class OtoroshiNextModelsNgMinimalRoute(UniversalBaseModel):
    """
    A route representation with it's minimal attributes
    """

    backend_ref: typing.Optional[OtoroshiNextModelsNgMinimalRouteBackendRef] = pydantic.Field(default=None)
    """
    The backend id of the route (if one)
    """

    frontend: typing.Optional[typing.Any] = None
    override_plugins: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Override global plugin list from route composition
    """

    backend: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
