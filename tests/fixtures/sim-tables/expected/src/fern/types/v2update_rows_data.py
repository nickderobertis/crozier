

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2UpdateRowsData(UniversalBaseModel):
    """
    Result of a bulk row update.
    """

    updated_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="updatedCount"),
        pydantic.Field(alias="updatedCount", description="Number of updated rows."),
    ]
    """
    Number of updated rows.
    """

    updated_row_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="updatedRowIds"),
        pydantic.Field(alias="updatedRowIds", description="Identifiers of updated rows."),
    ]
    """
    Identifiers of updated rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
