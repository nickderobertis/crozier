

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyModelPolicySubTypesItem(enum.StrEnum):
    RUN = "run"
    BUILD = "build"
    RUN_AND_BUILD = "run_and_build"
    AUDIT = "audit"
    DATA_CLASSIFICATION = "data_classification"
    DNS = "dns"
    MALWARE = "malware"
    NETWORK_EVENT = "network_event"
    NETWORK = "network"
    UEBA = "ueba"
    PERMISSIONS = "permissions"
    NETWORK_CONFIG = "network_config"
    IDENTITY = "identity"
    SENSITIVE_DATA_EXPOSURE = "sensitive_data_exposure"
    INTERNET_EXPOSURE = "internet_exposure"
    INJECTIONS = "injections"
    VULNERABILITY_SCANNING = "vulnerability_scanning"
    SHELLSHOCK = "shellshock"
    KNOWN_BOTS = "known_bots"
    UNKNOWN_BOTS = "unknown_bots"
    VIRTUAL_PATCHES = "virtual_patches"
    EVENT = "event"
    MISCONFIG_AND_EVENT = "misconfig_and_event"
    MISCONFIG = "misconfig"
    HOST = "host"
    CONTAINER_IMAGE = "container_image"

    def visit(
        self,
        run: typing.Callable[[], T_Result],
        build: typing.Callable[[], T_Result],
        run_and_build: typing.Callable[[], T_Result],
        audit: typing.Callable[[], T_Result],
        data_classification: typing.Callable[[], T_Result],
        dns: typing.Callable[[], T_Result],
        malware: typing.Callable[[], T_Result],
        network_event: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        ueba: typing.Callable[[], T_Result],
        permissions: typing.Callable[[], T_Result],
        network_config: typing.Callable[[], T_Result],
        identity: typing.Callable[[], T_Result],
        sensitive_data_exposure: typing.Callable[[], T_Result],
        internet_exposure: typing.Callable[[], T_Result],
        injections: typing.Callable[[], T_Result],
        vulnerability_scanning: typing.Callable[[], T_Result],
        shellshock: typing.Callable[[], T_Result],
        known_bots: typing.Callable[[], T_Result],
        unknown_bots: typing.Callable[[], T_Result],
        virtual_patches: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        misconfig_and_event: typing.Callable[[], T_Result],
        misconfig: typing.Callable[[], T_Result],
        host: typing.Callable[[], T_Result],
        container_image: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyModelPolicySubTypesItem.RUN:
            return run()
        if self is PolicyModelPolicySubTypesItem.BUILD:
            return build()
        if self is PolicyModelPolicySubTypesItem.RUN_AND_BUILD:
            return run_and_build()
        if self is PolicyModelPolicySubTypesItem.AUDIT:
            return audit()
        if self is PolicyModelPolicySubTypesItem.DATA_CLASSIFICATION:
            return data_classification()
        if self is PolicyModelPolicySubTypesItem.DNS:
            return dns()
        if self is PolicyModelPolicySubTypesItem.MALWARE:
            return malware()
        if self is PolicyModelPolicySubTypesItem.NETWORK_EVENT:
            return network_event()
        if self is PolicyModelPolicySubTypesItem.NETWORK:
            return network()
        if self is PolicyModelPolicySubTypesItem.UEBA:
            return ueba()
        if self is PolicyModelPolicySubTypesItem.PERMISSIONS:
            return permissions()
        if self is PolicyModelPolicySubTypesItem.NETWORK_CONFIG:
            return network_config()
        if self is PolicyModelPolicySubTypesItem.IDENTITY:
            return identity()
        if self is PolicyModelPolicySubTypesItem.SENSITIVE_DATA_EXPOSURE:
            return sensitive_data_exposure()
        if self is PolicyModelPolicySubTypesItem.INTERNET_EXPOSURE:
            return internet_exposure()
        if self is PolicyModelPolicySubTypesItem.INJECTIONS:
            return injections()
        if self is PolicyModelPolicySubTypesItem.VULNERABILITY_SCANNING:
            return vulnerability_scanning()
        if self is PolicyModelPolicySubTypesItem.SHELLSHOCK:
            return shellshock()
        if self is PolicyModelPolicySubTypesItem.KNOWN_BOTS:
            return known_bots()
        if self is PolicyModelPolicySubTypesItem.UNKNOWN_BOTS:
            return unknown_bots()
        if self is PolicyModelPolicySubTypesItem.VIRTUAL_PATCHES:
            return virtual_patches()
        if self is PolicyModelPolicySubTypesItem.EVENT:
            return event()
        if self is PolicyModelPolicySubTypesItem.MISCONFIG_AND_EVENT:
            return misconfig_and_event()
        if self is PolicyModelPolicySubTypesItem.MISCONFIG:
            return misconfig()
        if self is PolicyModelPolicySubTypesItem.HOST:
            return host()
        if self is PolicyModelPolicySubTypesItem.CONTAINER_IMAGE:
            return container_image()
