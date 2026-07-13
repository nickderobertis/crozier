

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_craftables_destiny_craftable_component import (
    DestinyComponentsCraftablesDestinyCraftableComponent,
)


class DestinyComponentsCraftablesDestinyCraftablesComponent(UniversalBaseModel):
    craftables: typing.Optional[typing.Dict[str, DestinyComponentsCraftablesDestinyCraftableComponent]] = (
        pydantic.Field(default=None)
    )
    """
    A map of craftable item hashes to craftable item state components.
    """

    crafting_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="craftingRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of craftable item categories.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
