

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_next_models_ng_minimal_route import OtoroshiNextModelsNgMinimalRoute


class OtoroshiNextModelsNgRouteComposition(UniversalBaseModel):
    """
    ???
    """

    capture: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    debug_flow: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    routes: typing.Optional[typing.List[OtoroshiNextModelsNgMinimalRoute]] = pydantic.Field(default=None)
    """
    ???
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    export_reporting: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    client: typing.Optional[typing.Any] = None
    groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
