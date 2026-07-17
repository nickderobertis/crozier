

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_account6 import ObAccount6


class ObReadAccount6Data(UniversalBaseModel):
    account: typing_extensions.Annotated[
        typing.Optional[typing.List[ObAccount6]], FieldMetadata(alias="Account"), pydantic.Field(alias="Account")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
