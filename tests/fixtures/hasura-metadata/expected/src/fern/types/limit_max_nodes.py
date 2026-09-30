

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LimitMaxNodes(UniversalBaseModel):
    global_: typing_extensions.Annotated[float, FieldMetadata(alias="global"), pydantic.Field(alias="global")]
    per_role: typing.Optional[typing.Dict[str, float]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
