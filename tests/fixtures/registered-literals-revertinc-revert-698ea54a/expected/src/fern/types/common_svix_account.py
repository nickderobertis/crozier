

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonSvixAccount(UniversalBaseModel):
    uid: typing.Optional[str] = None
    name: str
    rate_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="rateLimit"), pydantic.Field(alias="rateLimit")
    ] = None
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
