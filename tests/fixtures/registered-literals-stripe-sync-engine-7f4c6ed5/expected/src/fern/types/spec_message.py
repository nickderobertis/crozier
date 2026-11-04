

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .spec_message_spec import SpecMessageSpec


class SpecMessage(UniversalBaseModel):
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="_emitted_by"),
        pydantic.Field(
            alias="_emitted_by",
            description='Who emitted this message: "source/{type}", "destination/{type}", or "engine". Set by the engine.',
        ),
    ] = None
    """
    Who emitted this message: "source/{type}", "destination/{type}", or "engine". Set by the engine.
    """

    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="_ts"),
        pydantic.Field(alias="_ts", description="ISO 8601 timestamp when the engine observed this message."),
    ] = None
    """
    ISO 8601 timestamp when the engine observed this message.
    """

    spec: SpecMessageSpec = pydantic.Field()
    """
    JSON Schema describing the configuration a connector requires.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
