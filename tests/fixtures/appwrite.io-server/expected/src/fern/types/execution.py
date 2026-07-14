

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Execution(UniversalBaseModel):
    """
    Execution
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    Execution ID.
    """

    date_created: typing_extensions.Annotated[int, FieldMetadata(alias="dateCreated")] = pydantic.Field()
    """
    The execution creation date in Unix timestamp.
    """

    exit_code: typing_extensions.Annotated[int, FieldMetadata(alias="exitCode")] = pydantic.Field()
    """
    The script exit code.
    """

    function_id: typing_extensions.Annotated[str, FieldMetadata(alias="functionId")] = pydantic.Field()
    """
    Function ID.
    """

    status: str = pydantic.Field()
    """
    The status of the function execution. Possible values can be: `waiting`, `processing`, `completed`, or `failed`.
    """

    stderr: str = pydantic.Field()
    """
    The script stderr output string. Logs the last 4,000 characters of the execution stderr output
    """

    stdout: str = pydantic.Field()
    """
    The script stdout output string. Logs the last 4,000 characters of the execution stdout output.
    """

    time: float = pydantic.Field()
    """
    The script execution time in seconds.
    """

    trigger: str = pydantic.Field()
    """
    The trigger that caused the function to execute. Possible values can be: `http`, `schedule`, or `event`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
