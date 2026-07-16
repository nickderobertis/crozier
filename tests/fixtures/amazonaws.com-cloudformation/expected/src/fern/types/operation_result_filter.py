

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operation_result_filter_name import OperationResultFilterName


class OperationResultFilter(UniversalBaseModel):
    """
    The status that operation results are filtered by.
    """

    name: typing_extensions.Annotated[typing.Optional[OperationResultFilterName], FieldMetadata(alias="Name")] = (
        pydantic.Field(default=None)
    )
    """
    The type of filter to apply.
    """

    values: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Values")] = pydantic.Field(
        default=None
    )
    """
    The value to filter by.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
