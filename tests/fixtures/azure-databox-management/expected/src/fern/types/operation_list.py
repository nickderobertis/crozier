

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operation import Operation


class OperationList(UniversalBaseModel):
    """
    Operation Collection.
    """

    next_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextLink"),
        pydantic.Field(alias="nextLink", description="Link for the next set of operations."),
    ] = None
    """
    Link for the next set of operations.
    """

    value: typing.Optional[typing.List[Operation]] = pydantic.Field(default=None)
    """
    List of operations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
