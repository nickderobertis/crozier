

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MoveOperation(UniversalBaseModel):
    from_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="A JSON Pointer path pointing to the location to move/copy from."),
    ]
    """
    A JSON Pointer path pointing to the location to move/copy from.
    """

    path: str = pydantic.Field()
    """
    A JSON Pointer path pointing to the location to move/copy from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
