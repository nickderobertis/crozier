

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent


class NrppaInformation(UniversalBaseModel):
    nf_id: typing_extensions.Annotated[str, FieldMetadata(alias="nfId"), pydantic.Field(alias="nfId")]
    nrppa_pdu: typing_extensions.Annotated[
        N2InfoContent, FieldMetadata(alias="nrppaPdu"), pydantic.Field(alias="nrppaPdu")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
