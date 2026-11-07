

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SchemaResponseActionReadResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the Schema Response Action entity.
    """

    creator: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node the file is on.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node the file is on.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
