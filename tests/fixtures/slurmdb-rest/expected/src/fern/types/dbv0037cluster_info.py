

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037cluster_info_associations import Dbv0037ClusterInfoAssociations
from .dbv0037cluster_info_controller import Dbv0037ClusterInfoController
from .dbv0037response_tres import Dbv0037ResponseTres


class Dbv0037ClusterInfo(UniversalBaseModel):
    controller: typing.Optional[Dbv0037ClusterInfoController] = None
    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of cluster
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster name
    """

    nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned nodes
    """

    select_plugin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Configured select plugin
    """

    associations: typing.Optional[Dbv0037ClusterInfoAssociations] = None
    rpc_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number rpc version
    """

    tres: typing.Optional[typing.List[Dbv0037ResponseTres]] = pydantic.Field(default=None)
    """
    List of TRES in cluster
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
