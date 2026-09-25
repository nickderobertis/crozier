

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item22(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    device_identifier: typing_extensions.Annotated[
        str, FieldMetadata(alias="deviceIdentifier"), pydantic.Field(alias="deviceIdentifier")
    ]
    universal_device_identifier: typing_extensions.Annotated[
        str, FieldMetadata(alias="universalDeviceIdentifier"), pydantic.Field(alias="universalDeviceIdentifier")
    ]
    sno_med_ct_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="snoMedCtCode"), pydantic.Field(alias="snoMedCtCode")
    ]
    sno_med_ct_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="snoMedCtDescription"), pydantic.Field(alias="snoMedCtDescription")
    ]
    lot_or_batch_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="lotOrBatchNumber"), pydantic.Field(alias="lotOrBatchNumber")
    ]
    serial_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="serialNumber"), pydantic.Field(alias="serialNumber")
    ]
    manufacturing_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="manufacturingDate"), pydantic.Field(alias="manufacturingDate")
    ]
    expiration_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expirationDate"), pydantic.Field(alias="expirationDate")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    assigning_authority_oid: typing_extensions.Annotated[
        str, FieldMetadata(alias="assigningAuthorityOid"), pydantic.Field(alias="assigningAuthorityOid")
    ]
    assigning_authority: typing_extensions.Annotated[
        str, FieldMetadata(alias="assigningAuthority"), pydantic.Field(alias="assigningAuthority")
    ]
    gmdn_product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="gmdnProductName"), pydantic.Field(alias="gmdnProductName")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
