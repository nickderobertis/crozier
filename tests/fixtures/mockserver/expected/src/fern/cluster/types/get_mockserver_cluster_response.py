

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_mockserver_cluster_response_members_item import GetMockserverClusterResponseMembersItem


class GetMockserverClusterResponse(UniversalBaseModel):
    clustered: typing.Optional[bool] = None
    node_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")
    ] = None
    coordinator: typing.Optional[bool] = None
    cluster_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clusterName"), pydantic.Field(alias="clusterName")
    ] = None
    member_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="memberCount"), pydantic.Field(alias="memberCount")
    ] = None
    members: typing.Optional[typing.List[GetMockserverClusterResponseMembersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
