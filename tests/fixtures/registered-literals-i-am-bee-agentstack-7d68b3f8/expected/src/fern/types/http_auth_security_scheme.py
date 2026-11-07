

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpAuthSecurityScheme(UniversalBaseModel):
    """
    Defines a security scheme using HTTP authentication.
    """

    bearer_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bearerFormat"), pydantic.Field(alias="bearerFormat")
    ] = None
    description: typing.Optional[str] = None
    scheme: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
