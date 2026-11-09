

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetPoliciesPolicyIdGroupsResponseItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    role: typing.Optional[str] = None
    group_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupLabel"), pydantic.Field(alias="groupLabel")
    ] = None
    group_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupName"), pydantic.Field(alias="groupName")
    ] = None
    active: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
