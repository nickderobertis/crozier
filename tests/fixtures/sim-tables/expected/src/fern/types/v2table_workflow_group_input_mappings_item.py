

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableWorkflowGroupInputMappingsItem(UniversalBaseModel):
    input_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="inputName"), pydantic.Field(alias="inputName", description="Workflow input name.")
    ]
    """
    Workflow input name.
    """

    column_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="columnName"),
        pydantic.Field(alias="columnName", description="Name of the source table column."),
    ]
    """
    Name of the source table column.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
