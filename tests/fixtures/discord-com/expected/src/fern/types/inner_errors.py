

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error import Error


class InnerErrors(UniversalBaseModel):
    errors: typing_extensions.Annotated[
        typing.List[Error],
        FieldMetadata(alias="_errors"),
        pydantic.Field(alias="_errors", description="The list of errors for this field"),
    ]
    """
    The list of errors for this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
