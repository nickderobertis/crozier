

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NotificationBase(UniversalBaseModel):
    """
    base object for Notifications (every notification has this basic structure)
    """

    created_at: typing.Optional[int] = None
    data_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dataId"), pydantic.Field(alias="dataId")
    ] = None
    last_updated: typing.Optional[int] = None
    max_tries: typing.Optional[int] = None
    queue_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="queueId"), pydantic.Field(alias="queueId")
    ] = None
    record_state_key: typing.Optional[str] = None
    record_state_val: typing.Optional[str] = None
    tries: typing.Optional[int] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
