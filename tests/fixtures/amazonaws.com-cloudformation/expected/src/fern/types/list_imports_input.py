

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListImportsInput(UniversalBaseModel):
    export_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ExportName"),
        pydantic.Field(
            alias="ExportName",
            description="The name of the exported output value. CloudFormation returns the stack names that are importing this value.",
        ),
    ]
    """
    The name of the exported output value. CloudFormation returns the stack names that are importing this value.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="A string (provided by the <a>ListImports</a> response output) that identifies the next page of stacks that are importing the specified exported output value.",
        ),
    ] = None
    """
    A string (provided by the <a>ListImports</a> response output) that identifies the next page of stacks that are importing the specified exported output value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
