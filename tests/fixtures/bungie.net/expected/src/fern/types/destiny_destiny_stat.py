

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDestinyStat(UniversalBaseModel):
    """
    Represents a stat on an item *or* Character (NOT a Historical Stat, but a physical attribute stat like Attack, Defense etc...)
    """

    stat_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="statHash"),
        pydantic.Field(
            alias="statHash",
            description="The hash identifier for the Stat. Use it to look up the DestinyStatDefinition for static data about the stat.",
        ),
    ] = None
    """
    The hash identifier for the Stat. Use it to look up the DestinyStatDefinition for static data about the stat.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current value of the Stat.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
