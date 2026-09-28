

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .key_to_multi_value_key_match_style_key_match_style import KeyToMultiValueKeyMatchStyleKeyMatchStyle


class KeyToMultiValueKeyMatchStyle(UniversalBaseModel):
    key_match_style: typing_extensions.Annotated[
        typing.Optional[KeyToMultiValueKeyMatchStyleKeyMatchStyle],
        FieldMetadata(alias="keyMatchStyle"),
        pydantic.Field(alias="keyMatchStyle"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
