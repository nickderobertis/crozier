

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetStatusResponseScoutingExplorerProvider(UniversalBaseModel):
    observed_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ]
    http_status: typing_extensions.Annotated[int, FieldMetadata(alias="httpStatus"), pydantic.Field(alias="httpStatus")]
    credits_available: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="creditsAvailable"), pydantic.Field(alias="creditsAvailable")
    ] = None
    requests_per_second: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="requestsPerSecond"), pydantic.Field(alias="requestsPerSecond")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
