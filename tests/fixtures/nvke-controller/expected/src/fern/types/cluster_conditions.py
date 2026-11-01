

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .certificate_renewal_status import CertificateRenewalStatus
from .condition import Condition
from .etcd_key_rotation_status import EtcdKeyRotationStatus
from .update_in_progress import UpdateInProgress


class ClusterConditions(UniversalBaseModel):
    """
    Lifecycle conditions of a cluster. Each is a Condition.
    """

    provisioning: Condition = pydantic.Field()
    """
    The cluster is provisioning.
    """

    provisioned: Condition = pydantic.Field()
    """
    The cluster is provisioned.
    """

    deleting: Condition = pydantic.Field()
    """
    The cluster is being deleted.
    """

    cp_nodes_recycling: typing_extensions.Annotated[
        typing.Optional[Condition],
        FieldMetadata(alias="cpNodesRecycling"),
        pydantic.Field(alias="cpNodesRecycling", description="Control-plane nodes are being replaced."),
    ] = None
    """
    Control-plane nodes are being replaced.
    """

    control_plane_upgrading: typing_extensions.Annotated[
        typing.Optional[Condition],
        FieldMetadata(alias="controlPlaneUpgrading"),
        pydantic.Field(alias="controlPlaneUpgrading", description="The control plane is being upgraded."),
    ] = None
    """
    The control plane is being upgraded.
    """

    update_in_progress: typing_extensions.Annotated[
        typing.Optional[UpdateInProgress],
        FieldMetadata(alias="updateInProgress"),
        pydantic.Field(
            alias="updateInProgress",
            description="The mutually exclusive cluster operation in progress, if any. Absent when none.",
        ),
    ] = None
    """
    The mutually exclusive cluster operation in progress, if any. Absent when none.
    """

    update_failed: typing_extensions.Annotated[
        typing.Optional[Condition],
        FieldMetadata(alias="updateFailed"),
        pydantic.Field(alias="updateFailed", description="The most recent cluster update failed."),
    ] = None
    """
    The most recent cluster update failed.
    """

    certificate_renewal: typing_extensions.Annotated[
        typing.Optional[CertificateRenewalStatus],
        FieldMetadata(alias="certificateRenewal"),
        pydantic.Field(
            alias="certificateRenewal",
            description="The accepted, succeeded, or failed state of the most recent certificate-renewal cycle.",
        ),
    ] = None
    """
    The accepted, succeeded, or failed state of the most recent certificate-renewal cycle.
    """

    etcd_key_rotation: typing_extensions.Annotated[
        typing.Optional[EtcdKeyRotationStatus],
        FieldMetadata(alias="etcdKeyRotation"),
        pydantic.Field(
            alias="etcdKeyRotation",
            description="The most recent etcd data-encryption-key rotation, including retained ownership after failure.",
        ),
    ] = None
    """
    The most recent etcd data-encryption-key rotation, including retained ownership after failure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
