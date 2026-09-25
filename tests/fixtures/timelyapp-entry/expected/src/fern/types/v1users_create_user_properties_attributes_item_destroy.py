

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V1UsersCreateUserPropertiesAttributesItemDestroy(UniversalBaseModel):
    id: int
    destroy: typing_extensions.Annotated[bool, FieldMetadata(alias="_destroy"), pydantic.Field(alias="_destroy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
