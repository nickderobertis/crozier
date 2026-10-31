

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_summary_details import ModelSummaryDetails


class ModelSummary(UniversalBaseModel):
    """
    Summary information for a locally available model
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model name
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model name
    """

    remote_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the upstream model, if the model is remote
    """

    remote_host: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the upstream Ollama host, if the model is remote
    """

    modified_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last modified timestamp in ISO 8601 format
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total size of the model on disk in bytes
    """

    digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 digest identifier of the model contents
    """

    details: typing.Optional[ModelSummaryDetails] = pydantic.Field(default=None)
    """
    Additional information about the model's format and family
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
