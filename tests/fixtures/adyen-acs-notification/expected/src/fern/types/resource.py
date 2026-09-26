

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Resource(UniversalBaseModel):
    balance_platform: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balancePlatform"),
        pydantic.Field(alias="balancePlatform", description="The unique identifier of the balance platform."),
    ] = None
    """
    The unique identifier of the balance platform.
    """

    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationDate"),
        pydantic.Field(
            alias="creationDate",
            description="The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.",
        ),
    ] = None
    """
    The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
