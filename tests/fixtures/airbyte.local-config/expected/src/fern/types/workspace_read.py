

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .customer_id import CustomerId
from .geography import Geography
from .notification import Notification
from .webhook_config_read import WebhookConfigRead
from .workspace_id import WorkspaceId


class WorkspaceRead(UniversalBaseModel):
    anonymous_data_collection: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="anonymousDataCollection"),
        pydantic.Field(alias="anonymousDataCollection"),
    ] = None
    customer_id: typing_extensions.Annotated[
        CustomerId, FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")
    ]
    default_geography: typing_extensions.Annotated[
        typing.Optional[Geography], FieldMetadata(alias="defaultGeography"), pydantic.Field(alias="defaultGeography")
    ] = None
    display_setup_wizard: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="displaySetupWizard"), pydantic.Field(alias="displaySetupWizard")
    ] = None
    email: typing.Optional[str] = None
    feedback_done: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="feedbackDone"), pydantic.Field(alias="feedbackDone")
    ] = None
    first_completed_sync: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="firstCompletedSync"), pydantic.Field(alias="firstCompletedSync")
    ] = None
    initial_setup_complete: typing_extensions.Annotated[
        bool, FieldMetadata(alias="initialSetupComplete"), pydantic.Field(alias="initialSetupComplete")
    ]
    name: str
    news: typing.Optional[bool] = None
    notifications: typing.Optional[typing.List[Notification]] = None
    security_updates: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="securityUpdates"), pydantic.Field(alias="securityUpdates")
    ] = None
    slug: str
    webhook_configs: typing_extensions.Annotated[
        typing.Optional[typing.List[WebhookConfigRead]],
        FieldMetadata(alias="webhookConfigs"),
        pydantic.Field(alias="webhookConfigs"),
    ] = None
    workspace_id: typing_extensions.Annotated[
        WorkspaceId, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
