

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UnderInvestigationResponseBody(UniversalBaseModel):
    investigation_started: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="investigationStarted"),
        pydantic.Field(alias="investigationStarted"),
    ] = None
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    under_investigation: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="underInvestigation"), pydantic.Field(alias="underInvestigation")
    ] = None
    updated: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
