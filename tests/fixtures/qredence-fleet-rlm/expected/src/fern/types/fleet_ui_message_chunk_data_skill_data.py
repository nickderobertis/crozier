

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fleet_ui_message_chunk_data_skill_data_phase import FleetUiMessageChunkDataSkillDataPhase


class FleetUiMessageChunkDataSkillData(UniversalBaseModel):
    skill_id: str
    name: str
    version: str
    phase: typing.Optional[FleetUiMessageChunkDataSkillDataPhase] = None
    trust: typing.Optional[str] = None
    affordances: typing.Optional[typing.List[str]] = None
    skill_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="skillId"), pydantic.Field(alias="skillId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
