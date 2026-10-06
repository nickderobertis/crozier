

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .card_version import CardVersion
from .xml_gregorian_calendar import XmlGregorianCalendar


class CardInfoType(UniversalBaseModel):
    card_handle: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardHandle"), pydantic.Field(alias="cardHandle")
    ] = None
    card_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardType"), pydantic.Field(alias="cardType")
    ] = None
    card_version: typing_extensions.Annotated[
        typing.Optional[CardVersion], FieldMetadata(alias="cardVersion"), pydantic.Field(alias="cardVersion")
    ] = None
    iccsn: typing.Optional[str] = None
    ct_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ctId"), pydantic.Field(alias="ctId")
    ] = None
    slot_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="slotId"), pydantic.Field(alias="slotId")
    ] = None
    insert_time: typing_extensions.Annotated[
        typing.Optional[XmlGregorianCalendar], FieldMetadata(alias="insertTime"), pydantic.Field(alias="insertTime")
    ] = None
    card_holder_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardHolderName"), pydantic.Field(alias="cardHolderName")
    ] = None
    kvnr: typing.Optional[str] = None
    certificate_expiration_date: typing_extensions.Annotated[
        typing.Optional[XmlGregorianCalendar],
        FieldMetadata(alias="certificateExpirationDate"),
        pydantic.Field(alias="certificateExpirationDate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
