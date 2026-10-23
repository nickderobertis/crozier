

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upload_bulk_contacts_request_contacts_item_attributes_item import (
    UploadBulkContactsRequestContactsItemAttributesItem,
)


class UploadBulkContactsRequestContactsItem(UniversalBaseModel):
    attributes: typing.List[UploadBulkContactsRequestContactsItemAttributesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
