

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .control_plane_config_field import ControlPlaneConfigField


class ControlPlaneConfigChange(UniversalBaseModel):
    """
    One control-plane configuration snapshot and what changed in it.
    """

    configuration_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="configurationID"),
        pydantic.Field(alias="configurationID", description="The configuration snapshot."),
    ]
    """
    The configuration snapshot.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the change took effect."),
    ]
    """
    When the change took effect.
    """

    is_current: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isCurrent"),
        pydantic.Field(alias="isCurrent", description="Whether this is the cluster's current desired configuration."),
    ]
    """
    Whether this is the cluster's current desired configuration.
    """

    change_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="changeReason"),
        pydantic.Field(alias="changeReason", description="Why the snapshot was created, when recorded."),
    ] = None
    """
    Why the snapshot was created, when recorded.
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Who created the snapshot, when recorded."),
    ] = None
    """
    Who created the snapshot, when recorded.
    """

    changed_fields: typing_extensions.Annotated[
        typing.List[ControlPlaneConfigField],
        FieldMetadata(alias="changedFields"),
        pydantic.Field(
            alias="changedFields",
            description="Fields that changed relative to the previous snapshot. Empty for the first entry.",
        ),
    ]
    """
    Fields that changed relative to the previous snapshot. Empty for the first entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
