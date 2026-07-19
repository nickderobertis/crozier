

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .guami import Guami
from .status_change import StatusChange


class AmfStatusInfo(UniversalBaseModel):
    guami_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Guami]], FieldMetadata(alias="guamiList"), pydantic.Field(alias="guamiList")
    ] = None
    status_change: typing_extensions.Annotated[
        StatusChange, FieldMetadata(alias="statusChange"), pydantic.Field(alias="statusChange")
    ]
    target_amf_removal: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetAmfRemoval"), pydantic.Field(alias="targetAmfRemoval")
    ] = None
    target_amf_failure: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetAmfFailure"), pydantic.Field(alias="targetAmfFailure")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
