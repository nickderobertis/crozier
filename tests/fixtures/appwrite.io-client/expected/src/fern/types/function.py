

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Function(UniversalBaseModel):
    """
    Function
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    Function ID.
    """

    permissions: typing_extensions.Annotated[
        typing.Dict[str, typing.Optional[typing.Any]], FieldMetadata(alias="$permissions")
    ] = pydantic.Field()
    """
    Function permissions.
    """

    date_created: typing_extensions.Annotated[int, FieldMetadata(alias="dateCreated")] = pydantic.Field()
    """
    Function creation date in Unix timestamp.
    """

    date_updated: typing_extensions.Annotated[int, FieldMetadata(alias="dateUpdated")] = pydantic.Field()
    """
    Function update date in Unix timestamp.
    """

    events: typing.List[str] = pydantic.Field()
    """
    Function trigger events.
    """

    name: str = pydantic.Field()
    """
    Function name.
    """

    runtime: str = pydantic.Field()
    """
    Function execution runtime.
    """

    schedule: str = pydantic.Field()
    """
    Function execution schedult in CRON format.
    """

    schedule_next: typing_extensions.Annotated[int, FieldMetadata(alias="scheduleNext")] = pydantic.Field()
    """
    Function next scheduled execution date in Unix timestamp.
    """

    schedule_previous: typing_extensions.Annotated[int, FieldMetadata(alias="schedulePrevious")] = pydantic.Field()
    """
    Function next scheduled execution date in Unix timestamp.
    """

    status: str = pydantic.Field()
    """
    Function status. Possible values: disabled, enabled
    """

    tag: str = pydantic.Field()
    """
    Function active tag ID.
    """

    timeout: int = pydantic.Field()
    """
    Function execution timeout in seconds.
    """

    vars: str = pydantic.Field()
    """
    Function environment variables.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
