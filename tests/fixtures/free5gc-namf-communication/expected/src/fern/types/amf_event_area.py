

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ladn_info import LadnInfo
from .presence_info import PresenceInfo


class AmfEventArea(UniversalBaseModel):
    presence_info: typing_extensions.Annotated[
        typing.Optional[PresenceInfo], FieldMetadata(alias="presenceInfo"), pydantic.Field(alias="presenceInfo")
    ] = None
    ladn_info: typing_extensions.Annotated[
        typing.Optional[LadnInfo], FieldMetadata(alias="ladnInfo"), pydantic.Field(alias="ladnInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
