

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .eps_bearer_id import EpsBearerId
from .ng_ap_cause import NgApCause
from .problem_details import ProblemDetails
from .ref_to_binary_data import RefToBinaryData


class VsmfUpdateError(UniversalBaseModel):
    error: ProblemDetails
    pti: typing.Optional[int] = None
    n1sm_cause: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n1smCause"), pydantic.Field(alias="n1smCause")
    ] = None
    n1sm_info_from_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoFromUe"), pydantic.Field(alias="n1SmInfoFromUe")
    ] = None
    unknown_n1sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData],
        FieldMetadata(alias="unknownN1SmInfo"),
        pydantic.Field(alias="unknownN1SmInfo"),
    ] = None
    failed_to_assign_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="failedToAssignEbiList"),
        pydantic.Field(alias="failedToAssignEbiList"),
    ] = None
    ng_ap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngApCause"), pydantic.Field(alias="ngApCause")
    ] = None
    f_5g_mm_cause_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="5gMmCauseValue"), pydantic.Field(alias="5gMmCauseValue")
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
