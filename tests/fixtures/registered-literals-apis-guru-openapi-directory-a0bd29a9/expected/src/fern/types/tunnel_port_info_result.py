

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TunnelPortInfoResult(UniversalBaseModel):
    port_visibility: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="portVisibility"), pydantic.Field(alias="portVisibility")
    ] = None
    tunnel_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tunnelToken"), pydantic.Field(alias="tunnelToken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
