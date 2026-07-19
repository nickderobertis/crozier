

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .key_amf import KeyAmf
from .ng_ksi import NgKsi


class SeafData(UniversalBaseModel):
    ng_ksi: typing_extensions.Annotated[NgKsi, FieldMetadata(alias="ngKsi"), pydantic.Field(alias="ngKsi")]
    key_amf: typing_extensions.Annotated[KeyAmf, FieldMetadata(alias="keyAmf"), pydantic.Field(alias="keyAmf")]
    nh: typing.Optional[str] = None
    ncc: typing.Optional[int] = None
    key_amf_change_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="keyAmfChangeInd"), pydantic.Field(alias="keyAmfChangeInd")
    ] = None
    key_amf_h_derivation_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="keyAmfHDerivationInd"), pydantic.Field(alias="keyAmfHDerivationInd")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
