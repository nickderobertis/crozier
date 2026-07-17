

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Export(UniversalBaseModel):
    """
    The <code>Export</code> structure describes the exported output values for a stack.
    """

    exporting_stack_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExportingStackId"),
        pydantic.Field(
            alias="ExportingStackId", description="The stack that contains the exported output name and value."
        ),
    ] = None
    """
    The stack that contains the exported output name and value.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(
            alias="Name",
            description="The name of exported output value. Use this name and the <code>Fn::ImportValue</code> function to import the associated value into other stacks. The name is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.",
        ),
    ] = None
    """
    The name of exported output value. Use this name and the <code>Fn::ImportValue</code> function to import the associated value into other stacks. The name is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.
    """

    value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Value"),
        pydantic.Field(
            alias="Value",
            description="The value of the exported output, such as a resource physical ID. This value is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.",
        ),
    ] = None
    """
    The value of the exported output, such as a resource physical ID. This value is defined in the <code>Export</code> field in the associated stack's <code>Outputs</code> section.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
