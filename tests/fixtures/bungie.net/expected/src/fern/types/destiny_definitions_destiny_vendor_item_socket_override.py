

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorItemSocketOverride(UniversalBaseModel):
    """
    The information for how the vendor purchase should override a given socket with custom plug data.
    """

    randomized_options_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="randomizedOptionsCount"),
        pydantic.Field(
            alias="randomizedOptionsCount",
            description="If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it's set to by default.",
        ),
    ] = None
    """
    If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it's set to by default.
    """

    single_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="singleItemHash"),
        pydantic.Field(
            alias="singleItemHash",
            description="If this is populated, the socket will be overridden with a specific plug.\r\nIf this isn't populated, it's being overridden by something more complicated that is only known by the Game Server and God, which means we can't tell you in advance what it'll be.",
        ),
    ] = None
    """
    If this is populated, the socket will be overridden with a specific plug.
    If this isn't populated, it's being overridden by something more complicated that is only known by the Game Server and God, which means we can't tell you in advance what it'll be.
    """

    socket_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketTypeHash"),
        pydantic.Field(
            alias="socketTypeHash",
            description="This appears to be used to select which socket ultimately gets the override defined here.",
        ),
    ] = None
    """
    This appears to be used to select which socket ultimately gets the override defined here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
