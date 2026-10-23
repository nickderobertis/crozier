

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdStatusResponseJobsItemMetricCoverageValue(UniversalBaseModel):
    eligible: int
    current: int
    failed: int
    unread: int
    oldest_input_age_seconds: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="oldestInputAgeSeconds"),
        pydantic.Field(alias="oldestInputAgeSeconds"),
    ] = None
    measured_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="measuredAt"), pydantic.Field(alias="measuredAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
