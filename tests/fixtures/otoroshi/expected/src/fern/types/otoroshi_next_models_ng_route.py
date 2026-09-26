

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_next_models_ng_route_backend_ref import OtoroshiNextModelsNgRouteBackendRef


class OtoroshiNextModelsNgRoute(UniversalBaseModel):
    """
    A routing primitive representing how a request is matched and where the request is forwarded
    """

    debug_flow: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable report debugging
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the route enabled
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the route
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ud of the route
    """

    export_reporting: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Export the execution reporting through standard data exporter
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The metadata of the route
    """

    frontend: typing.Optional[typing.Any] = None
    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags of the route
    """

    capture: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Capture http traffic
    """

    groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The groups of the route
    """

    backend_ref: typing.Optional[OtoroshiNextModelsNgRouteBackendRef] = pydantic.Field(default=None)
    """
    The backend id of the route (if one)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the route
    """

    backend: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
