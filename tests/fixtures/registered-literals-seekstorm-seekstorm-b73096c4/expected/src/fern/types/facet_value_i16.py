

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueI16(UniversalBaseModel):
    """
    Signed 16-bit integer
    """

    i16: typing_extensions.Annotated[
        int, FieldMetadata(alias="I16"), pydantic.Field(alias="I16", description="Signed 16-bit integer")
    ]
    """
    Signed 16-bit integer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
