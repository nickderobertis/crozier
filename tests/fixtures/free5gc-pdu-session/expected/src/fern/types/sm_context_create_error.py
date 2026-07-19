

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .problem_details import ProblemDetails
from .ref_to_binary_data import RefToBinaryData


class SmContextCreateError(UniversalBaseModel):
    error: ProblemDetails
    n1sm_msg: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmMsg"), pydantic.Field(alias="n1SmMsg")
    ] = None
    recovery_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="recoveryTime"), pydantic.Field(alias="recoveryTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
