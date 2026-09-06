

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_handler import ApplicationCommandHandler
from .application_command_patch_request_partial_options_item import ApplicationCommandPatchRequestPartialOptionsItem
from .application_integration_type import ApplicationIntegrationType
from .interaction_context_type import InteractionContextType


class ApplicationCommandPatchRequestPartial(UniversalBaseModel):
    name: typing.Optional[str] = None
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: typing.Optional[str] = None
    description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    options: typing.Optional[typing.List[ApplicationCommandPatchRequestPartialOptionsItem]] = None
    default_member_permissions: typing.Optional[int] = None
    dm_permission: typing.Optional[bool] = None
    contexts: typing.Optional[typing.List[InteractionContextType]] = None
    integration_types: typing.Optional[typing.List[ApplicationIntegrationType]] = None
    handler: typing.Optional[ApplicationCommandHandler] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
