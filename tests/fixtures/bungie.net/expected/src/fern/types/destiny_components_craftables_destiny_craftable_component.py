

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_craftables_destiny_craftable_socket_component import (
    DestinyComponentsCraftablesDestinyCraftableSocketComponent,
)


class DestinyComponentsCraftablesDestinyCraftableComponent(UniversalBaseModel):
    failed_requirement_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="failedRequirementIndexes")
    ] = pydantic.Field(default=None)
    """
    If the requirements are not met for crafting this item, these will index into the list of failure strings.
    """

    sockets: typing.Optional[typing.List[DestinyComponentsCraftablesDestinyCraftableSocketComponent]] = pydantic.Field(
        default=None
    )
    """
    Plug item state for the crafting sockets.
    """

    visible: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
