

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_party2 import ObParty2


class ObReadParty2Data(UniversalBaseModel):
    party: typing_extensions.Annotated[
        typing.Optional[ObParty2], FieldMetadata(alias="Party"), pydantic.Field(alias="Party")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
