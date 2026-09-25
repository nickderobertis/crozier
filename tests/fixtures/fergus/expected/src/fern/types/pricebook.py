

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_item import ContactItem
from .links import Links
from .pricebook_type import PricebookType


class Pricebook(UniversalBaseModel):
    id: float
    supplier_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="supplierName"), pydantic.Field(alias="supplierName")
    ]
    supplier_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="supplierId"), pydantic.Field(alias="supplierId")
    ] = None
    type: PricebookType
    item_count: typing_extensions.Annotated[float, FieldMetadata(alias="itemCount"), pydantic.Field(alias="itemCount")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    last_updated_at: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastUpdatedAt"), pydantic.Field(alias="lastUpdatedAt")
    ]
    supplier_contact: typing_extensions.Annotated[
        typing.Optional[typing.List[ContactItem]],
        FieldMetadata(alias="supplierContact"),
        pydantic.Field(alias="supplierContact"),
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
