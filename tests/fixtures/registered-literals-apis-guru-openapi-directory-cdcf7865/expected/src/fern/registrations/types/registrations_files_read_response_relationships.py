

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationsFilesReadResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    checkout: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the user who checked out the file.
    """

    comments: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the comments on the file.
    """

    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node the file is on.
    """

    versions: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the versions of the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
