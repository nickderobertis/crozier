

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueBool(UniversalBaseModel):
    """
    Boolean value
    """

    bool_: typing_extensions.Annotated[
        bool, FieldMetadata(alias="Bool"), pydantic.Field(alias="Bool", description="Boolean value")
    ]
    """
    Boolean value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
