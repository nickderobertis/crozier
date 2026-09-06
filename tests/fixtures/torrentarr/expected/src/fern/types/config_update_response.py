

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .config_update_response_reload_type import ConfigUpdateResponseReloadType


class ConfigUpdateResponse(UniversalBaseModel):
    affected_instances: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="affectedInstances"),
        pydantic.Field(
            alias="affectedInstances", description="Arr instance section names reloaded (single_arr / multi_arr only)."
        ),
    ]
    """
    Arr instance section names reloaded (single_arr / multi_arr only).
    """

    config_reloaded: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="configReloaded"),
        pydantic.Field(
            alias="configReloaded",
            description="True when any backend reload action ran (excludes frontend-only changes).",
        ),
    ]
    """
    True when any backend reload action ran (excludes frontend-only changes).
    """

    reload_type: typing_extensions.Annotated[
        ConfigUpdateResponseReloadType,
        FieldMetadata(alias="reloadType"),
        pydantic.Field(alias="reloadType", description="Reload strategy applied after saving config changes."),
    ]
    """
    Reload strategy applied after saving config changes.
    """

    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
