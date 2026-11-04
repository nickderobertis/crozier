

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueU16(UniversalBaseModel):
    """
    Unsigned 16-bit integer
    """

    u16: typing_extensions.Annotated[
        int, FieldMetadata(alias="U16"), pydantic.Field(alias="U16", description="Unsigned 16-bit integer")
    ]
    """
    Unsigned 16-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
