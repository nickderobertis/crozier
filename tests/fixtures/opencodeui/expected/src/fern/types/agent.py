

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_mode import AgentMode
from .agent_model import AgentModel
from .permission_ruleset import PermissionRuleset


class Agent(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    mode: AgentMode
    native: typing.Optional[bool] = None
    hidden: typing.Optional[bool] = None
    top_p: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="topP"), pydantic.Field(alias="topP")
    ] = None
    temperature: typing.Optional[float] = None
    color: typing.Optional[str] = None
    permission: PermissionRuleset
    model: typing.Optional[AgentModel] = None
    prompt: typing.Optional[str] = None
    options: typing.Dict[str, typing.Any]
    steps: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
