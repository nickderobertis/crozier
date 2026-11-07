

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_change_meta_change_type import EntityChangeMetaChangeType


class EntityChangeMeta(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transactionId"), pydantic.Field(alias="transactionId")
    ] = None
    time_of_change: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="timeOfChange"), pydantic.Field(alias="timeOfChange")
    ]
    user: str
    change_type: typing_extensions.Annotated[
        EntityChangeMetaChangeType, FieldMetadata(alias="changeType"), pydantic.Field(alias="changeType")
    ]
    fields_changed_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fieldsChangedCount"), pydantic.Field(alias="fieldsChangedCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
