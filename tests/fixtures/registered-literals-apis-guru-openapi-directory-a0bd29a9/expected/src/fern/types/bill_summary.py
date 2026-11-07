

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .azure_location import AzureLocation
from .environment_usage import EnvironmentUsage
from .vso_plan_info import VsoPlanInfo


class BillSummary(UniversalBaseModel):
    bill_generation_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="billGenerationTime"),
        pydantic.Field(alias="billGenerationTime"),
    ] = None
    environment_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="environmentId"), pydantic.Field(alias="environmentId")
    ] = None
    id: typing.Optional[str] = None
    location: typing.Optional[AzureLocation] = None
    partition_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="partitionKey"), pydantic.Field(alias="partitionKey")
    ] = None
    period_end: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="periodEnd"), pydantic.Field(alias="periodEnd")
    ] = None
    period_start: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="periodStart"), pydantic.Field(alias="periodStart")
    ] = None
    plan: typing.Optional[VsoPlanInfo] = None
    usage: typing.Optional[typing.Dict[str, typing.Optional[float]]] = None
    usage_detail: typing_extensions.Annotated[
        typing.Optional[typing.List[EnvironmentUsage]],
        FieldMetadata(alias="usageDetail"),
        pydantic.Field(alias="usageDetail"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
