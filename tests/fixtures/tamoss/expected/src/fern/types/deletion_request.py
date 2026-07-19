

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deletion_request_status import DeletionRequestStatus
from .error import Error
from .timerange import Timerange
from .uuid_ import Uuid


class DeletionRequest(UniversalBaseModel):
    """
    Describes an ongoing deletion request
    """

    id: Uuid = pydantic.Field()
    """
    Deletion Request ID
    """

    flow_id: Uuid = pydantic.Field()
    """
    ID of the Flow to which the deletion request relates
    """

    timerange_to_delete: Timerange = pydantic.Field()
    """
    The timerange of Flow Segments to be deleted in this request, as described by the [TimeRange](#/schemas/timerange) type
    """

    timerange_remaining: typing.Optional[Timerange] = pydantic.Field(default=None)
    """
    The timerange of Flow Segments not yet deleted by this request, as described by the [TimeRange](#/schemas/timerange) type
    """

    delete_flow: bool = pydantic.Field()
    """
    Whether the Flow should be deleted once the timerange has been
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date/Time when this deletion request was created
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string identifier for the entity that created the deletion request. Service implementations SHOULD set suitable default values for `created_by` based on the principal accessing the system.
    """

    updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date/Time when this deletion request was updated
    """

    expiry: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date/Time when this deletion request will be deleted
    """

    status: DeletionRequestStatus = pydantic.Field()
    """
    Status of the delete request
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    Provides more information for the error status, as described by the [Error](#/schemas/error) type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
