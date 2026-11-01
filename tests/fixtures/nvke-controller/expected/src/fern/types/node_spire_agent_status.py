

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NodeSpireAgentStatus(UniversalBaseModel):
    """
    One node's SPIRE agent, as reported live by its node agent.
    """

    node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="nodeID"), pydantic.Field(alias="nodeID", description="Node ID.")
    ]
    """
    Node ID.
    """

    name: str = pydantic.Field()
    """
    Node name.
    """

    reachable: bool = pydantic.Field()
    """
    The node agent answered. When false, only `message` is set.
    """

    server_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serverAddress"),
        pydantic.Field(alias="serverAddress", description="SPIRE server address in the node's agent config."),
    ] = None
    """
    SPIRE server address in the node's agent config.
    """

    server_port: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="serverPort"),
        pydantic.Field(alias="serverPort", description="SPIRE server port in the node's agent config."),
    ] = None
    """
    SPIRE server port in the node's agent config.
    """

    has_valid_svid: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasValidSVID"),
        pydantic.Field(
            alias="hasValidSVID",
            description="The running SPIRE agent uses the config above and serves an\nunexpired X.509 SVID, so it holds a certificate from that server.",
        ),
    ]
    """
    The running SPIRE agent uses the config above and serves an
    unexpired X.509 SVID, so it holds a certificate from that server.
    """

    svid_expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="svidExpiresAt"),
        pydantic.Field(alias="svidExpiresAt", description="Expiry of that SVID."),
    ] = None
    """
    Expiry of that SVID.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Why the node is unreachable or has no valid SVID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
