

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListingSettingsNaming(enum.StrEnum):
    LISTING = "LISTING"
    LISTINGS = "LISTINGS"
    INTEGRATIONS = "INTEGRATIONS"
    APPS = "APPS"
    CONNECTORS = "CONNECTORS"
    DATASOURCES = "DATASOURCES"
    ADDONS = "ADDONS"
    PLUGINS = "PLUGINS"
    PARTNERS = "PARTNERS"
    CHANNELS = "CHANNELS"
    CONNECTIONS = "CONNECTIONS"
    EXTENSIONS = "EXTENSIONS"

    def visit(
        self,
        listing: typing.Callable[[], T_Result],
        listings: typing.Callable[[], T_Result],
        integrations: typing.Callable[[], T_Result],
        apps: typing.Callable[[], T_Result],
        connectors: typing.Callable[[], T_Result],
        datasources: typing.Callable[[], T_Result],
        addons: typing.Callable[[], T_Result],
        plugins: typing.Callable[[], T_Result],
        partners: typing.Callable[[], T_Result],
        channels: typing.Callable[[], T_Result],
        connections: typing.Callable[[], T_Result],
        extensions: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListingSettingsNaming.LISTING:
            return listing()
        if self is ListingSettingsNaming.LISTINGS:
            return listings()
        if self is ListingSettingsNaming.INTEGRATIONS:
            return integrations()
        if self is ListingSettingsNaming.APPS:
            return apps()
        if self is ListingSettingsNaming.CONNECTORS:
            return connectors()
        if self is ListingSettingsNaming.DATASOURCES:
            return datasources()
        if self is ListingSettingsNaming.ADDONS:
            return addons()
        if self is ListingSettingsNaming.PLUGINS:
            return plugins()
        if self is ListingSettingsNaming.PARTNERS:
            return partners()
        if self is ListingSettingsNaming.CHANNELS:
            return channels()
        if self is ListingSettingsNaming.CONNECTIONS:
            return connections()
        if self is ListingSettingsNaming.EXTENSIONS:
            return extensions()
