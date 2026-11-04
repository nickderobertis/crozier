

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registration_schema_read_response_attributes import RegistrationSchemaReadResponseAttributes
from .registration_schema_read_response_links import RegistrationSchemaReadResponseLinks
from .registration_schema_read_response_relationships import RegistrationSchemaReadResponseRelationships


class RegistrationSchemaReadResponse(UniversalBaseModel):
    attributes: typing.Optional[RegistrationSchemaReadResponseAttributes] = pydantic.Field(default=None)
    """
    The attributes of the Registration Schema.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Registration Schema.
    """

    links: typing.Optional[RegistrationSchemaReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs that link to alternative representations of the Registration Schema.
    """

    relationships: typing.Optional[RegistrationSchemaReadResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the Registration Schema.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the Registration Schema (`registration-schemas`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
