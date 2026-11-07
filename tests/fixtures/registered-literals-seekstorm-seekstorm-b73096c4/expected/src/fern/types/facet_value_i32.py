

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueI32(UniversalBaseModel):
    """
    Signed 32-bit integer
    """

    i32: typing_extensions.Annotated[
        int, FieldMetadata(alias="I32"), pydantic.Field(alias="I32", description="Signed 32-bit integer")
    ]
    """
    Signed 32-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
