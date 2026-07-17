

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Output(UniversalBaseModel):
    """
    The Output data type.
    """

    output_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OutputKey"),
        pydantic.Field(alias="OutputKey", description="The key associated with the output."),
    ] = None
    """
    The key associated with the output.
    """

    output_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OutputValue"),
        pydantic.Field(alias="OutputValue", description="The value associated with the output."),
    ] = None
    """
    The value associated with the output.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="User defined description associated with the output."),
    ] = None
    """
    User defined description associated with the output.
    """

    export_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExportName"),
        pydantic.Field(alias="ExportName", description="The name of the export associated with the output."),
    ] = None
    """
    The name of the export associated with the output.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
