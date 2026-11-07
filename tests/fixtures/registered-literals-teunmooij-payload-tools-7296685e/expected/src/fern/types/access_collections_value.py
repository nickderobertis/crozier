

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_collections_value_create import AccessCollectionsValueCreate
from .access_collections_value_delete import AccessCollectionsValueDelete
from .access_collections_value_fields_value import AccessCollectionsValueFieldsValue
from .access_collections_value_read import AccessCollectionsValueRead
from .access_collections_value_update import AccessCollectionsValueUpdate


class AccessCollectionsValue(UniversalBaseModel):
    create: AccessCollectionsValueCreate
    read: AccessCollectionsValueRead
    update: AccessCollectionsValueUpdate
    delete: AccessCollectionsValueDelete
    fields: typing.Dict[str, AccessCollectionsValueFieldsValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
