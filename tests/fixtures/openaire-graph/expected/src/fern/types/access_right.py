

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_right_open_access_route import AccessRightOpenAccessRoute


class AccessRight(UniversalBaseModel):
    code: typing.Optional[str] = None
    label: typing.Optional[str] = None
    scheme: typing.Optional[str] = None
    open_access_route: typing_extensions.Annotated[
        typing.Optional[AccessRightOpenAccessRoute],
        FieldMetadata(alias="openAccessRoute"),
        pydantic.Field(alias="openAccessRoute"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
