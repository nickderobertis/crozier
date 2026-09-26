

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_data_index_non_view_schema_key import ProjectDataIndexNonViewSchemaKey


class ProjectDataIndexNonView(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    schema_key: typing.Optional[ProjectDataIndexNonViewSchemaKey] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
