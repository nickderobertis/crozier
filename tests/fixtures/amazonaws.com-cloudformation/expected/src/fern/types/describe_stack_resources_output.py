

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource import StackResource


class DescribeStackResourcesOutput(UniversalBaseModel):
    """
    The output for a <a>DescribeStackResources</a> action.
    """

    stack_resources: typing_extensions.Annotated[
        typing.Optional[typing.List[StackResource]], FieldMetadata(alias="StackResources")
    ] = pydantic.Field(default=None)
    """
    A list of <code>StackResource</code> structures.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
