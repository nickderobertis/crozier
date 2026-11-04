

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueU32(UniversalBaseModel):
    """
    Unsigned 32-bit integer
    """

    u32: typing_extensions.Annotated[
        int, FieldMetadata(alias="U32"), pydantic.Field(alias="U32", description="Unsigned 32-bit integer")
    ]
    """
    Unsigned 32-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
