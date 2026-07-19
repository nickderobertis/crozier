

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GNbId(UniversalBaseModel):
    bit_length: typing_extensions.Annotated[int, FieldMetadata(alias="bitLength"), pydantic.Field(alias="bitLength")]
    g_nb_value: typing_extensions.Annotated[str, FieldMetadata(alias="gNBValue"), pydantic.Field(alias="gNBValue")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
