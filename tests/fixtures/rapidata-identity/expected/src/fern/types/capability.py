

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Capability(enum.StrEnum):
    """
    The named platform-wide capability entitlements a customer can be granted. Each maps to a
    `capability` object in the authorization graph; convert to its object id with
    string CapabilityExtensions.ToObjectId(Capability capability). Kept as a typed enum so
    capability grants read explicitly at call sites (and, later, on endpoint contracts) instead of
    passing raw id strings around.
    """

    SKIP_CONTENT_CHECK = "SkipContentCheck"
    PREHEAT_BOOST = "PreheatBoost"
    MANAGED_IMAGE_FAUCET = "ManagedImageFaucet"
    REQUEST_FEATURES = "RequestFeatures"
    RUN_EXPERIMENTS = "RunExperiments"
    MANAGED_FORGE_FAUCET = "ManagedForgeFaucet"
    UPLOAD_LONG_MEDIA = "UploadLongMedia"

    def visit(
        self,
        skip_content_check: typing.Callable[[], T_Result],
        preheat_boost: typing.Callable[[], T_Result],
        managed_image_faucet: typing.Callable[[], T_Result],
        request_features: typing.Callable[[], T_Result],
        run_experiments: typing.Callable[[], T_Result],
        managed_forge_faucet: typing.Callable[[], T_Result],
        upload_long_media: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Capability.SKIP_CONTENT_CHECK:
            return skip_content_check()
        if self is Capability.PREHEAT_BOOST:
            return preheat_boost()
        if self is Capability.MANAGED_IMAGE_FAUCET:
            return managed_image_faucet()
        if self is Capability.REQUEST_FEATURES:
            return request_features()
        if self is Capability.RUN_EXPERIMENTS:
            return run_experiments()
        if self is Capability.MANAGED_FORGE_FAUCET:
            return managed_forge_faucet()
        if self is Capability.UPLOAD_LONG_MEDIA:
            return upload_long_media()
