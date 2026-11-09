

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .role_detail import RoleDetail


class Role(UniversalBaseModel):
    """
    ADocumentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    role_detail: typing_extensions.Annotated[
        RoleDetail, FieldMetadata(alias="ROLE_DETAIL"), pydantic.Field(alias="ROLE_DETAIL")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
