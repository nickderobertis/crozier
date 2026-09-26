

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item_status import ItemStatus


class Item(UniversalBaseModel):
    contact_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactEmail"),
        pydantic.Field(alias="contactEmail", description="Email address of the merchant's primary contact."),
    ] = None
    """
    Email address of the merchant's primary contact.
    """

    contact_first: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactFirst"),
        pydantic.Field(alias="contactFirst", description="First name of the merchant's primary contact."),
    ] = None
    """
    First name of the merchant's primary contact.
    """

    contact_last: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactLast"),
        pydantic.Field(alias="contactLast", description="Last name of the merchant's primary contact."),
    ] = None
    """
    Last name of the merchant's primary contact.
    """

    merchant_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId", description="UUID of the merchant.")
    ]
    """
    UUID of the merchant.
    """

    merchant_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantName"),
        pydantic.Field(alias="merchantName", description="Legal or trading name of the merchant business."),
    ]
    """
    Legal or trading name of the merchant business.
    """

    reference_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="referenceId"),
        pydantic.Field(alias="referenceId", description="The ID you use in your own system to identify this merchant."),
    ] = None
    """
    The ID you use in your own system to identify this merchant.
    """

    status: ItemStatus = pydantic.Field()
    """
    Derived TaxCloud lifecycle status: 'taxcloud_invited' (invite sent, not yet accepted), 'taxcloud_connected' (TaxCloud credentials set and active), 'taxcloud_disconnected' (previously connected, now disconnected), or 'external_compliance' (managed outside TaxCloud).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
