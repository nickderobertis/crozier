

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NodeRetrieved(UniversalBaseModel):
    size_bytes: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="sizeBytes"),
        pydantic.Field(alias="sizeBytes", description="The amount of data transferred by the retrieve call"),
    ]
    """
    The amount of data transferred by the retrieve call
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
