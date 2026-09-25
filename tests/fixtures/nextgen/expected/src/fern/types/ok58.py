

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok58(UniversalBaseModel):
    id: str
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    test_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeId"), pydantic.Field(alias="testCodeId")
    ]
    test_code_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeText"), pydantic.Field(alias="testCodeText")
    ]
    test_code_system: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeSystem"), pydantic.Field(alias="testCodeSystem")
    ]
    test_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="testComment"), pydantic.Field(alias="testComment")
    ]
    collection_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionTime"), pydantic.Field(alias="collectionTime")
    ]
    collection_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionTimezone"), pydantic.Field(alias="collectionTimezone")
    ]
    expected_result_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedResultDate"), pydantic.Field(alias="expectedResultDate")
    ]
    scheduled_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduledTime"), pydantic.Field(alias="scheduledTime")
    ]
    scheduled_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduledTimezone"), pydantic.Field(alias="scheduledTimezone")
    ]
    loinc_code: typing_extensions.Annotated[str, FieldMetadata(alias="loincCode"), pydantic.Field(alias="loincCode")]
    charge_id: typing_extensions.Annotated[str, FieldMetadata(alias="chargeId"), pydantic.Field(alias="chargeId")]
    ordering_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingReason"), pydantic.Field(alias="orderingReason")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
