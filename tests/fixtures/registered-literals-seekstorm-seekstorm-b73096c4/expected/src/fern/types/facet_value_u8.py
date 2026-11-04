

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueU8(UniversalBaseModel):
    """
    Unsigned 8-bit integer
    """

    u8: typing_extensions.Annotated[
        int, FieldMetadata(alias="U8"), pydantic.Field(alias="U8", description="Unsigned 8-bit integer")
    ]
    """
    Unsigned 8-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
