

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JsonSchemaResponseFormat(UniversalBaseModel):
    """
    Response format for JSON schema-based responses.
    """

    json_schema: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The JSON schema of the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
