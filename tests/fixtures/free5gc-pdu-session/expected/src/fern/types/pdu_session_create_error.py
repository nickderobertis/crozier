

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .problem_details import ProblemDetails
from .ref_to_binary_data import RefToBinaryData


class PduSessionCreateError(UniversalBaseModel):
    error: ProblemDetails
    n1sm_cause: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n1smCause"), pydantic.Field(alias="n1smCause")
    ] = None
    n1sm_info_to_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoToUe"), pydantic.Field(alias="n1SmInfoToUe")
    ] = None
    back_off_timer: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="backOffTimer"), pydantic.Field(alias="backOffTimer")
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
