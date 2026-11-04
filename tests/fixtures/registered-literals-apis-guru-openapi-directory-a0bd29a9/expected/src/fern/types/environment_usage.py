

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_environment_state import CloudEnvironmentState
from .resource_usage_detail import ResourceUsageDetail
from .sku import Sku


class EnvironmentUsage(UniversalBaseModel):
    end_state: typing_extensions.Annotated[
        typing.Optional[CloudEnvironmentState], FieldMetadata(alias="endState"), pydantic.Field(alias="endState")
    ] = None
    id: typing.Optional[str] = None
    resource_usage: typing_extensions.Annotated[
        typing.Optional[ResourceUsageDetail],
        FieldMetadata(alias="resourceUsage"),
        pydantic.Field(alias="resourceUsage"),
    ] = None
    sku: typing.Optional[Sku] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
