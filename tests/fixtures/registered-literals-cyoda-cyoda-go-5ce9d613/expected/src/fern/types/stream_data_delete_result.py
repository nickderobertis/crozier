

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StreamDataDeleteResult(UniversalBaseModel):
    number_of_entitites: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfEntitites"), pydantic.Field(alias="numberOfEntitites")
    ] = None
    number_of_entitites_removed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfEntititesRemoved"),
        pydantic.Field(alias="numberOfEntititesRemoved"),
    ] = None
    id_to_error: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="idToError"), pydantic.Field(alias="idToError")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
