

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pending_approval_call import PendingApprovalCall
from .pending_approval_status import PendingApprovalStatus


class PendingApproval(UniversalBaseModel):
    batch_id: typing_extensions.Annotated[str, FieldMetadata(alias="batchId"), pydantic.Field(alias="batchId")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]
    calls: typing.List[PendingApprovalCall]
    status: PendingApprovalStatus = pydantic.Field()
    """
    Unavailable means the batch was physically removed; it does not assert whether the tool executed.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Approval deadline; absent for an unavailable batch that has already been physically removed.",
        ),
    ] = None
    """
    Approval deadline; absent for an unavailable batch that has already been physically removed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
