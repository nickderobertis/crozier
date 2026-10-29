

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .select_id import SelectId


class PreviewConfigInfoCardSelectsItem(UniversalBaseModel):
    select_id: typing_extensions.Annotated[
        typing.Optional[SelectId], FieldMetadata(alias="selectId"), pydantic.Field(alias="selectId")
    ] = None
    description: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
