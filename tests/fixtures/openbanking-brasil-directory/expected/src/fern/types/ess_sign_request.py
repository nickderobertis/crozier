

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tn_c_id import TnCId


class EssSignRequest(UniversalBaseModel):
    no_of_signers: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="NoOfSigners"), pydantic.Field(alias="NoOfSigners")
    ] = None
    tn_c_id: typing_extensions.Annotated[
        typing.Optional[TnCId], FieldMetadata(alias="TnCId"), pydantic.Field(alias="TnCId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
