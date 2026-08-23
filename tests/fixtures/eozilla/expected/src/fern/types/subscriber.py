

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Subscriber(UniversalBaseModel):
    """
    Optional URIs for callbacks for this job.

    Support for this parameter is not required and the parameter may be
    removed from the API definition, if conformance class **'callback'**
    is not listed in the conformance declaration under `/conformance`.
    """

    success_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="successUri"), pydantic.Field(alias="successUri")
    ] = None
    in_progress_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inProgressUri"), pydantic.Field(alias="inProgressUri")
    ] = None
    failed_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="failedUri"), pydantic.Field(alias="failedUri")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
