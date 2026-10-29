

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date_time import DateTime
from .execution_id import ExecutionId
from .query_state import QueryState
from .result_asset import ResultAsset
from .secondary_id_id import SecondaryIdId
from .user_id import UserId


class QueryStatus(UniversalBaseModel):
    """
    Status of an executing or executed query.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display label of the query.
    """

    is_pristine_label: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPristineLabel"),
        pydantic.Field(alias="isPristineLabel", description="True if the user did not alter the queries label."),
    ] = None
    """
    True if the user did not alter the queries label.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags of the query. To be treated like directories.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[DateTime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    last_used: typing_extensions.Annotated[
        typing.Optional[DateTime], FieldMetadata(alias="lastUsed"), pydantic.Field(alias="lastUsed")
    ] = None
    owner: typing.Optional[UserId] = None
    owner_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerName"), pydantic.Field(alias="ownerName")
    ] = None
    shared: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the query is shared with other users.
    """

    own: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the query is owned by the current user.
    """

    system: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the query is system generated.
    """

    id: typing_extensions.Annotated[
        typing.Optional[ExecutionId], FieldMetadata(alias="Id"), pydantic.Field(alias="Id")
    ] = None
    status: typing.Optional[QueryState] = None
    number_of_results: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfResults"),
        pydantic.Field(alias="numberOfResults", description="Number of result-lines of the query."),
    ] = None
    """
    Number of result-lines of the query.
    """

    required_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requiredTime"),
        pydantic.Field(alias="requiredTime", description="Duration of the last execution."),
    ] = None
    """
    Duration of the last execution.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[DateTime], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    finish_time: typing_extensions.Annotated[
        typing.Optional[DateTime], FieldMetadata(alias="finishTime"), pydantic.Field(alias="finishTime")
    ] = None
    query_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="queryType"),
        pydantic.Field(alias="queryType", description="Specific subtype of the query."),
    ] = None
    """
    Specific subtype of the query.
    """

    secondary_id: typing_extensions.Annotated[
        typing.Optional[SecondaryIdId], FieldMetadata(alias="secondaryId"), pydantic.Field(alias="secondaryId")
    ] = None
    result_urls: typing_extensions.Annotated[
        typing.Optional[typing.List[ResultAsset]],
        FieldMetadata(alias="resultUrls"),
        pydantic.Field(alias="resultUrls", description="Available result urls of the query."),
    ] = None
    """
    Available result urls of the query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
