

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .dns_record import DnsRecord
from .dns_response_response_code import DnsResponseResponseCode


class DnsResponse(UniversalBaseModel):
    """
    DNS response to return
    """

    delay: typing.Optional[Delay] = None
    answer_records: typing_extensions.Annotated[
        typing.Optional[typing.List[DnsRecord]],
        FieldMetadata(alias="answerRecords"),
        pydantic.Field(alias="answerRecords"),
    ] = None
    authority_records: typing_extensions.Annotated[
        typing.Optional[typing.List[DnsRecord]],
        FieldMetadata(alias="authorityRecords"),
        pydantic.Field(alias="authorityRecords"),
    ] = None
    additional_records: typing_extensions.Annotated[
        typing.Optional[typing.List[DnsRecord]],
        FieldMetadata(alias="additionalRecords"),
        pydantic.Field(alias="additionalRecords"),
    ] = None
    response_code: typing_extensions.Annotated[
        typing.Optional[DnsResponseResponseCode],
        FieldMetadata(alias="responseCode"),
        pydantic.Field(alias="responseCode"),
    ] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
