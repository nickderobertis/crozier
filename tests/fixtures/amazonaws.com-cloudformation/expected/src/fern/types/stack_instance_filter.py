

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_instance_filter_name import StackInstanceFilterName


class StackInstanceFilter(UniversalBaseModel):
    """
    The filter to apply to stack instances
    """

    name: typing_extensions.Annotated[
        typing.Optional[StackInstanceFilterName],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The type of filter to apply."),
    ] = None
    """
    The type of filter to apply.
    """

    values: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Values"),
        pydantic.Field(alias="Values", description="The status to filter by."),
    ] = None
    """
    The status to filter by.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
