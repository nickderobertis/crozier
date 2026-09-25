

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class V1ForecastsUpdateForecast(UniversalBaseModel):
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Task title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Detailed description
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Start date (YYYY-MM-DD)"),
    ] = None
    """
    Start date (YYYY-MM-DD)
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    End date (YYYY-MM-DD)
    """

    project_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Project ID
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Primary user ID (alternative to users array)
    """

    users: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    User assignments with per-user estimates
    """

    estimated_minutes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Estimated time in minutes
    """

    label_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Tag/label IDs to apply
    """

    completed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp to mark as completed
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External system identifier for integration mapping
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
