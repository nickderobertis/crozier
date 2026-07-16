

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mapping_job_id_type import MappingJobIdType
from .mapping_job_id_value import MappingJobIdValue
from .mapping_job_option_type import MappingJobOptionType
from .mapping_job_state_code import MappingJobStateCode
from .nullable_date_interval import NullableDateInterval
from .nullable_number_interval import NullableNumberInterval


class MappingJob(UniversalBaseModel):
    """
    For V3: securityType2 is required when idType is BASE_TICKER or ID_EXCH_SYMBOL.  expiration is required when securityType2 is Option or Warrant.  maturity is required when securityType2 is Pool.
    """

    contract_size: typing_extensions.Annotated[
        typing.Optional[NullableNumberInterval], FieldMetadata(alias="contractSize")
    ] = None
    coupon: typing.Optional[NullableNumberInterval] = None
    currency: typing.Optional[str] = None
    exch_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="exchCode")] = None
    expiration: typing.Optional[NullableDateInterval] = None
    id_type: typing_extensions.Annotated[MappingJobIdType, FieldMetadata(alias="idType")]
    id_value: typing_extensions.Annotated[MappingJobIdValue, FieldMetadata(alias="idValue")]
    include_unlisted_equities: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="includeUnlistedEquities")
    ] = None
    market_sec_des: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="marketSecDes")] = None
    maturity: typing.Optional[NullableDateInterval] = None
    mic_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="micCode")] = None
    option_type: typing_extensions.Annotated[
        typing.Optional[MappingJobOptionType], FieldMetadata(alias="optionType")
    ] = None
    security_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="securityType")] = None
    security_type2: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="securityType2")] = None
    state_code: typing_extensions.Annotated[typing.Optional[MappingJobStateCode], FieldMetadata(alias="stateCode")] = (
        None
    )
    strike: typing.Optional[NullableNumberInterval] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
