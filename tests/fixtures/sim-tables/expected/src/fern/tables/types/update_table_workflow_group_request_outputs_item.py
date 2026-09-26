

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateTableWorkflowGroupRequestOutputsItem(UniversalBaseModel):
    block_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blockId"),
        pydantic.Field(alias="blockId", description="Workflow block producing this output."),
    ] = None
    """
    Workflow block producing this output.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to the value in the workflow block output.
    """

    output_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="outputId"),
        pydantic.Field(alias="outputId", description="Registry enrichment output identifier."),
    ] = None
    """
    Registry enrichment output identifier.
    """

    column_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="columnName"),
        pydantic.Field(alias="columnName", description="Table column receiving the output."),
    ]
    """
    Table column receiving the output.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
