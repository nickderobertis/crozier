

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_installed_apps_item_teams_app import ChatInstalledAppsItemTeamsApp


class ChatInstalledAppsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    teams_app: typing_extensions.Annotated[
        typing.Optional[ChatInstalledAppsItemTeamsApp],
        FieldMetadata(alias="teamsApp"),
        pydantic.Field(alias="teamsApp"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
