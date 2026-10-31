

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_stage import ImageStage
from .test_execution_relevant_link_create import TestExecutionRelevantLinkCreate
from .test_execution_status import TestExecutionStatus


class StartImageTestExecutionRequest(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-defined name identifying the artefact under test. Not unique - multiple versions/stages of the same artefact share this name. Examples: 'core22', 'ubuntu-desktop', 'snapd'
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version identifier of the artefact being tested. Format depends on artefact family - e.g., revisions for charms/snaps, version numbers for debs.
    """

    arch: typing.Optional[str] = pydantic.Field(default=None)
    """
    CPU architecture where tests will execute. Common values: 'amd64', 'arm64', 'armhf', 's390x', 'ppc64el'
    """

    environment: str = pydantic.Field()
    """
    Name of the test execution environment. This can identify the specific physical device, VM, or container where tests run or logical environment like a test lab or cloud region. Examples: 'cm3', 'rpi4', 'lxd-vm', 'aws-ec2'. The environment will be auto-created if it doesn't exist.
    """

    expected_environments: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Environment names expected for this artefact, resolved using this request's architecture. Only applied when this request creates the artefact.
    """

    ci_link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional URL linking to the CI job executing these tests. Useful for tracking test runs back to their automation source. Can be omitted.
    """

    test_plan: str = pydantic.Field()
    """
    Identifier for the test suite or plan executed. Groups related test results together - e.g., 'certification-24.04', 'smoke-tests', 'full-regression'. The test plan will be auto-created if it doesn't exist.
    """

    initial_status: typing.Optional[TestExecutionStatus] = pydantic.Field(default=None)
    """
    Initial status of the test execution. Default 'IN_PROGRESS' is appropriate for ongoing tests. Use 'COMPLETED' if test results will be uploaded separately.
    """

    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = pydantic.Field(default=None)
    """
    Optional list of additional URLs related to this test execution (e.g., bug reports, documentation, related PRs). Can be omitted or left empty.
    """

    needs_assignment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the artefact created from this test execution requires assignment of a reviewer. Set to true if test results need human review before the artefact can be promoted. Default false means no review assignment needed.
    """

    execution_stage: typing.Optional[ImageStage] = pydantic.Field(default=None)
    """
    Promotion stage of the image being tested. Options: 'pending' (awaiting approval), 'current' (approved and published). Use 'pending' for images undergoing testing before promotion.
    """

    os: typing.Optional[str] = pydantic.Field(default=None)
    """
    Operating system of the image. Examples: 'ubuntu', 'ubuntu-core', 'ubuntu-server'
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    OS release codename or version. Examples: 'focal', 'jammy', 'noble', '20.04', '22.04', '24.04'
    """

    sha256: str = pydantic.Field()
    """
    SHA256 checksum hash uniquely identifying this image build. Used to verify image integrity and uniqueness.
    """

    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    Team or organization responsible for the image. Examples: 'canonical', 'ubuntu-images', team names
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct URL where the image file can be downloaded or accessed. Should be a valid HTTP/HTTPS URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
