

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_statement2 import ObStatement2


class ObReadDataStatement2(UniversalBaseModel):
    statement: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStatement2]], FieldMetadata(alias="Statement"), pydantic.Field(alias="Statement")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
