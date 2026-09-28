

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorReportingPanel(UniversalBaseModel):
    """
    A widget that displays a list of error groups.
    """

    project_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="projectNames"),
        pydantic.Field(
            alias="projectNames",
            description="The resource name of the Google Cloud Platform project. Written as projects/{projectID} or projects/{projectNumber}, where {projectID} and {projectNumber} can be found in the Google Cloud console (https://support.google.com/cloud/answer/6158840).Examples: projects/my-project-123, projects/5551234.",
        ),
    ] = None
    """
    The resource name of the Google Cloud Platform project. Written as projects/{projectID} or projects/{projectNumber}, where {projectID} and {projectNumber} can be found in the Google Cloud console (https://support.google.com/cloud/answer/6158840).Examples: projects/my-project-123, projects/5551234.
    """

    services: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An identifier of the service, such as the name of the executable, job, or Google App Engine service name. This field is expected to have a low number of values that are relatively stable over time, as opposed to version, which can be changed whenever new code is deployed.Contains the service name for error reports extracted from Google App Engine logs or default if the App Engine default service is used.
    """

    versions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Represents the source code version that the developer provided, which could represent a version label or a Git SHA-1 hash, for example. For App Engine standard environment, the version is set to the version of the app.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
