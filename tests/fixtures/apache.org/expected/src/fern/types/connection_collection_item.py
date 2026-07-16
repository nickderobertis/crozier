

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConnectionCollectionItem(UniversalBaseModel):
    """
    Connection collection item.
    The password and extra fields are only available when retrieving a single object due to the sensitivity of this data.
    """

    conn_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The connection type.
    """

    connection_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The connection ID.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the connection.
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    Host of the connection.
    """

    login: typing.Optional[str] = pydantic.Field(default=None)
    """
    Login of the connection.
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Port of the connection.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Schema of the connection."),
    ] = None
    """
    Schema of the connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
