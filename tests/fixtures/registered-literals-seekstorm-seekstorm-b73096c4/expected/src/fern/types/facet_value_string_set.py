

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueStringSet(UniversalBaseModel):
    """
    String set value
    """

    string_set: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="StringSet"),
        pydantic.Field(alias="StringSet", description="String set value"),
    ]
    """
    String set value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
