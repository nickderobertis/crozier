

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataStatusHistoryArrayItem(UniversalBaseModel):
    effective_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="effectiveDate"), pydantic.Field(alias="effectiveDate")
    ] = None
    status_change: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusChange"), pydantic.Field(alias="statusChange")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
