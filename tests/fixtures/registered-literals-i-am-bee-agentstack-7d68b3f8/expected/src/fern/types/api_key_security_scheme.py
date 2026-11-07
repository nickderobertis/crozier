

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .in_ import In


class ApiKeySecurityScheme(UniversalBaseModel):
    """
    Defines a security scheme using an API key.
    """

    description: typing.Optional[str] = None
    in_: typing_extensions.Annotated[In, FieldMetadata(alias="in"), pydantic.Field(alias="in")]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
