

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .upload_bulk_contacts_request_contacts_item_attributes_item_attribute_key import (
    UploadBulkContactsRequestContactsItemAttributesItemAttributeKey,
)


class UploadBulkContactsRequestContactsItemAttributesItem(UniversalBaseModel):
    attribute_key: typing_extensions.Annotated[
        UploadBulkContactsRequestContactsItemAttributesItemAttributeKey,
        FieldMetadata(alias="attributeKey"),
        pydantic.Field(alias="attributeKey"),
    ]
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
