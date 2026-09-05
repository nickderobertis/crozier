

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_service_get import NodeServiceGet
from .service_key_version import ServiceKeyVersion


class ProjectNodeServicesGet(UniversalBaseModel):
    project_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="projectUuid"), pydantic.Field(alias="projectUuid")
    ]
    services: typing.List[NodeServiceGet]
    missing: typing.Optional[typing.List[ServiceKeyVersion]] = pydantic.Field(default=None)
    """
    List of services defined in the project but that were not found in the catalog
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
