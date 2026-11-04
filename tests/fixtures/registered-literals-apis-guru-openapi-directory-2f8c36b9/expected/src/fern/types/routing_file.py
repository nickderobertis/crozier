

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .route import Route
from .routing_options import RoutingOptions


class RoutingFile(UniversalBaseModel):
    options: typing.Optional[RoutingOptions] = None
    routes: typing.List[Route]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
