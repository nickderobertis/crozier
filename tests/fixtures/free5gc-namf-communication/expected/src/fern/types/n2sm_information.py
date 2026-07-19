

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent
from .snssai import Snssai


class N2SmInformation(UniversalBaseModel):
    pdu_session_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ]
    n2info_content: typing_extensions.Annotated[
        typing.Optional[N2InfoContent], FieldMetadata(alias="n2InfoContent"), pydantic.Field(alias="n2InfoContent")
    ] = None
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    subject_to_ho: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="subjectToHo"), pydantic.Field(alias="subjectToHo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
