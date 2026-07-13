

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_craftables_destiny_craftable_socket_plug_component import (
    DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent,
)


class DestinyComponentsCraftablesDestinyCraftableSocketComponent(UniversalBaseModel):
    plug_set_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugSetHash")] = None
    plugs: typing.Optional[typing.List[DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent]] = (
        pydantic.Field(default=None)
    )
    """
    Unlock state for plugs in the socket plug set definition
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
