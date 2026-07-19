

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .arp import Arp
from .ebi_arp_mapping import EbiArpMapping
from .eps_bearer_id import EpsBearerId


class AssignedEbiData(UniversalBaseModel):
    pdu_session_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ]
    assigned_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="assignedEbiList"),
        pydantic.Field(alias="assignedEbiList"),
    ] = None
    failed_arp_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Arp]], FieldMetadata(alias="failedArpList"), pydantic.Field(alias="failedArpList")
    ] = None
    released_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="releasedEbiList"),
        pydantic.Field(alias="releasedEbiList"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
