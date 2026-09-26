

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_history_entry import ChatHistoryEntry
from .chat_request_project_whitelist_mode import ChatRequestProjectWhitelistMode
from .chat_request_selected_platforms_item import ChatRequestSelectedPlatformsItem
from .tool_floor import ToolFloor


class ChatRequest(UniversalBaseModel):
    model: typing.Optional[str] = None
    message: str
    business_id: typing.Optional[str] = None
    business_name: typing.Optional[str] = None
    business_category: typing.Optional[str] = None
    business_address: typing.Optional[str] = None
    business_phone: typing.Optional[str] = None
    business_website: typing.Optional[str] = None
    business_description: typing.Optional[str] = None
    business_voice_tone: typing.Optional[typing.List[str]] = None
    active_integrations: typing.Optional[typing.List[str]] = None
    selected_platforms: typing.Optional[typing.List[ChatRequestSelectedPlatformsItem]] = None
    history: typing.Optional[typing.List[ChatHistoryEntry]] = None
    project_id: typing.Optional[str] = None
    project_name: typing.Optional[str] = None
    project_system_prompt: typing.Optional[str] = None
    project_whitelist_mode: typing.Optional[ChatRequestProjectWhitelistMode] = None
    project_allowed_tools: typing.Optional[typing.List[str]] = None
    user_id: typing.Optional[str] = None
    message_id: typing.Optional[str] = None
    tier: typing.Optional[str] = None
    business_approvals: typing.Optional[typing.Dict[str, ToolFloor]] = None
    project_approval_overrides: typing.Optional[typing.Dict[str, ToolFloor]] = None
    locale: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
