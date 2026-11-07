

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueI64(UniversalBaseModel):
    """
    Signed 64-bit integer
    """

    i64: typing_extensions.Annotated[
        int, FieldMetadata(alias="I64"), pydantic.Field(alias="I64", description="Signed 64-bit integer")
    ]
    """
    Signed 64-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
