

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_item_payload_contact_type import ContactItemPayloadContactType


class ContactItemPayload(UniversalBaseModel):
    id: typing.Optional[float] = None
    contact_type: typing_extensions.Annotated[
        ContactItemPayloadContactType,
        FieldMetadata(alias="contactType"),
        pydantic.Field(
            alias="contactType",
            description="The type of this contact item. It can be one of the following: email, phone, mobile, other, fax, website",
        ),
    ]
    """
    The type of this contact item. It can be one of the following: email, phone, mobile, other, fax, website
    """

    contact_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="contactValue"),
        pydantic.Field(alias="contactValue", description="The value of this contact item."),
    ]
    """
    The value of this contact item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
