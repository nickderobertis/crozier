

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_metadata_port_get_kind import ProjectMetadataPortGetKind


class ProjectMetadataPortGet(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Project port's unique identifier. Same as the UUID of the associated port node
    """

    kind: ProjectMetadataPortGetKind
    content_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    jsonschema for the port's value. SEE https://json-schema.org/understanding-json-schema/
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
