

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .legacy_state import LegacyState


class PathMappingsLabel(UniversalBaseModel):
    """
    Content of "simcore.service.paths-mapping" label
    """

    inputs_path: str = pydantic.Field()
    """
    folder path where the service expects all the inputs
    """

    outputs_path: str = pydantic.Field()
    """
    folder path where the service is expected to provide all its outputs
    """

    state_paths: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    optional list of paths which contents need to be persisted
    """

    state_exclude: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    optional list unix shell rules used to exclude files from the state
    """

    volume_size_limits: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Apply volume size limits to entries in: `inputs_path`, `outputs_path` and `state_paths`. Limits must be parsable by Pydantic's ByteSize.
    """

    legacy_state: typing.Optional[LegacyState] = pydantic.Field(default=None)
    """
    if present, the service needs to first try to download the legacy statecoming from a different path.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
