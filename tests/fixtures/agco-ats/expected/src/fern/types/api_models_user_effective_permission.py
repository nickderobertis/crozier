

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsUserEffectivePermission(UniversalBaseModel):
    permission_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="PermissionId"), pydantic.Field(alias="PermissionId")
    ] = None
    permission_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PermissionName"), pydantic.Field(alias="PermissionName")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
