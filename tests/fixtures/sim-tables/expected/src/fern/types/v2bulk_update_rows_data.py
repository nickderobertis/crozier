

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2BulkUpdateRowsData(UniversalBaseModel):
    """
    Rows affected by a heterogeneous bulk update.
    """

    updated_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="updatedCount"),
        pydantic.Field(alias="updatedCount", description="Number of rows the batch updated."),
    ]
    """
    Number of rows the batch updated.
    """

    updated_row_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="updatedRowIds"),
        pydantic.Field(alias="updatedRowIds", description="Identifiers of the rows the batch updated."),
    ]
    """
    Identifiers of the rows the batch updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
