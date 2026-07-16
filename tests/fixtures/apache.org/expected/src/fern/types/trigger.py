

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Trigger(UniversalBaseModel):
    classpath: typing.Optional[str] = None
    created_date: typing.Optional[str] = None
    id: typing.Optional[int] = None
    kwargs_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kwargs"), pydantic.Field(alias="kwargs")
    ] = None
    triggerer_id: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
