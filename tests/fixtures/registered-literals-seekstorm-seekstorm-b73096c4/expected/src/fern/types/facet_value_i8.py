

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueI8(UniversalBaseModel):
    """
    Signed 8-bit integer
    """

    i8: typing_extensions.Annotated[
        int, FieldMetadata(alias="I8"), pydantic.Field(alias="I8", description="Signed 8-bit integer")
    ]
    """
    Signed 8-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
