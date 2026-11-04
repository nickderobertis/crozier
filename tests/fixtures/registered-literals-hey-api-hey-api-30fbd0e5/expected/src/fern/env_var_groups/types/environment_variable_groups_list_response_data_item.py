

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class EnvironmentVariableGroupsListResponseDataItem(UniversalBaseModel):
    """
    An environment variable group
    """

    name: str = pydantic.Field()
    """
    Name of the environment variable group
    """

    id: str = pydantic.Field()
    """
    The id of the group
    """

    org_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orgId"), pydantic.Field(alias="orgId", description="The id of the group")
    ]
    """
    The id of the group
    """

    count: int
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
