

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1project_with_database_response_output_database import V1ProjectWithDatabaseResponseOutputDatabase
from .v1project_with_database_response_output_status import V1ProjectWithDatabaseResponseOutputStatus


class V1ProjectWithDatabaseResponseOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Deprecated: Use `ref` instead.
    """

    ref: str = pydantic.Field()
    """
    Project ref
    """

    organization_id: str = pydantic.Field()
    """
    Deprecated: Use `organization_slug` instead.
    """

    organization_slug: str = pydantic.Field()
    """
    Organization slug
    """

    name: str = pydantic.Field()
    """
    Name of your project
    """

    region: str = pydantic.Field()
    """
    Region of your project
    """

    created_at: str = pydantic.Field()
    """
    Creation timestamp
    """

    status: V1ProjectWithDatabaseResponseOutputStatus
    database: V1ProjectWithDatabaseResponseOutputDatabase

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
