

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SbiLs(UniversalBaseModel):
    db_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DB_ID"),
        pydantic.Field(alias="DB_ID", description="The uuid of the component used by katana DB"),
    ] = None
    """
    The uuid of the component used by katana DB
    """

    component_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Component_ID"),
        pydantic.Field(
            alias="Component_ID", description="The uuid of the component as registered to katana by the admin"
        ),
    ] = None
    """
    The uuid of the component as registered to katana by the admin
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="created at"),
        pydantic.Field(alias="created at", description="Creation time of the component"),
    ] = None
    """
    Creation time of the component
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the component
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
