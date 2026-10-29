

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorInfo(UniversalBaseModel):
    """
    Basic format of an error.
    """

    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Id"), pydantic.Field(alias="Id")] = None
    code: typing.Optional[str] = None
    message: typing.Optional[str] = None
    context: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
