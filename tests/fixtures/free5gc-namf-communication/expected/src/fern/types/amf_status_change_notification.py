

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amf_status_info import AmfStatusInfo


class AmfStatusChangeNotification(UniversalBaseModel):
    amf_status_info_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AmfStatusInfo]],
        FieldMetadata(alias="amfStatusInfoList"),
        pydantic.Field(alias="amfStatusInfoList"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
