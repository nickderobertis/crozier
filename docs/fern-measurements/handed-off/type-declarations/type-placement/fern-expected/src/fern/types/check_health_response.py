

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .check_health_response_state import CheckHealthResponseState


class CheckHealthResponse(UniversalBaseModel):
    state: typing.Optional[CheckHealthResponseState] = None
    checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="checkedAt"), pydantic.Field(alias="checkedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
