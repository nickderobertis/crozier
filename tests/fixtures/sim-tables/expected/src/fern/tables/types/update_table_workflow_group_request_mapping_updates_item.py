

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateTableWorkflowGroupRequestMappingUpdatesItem(UniversalBaseModel):
    column_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="columnName"),
        pydantic.Field(alias="columnName", description="Existing output column to remap."),
    ]
    """
    Existing output column to remap.
    """

    block_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="blockId"),
        pydantic.Field(alias="blockId", description="New workflow block producing the value."),
    ]
    """
    New workflow block producing the value.
    """

    path: str = pydantic.Field()
    """
    New path to the workflow output value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
