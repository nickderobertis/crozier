

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceApplication(UniversalBaseModel):
    """
    Provides information about the application used to generate a change.
    """

    application_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Read-only Square ID assigned to the application. Only used for
    [Product](https://developer.squareup.com/reference/square_2021-08-18/enums/Product) type `EXTERNAL_API`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Read-only display name assigned to the application
    (e.g. `"Custom Application"`, `"Square POS 4.74 for Android"`).
    """

    product: typing.Optional[str] = pydantic.Field(default=None)
    """
    Read-only [Product](https://developer.squareup.com/reference/square_2021-08-18/enums/Product) type for the application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
