

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ControlPlaneRolloutChange(UniversalBaseModel):
    """
    One rollout-relevant field whose pinned value differs from the desired value, as plain strings.
    """

    field: str = pydantic.Field()
    """
    The rollout-relevant field that changed (e.g. kubernetesVersion, release).
    """

    from_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="The value the node is currently pinned to."),
    ]
    """
    The value the node is currently pinned to.
    """

    to: str = pydantic.Field()
    """
    The cluster's desired value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
