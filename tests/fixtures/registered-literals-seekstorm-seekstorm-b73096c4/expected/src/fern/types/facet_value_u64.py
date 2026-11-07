

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueU64(UniversalBaseModel):
    """
    Unsigned 64-bit integer
    """

    u64: typing_extensions.Annotated[
        int, FieldMetadata(alias="U64"), pydantic.Field(alias="U64", description="Unsigned 64-bit integer")
    ]
    """
    Unsigned 64-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
