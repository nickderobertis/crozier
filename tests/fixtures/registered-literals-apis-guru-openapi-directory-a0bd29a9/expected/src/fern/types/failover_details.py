

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .azure_location import AzureLocation


class FailoverDetails(UniversalBaseModel):
    failover_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="failoverEnabled"), pydantic.Field(alias="failoverEnabled")
    ] = None
    failover_region: typing_extensions.Annotated[
        typing.Optional[AzureLocation], FieldMetadata(alias="failoverRegion"), pydantic.Field(alias="failoverRegion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
