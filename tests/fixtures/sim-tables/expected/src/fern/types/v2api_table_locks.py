

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2ApiTableLocks(UniversalBaseModel):
    """
    Read-only table governance locks.
    """

    schema_locked: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="schemaLocked"),
        pydantic.Field(alias="schemaLocked", description="Whether column-schema changes are locked."),
    ]
    """
    Whether column-schema changes are locked.
    """

    insert_locked: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="insertLocked"),
        pydantic.Field(alias="insertLocked", description="Whether row insertion is locked."),
    ]
    """
    Whether row insertion is locked.
    """

    update_locked: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="updateLocked"),
        pydantic.Field(alias="updateLocked", description="Whether row updates are locked."),
    ]
    """
    Whether row updates are locked.
    """

    delete_locked: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="deleteLocked"),
        pydantic.Field(alias="deleteLocked", description="Whether row and table deletion is locked."),
    ]
    """
    Whether row and table deletion is locked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
