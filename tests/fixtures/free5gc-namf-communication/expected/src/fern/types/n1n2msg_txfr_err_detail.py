

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .arp import Arp


class N1N2MsgTxfrErrDetail(UniversalBaseModel):
    retry_after: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="retryAfter"), pydantic.Field(alias="retryAfter")
    ] = None
    highest_prio_arp: typing_extensions.Annotated[
        typing.Optional[Arp], FieldMetadata(alias="highestPrioArp"), pydantic.Field(alias="highestPrioArp")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
