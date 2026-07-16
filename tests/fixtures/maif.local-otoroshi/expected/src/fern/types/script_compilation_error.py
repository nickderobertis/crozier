

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScriptCompilationError(UniversalBaseModel):
    """
    The error of the compilation of a Script
    """

    column: str = pydantic.Field()
    """
    The column of the error
    """

    file: typing.Dict[str, str] = pydantic.Field()
    """
    The file where the error is located
    """

    line: str = pydantic.Field()
    """
    The line of the error
    """

    message: typing.Dict[str, str] = pydantic.Field()
    """
    The message to display for the error
    """

    raw_message: typing_extensions.Annotated[typing.Dict[str, str], FieldMetadata(alias="rawMessage")] = (
        pydantic.Field()
    )
    """
    The raw message from the compiler
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
