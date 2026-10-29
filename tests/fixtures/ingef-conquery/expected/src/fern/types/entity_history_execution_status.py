

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .entity_history_execution_status_infos_item import EntityHistoryExecutionStatusInfosItem
from .entity_history_execution_status_time_stratified_infos_item import (
    EntityHistoryExecutionStatusTimeStratifiedInfosItem,
)
from .full_execution_status import FullExecutionStatus


class EntityHistoryExecutionStatus(FullExecutionStatus):
    """
    Specific execution info for a entity-preview, containing additional information for the entity.
    """

    infos: typing.Optional[typing.List[EntityHistoryExecutionStatusInfosItem]] = pydantic.Field(default=None)
    """
    Auxiliary information to the entity.
    """

    time_stratified_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[EntityHistoryExecutionStatusTimeStratifiedInfosItem]],
        FieldMetadata(alias="timeStratifiedInfos"),
        pydantic.Field(
            alias="timeStratifiedInfos",
            description="Results stratified in time for every year and quarter for selects defined in PreviewConfig.timeStratifiedSelects of queried time.",
        ),
    ] = None
    """
    Results stratified in time for every year and quarter for selects defined in PreviewConfig.timeStratifiedSelects of queried time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
