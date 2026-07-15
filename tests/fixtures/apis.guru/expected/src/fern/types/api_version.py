

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiVersion(UniversalBaseModel):
    added: dt.datetime = pydantic.Field()
    """
    Timestamp when the version was added
    """

    external_docs: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="externalDocs")
    ] = pydantic.Field(default=None)
    """
    Copy of `externalDocs` section from OpenAPI definition
    """

    info: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    Copy of `info` section from OpenAPI definition
    """

    link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the individual API entry for this API
    """

    openapi_ver: typing_extensions.Annotated[str, FieldMetadata(alias="openapiVer")] = pydantic.Field()
    """
    The value of the `openapi` or `swagger` property of the source definition
    """

    swagger_url: typing_extensions.Annotated[str, FieldMetadata(alias="swaggerUrl")] = pydantic.Field()
    """
    URL to OpenAPI definition in JSON format
    """

    swagger_yaml_url: typing_extensions.Annotated[str, FieldMetadata(alias="swaggerYamlUrl")] = pydantic.Field()
    """
    URL to OpenAPI definition in YAML format
    """

    updated: dt.datetime = pydantic.Field()
    """
    Timestamp when the version was updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
