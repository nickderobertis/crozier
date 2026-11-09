

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TechnicalUserDto(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="The client identifier for the M2M client"),
    ]
    """
    The client identifier for the M2M client
    """

    creation_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="creationDate"),
        pydantic.Field(alias="creationDate", description="The date and time when the M2M client was created"),
    ]
    """
    The date and time when the M2M client was created
    """

    last_update_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastUpdateDate"),
        pydantic.Field(alias="lastUpdateDate", description="The date and time when the M2M client was last updated"),
    ]
    """
    The date and time when the M2M client was last updated
    """

    roles: typing.List[str] = pydantic.Field()
    """
    The roles assigned to the M2M client
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
