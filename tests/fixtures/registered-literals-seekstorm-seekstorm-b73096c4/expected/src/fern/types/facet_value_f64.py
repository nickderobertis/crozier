

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueF64(UniversalBaseModel):
    """
    64-bit floating point number
    """

    f64: typing_extensions.Annotated[
        float, FieldMetadata(alias="F64"), pydantic.Field(alias="F64", description="64-bit floating point number")
    ]
    """
    64-bit floating point number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
