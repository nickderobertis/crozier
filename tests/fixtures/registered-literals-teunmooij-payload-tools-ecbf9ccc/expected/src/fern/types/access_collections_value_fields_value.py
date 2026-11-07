

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_collections_value_fields_value_create import AccessCollectionsValueFieldsValueCreate
from .access_collections_value_fields_value_read import AccessCollectionsValueFieldsValueRead
from .access_collections_value_fields_value_update import AccessCollectionsValueFieldsValueUpdate


class AccessCollectionsValueFieldsValue(UniversalBaseModel):
    create: AccessCollectionsValueFieldsValueCreate
    read: AccessCollectionsValueFieldsValueRead
    update: AccessCollectionsValueFieldsValueUpdate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
