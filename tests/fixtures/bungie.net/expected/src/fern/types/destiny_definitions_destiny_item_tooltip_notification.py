

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemTooltipNotification(UniversalBaseModel):
    display_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayString"), pydantic.Field(alias="displayString")
    ] = None
    display_style: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayStyle"), pydantic.Field(alias="displayStyle")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
