

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationSchemaReadResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the Registration Schema.
    """

    schema_blocks: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of schema blocks that contain the question prompt information for the Registration Schema.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
