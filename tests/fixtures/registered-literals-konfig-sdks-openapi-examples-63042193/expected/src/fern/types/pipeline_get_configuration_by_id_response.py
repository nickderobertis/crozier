

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PipelineGetConfigurationByIdResponse(UniversalBaseModel):
    """
    The configuration strings for the pipeline.
    """

    source: str = pydantic.Field()
    """
    The source configuration for the pipeline, before any config compilation has been performed. If there is no config, then this field will be empty.
    """

    compiled: str = pydantic.Field()
    """
    The compiled configuration for the pipeline, after all orb expansion has been performed. If there were errors processing the pipeline's configuration, then this field may be empty.
    """

    setup_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="setup-config"),
        pydantic.Field(
            alias="setup-config",
            description="The setup configuration for the pipeline used for Setup Workflows. If there were errors processing the pipeline's configuration or if setup workflows are not enabled, then this field should not exist",
        ),
    ] = None
    """
    The setup configuration for the pipeline used for Setup Workflows. If there were errors processing the pipeline's configuration or if setup workflows are not enabled, then this field should not exist
    """

    compiled_setup_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="compiled-setup-config"),
        pydantic.Field(
            alias="compiled-setup-config",
            description="The compiled setup configuration for the pipeline, after all orb expansion has been performed. If there were errors processing the pipeline's setup workflows, then this field may be empty.",
        ),
    ] = None
    """
    The compiled setup configuration for the pipeline, after all orb expansion has been performed. If there were errors processing the pipeline's setup workflows, then this field may be empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
