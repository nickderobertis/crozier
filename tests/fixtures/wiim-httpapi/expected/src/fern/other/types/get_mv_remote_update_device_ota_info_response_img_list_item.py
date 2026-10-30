

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem(UniversalBaseModel):
    img_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imgName"), pydantic.Field(alias="imgName", description="Image name")
    ] = None
    """
    Image name
    """

    img_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imgVersion"),
        pydantic.Field(alias="imgVersion", description="Image version"),
    ] = None
    """
    Image version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
