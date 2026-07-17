

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .timesheet import Timesheet


class Timesheets(UniversalBaseModel):
    timesheets: typing_extensions.Annotated[
        typing.Optional[typing.List[Timesheet]], FieldMetadata(alias="Timesheets"), pydantic.Field(alias="Timesheets")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
