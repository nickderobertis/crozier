

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .supavisor_config_response_output_database_type import SupavisorConfigResponseOutputDatabaseType
from .supavisor_config_response_output_pool_mode import SupavisorConfigResponseOutputPoolMode


class SupavisorConfigResponseOutput(UniversalBaseModel):
    identifier: str
    database_type: SupavisorConfigResponseOutputDatabaseType
    is_using_scram_auth: bool
    db_user: str
    db_host: str
    db_port: int
    db_name: str
    connection_string: str
    connection_string: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionString"),
        pydantic.Field(alias="connectionString", description="Use connection_string instead"),
    ]
    """
    Use connection_string instead
    """

    default_pool_size: typing.Optional[int] = None
    max_client_conn: typing.Optional[int] = None
    pool_mode: SupavisorConfigResponseOutputPoolMode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
