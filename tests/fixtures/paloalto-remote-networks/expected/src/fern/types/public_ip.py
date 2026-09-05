

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PublicIp(UniversalBaseModel):
    """
    Public IP to detect region
    """

    public_ip: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicIp"),
        pydantic.Field(alias="PublicIp", description="Public IP to detect region"),
    ] = None
    """
    Public IP to detect region
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
