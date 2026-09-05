

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ACTIVITIES_INVITES_WRITE = "activities.invites.write"
    """
    allows your app to send activity invites - requires Discord approval (NOT REQUIRED FOR GAMESDK ACTIVITY MANAGER)
    """

    ACTIVITIES_READ = "activities.read"
    """
    allows your app to fetch data from a user's "Now Playing/Recently Played" list - requires Discord approval
    """

    ACTIVITIES_WRITE = "activities.write"
    """
    allows your app to update a user's activity - requires Discord approval (NOT REQUIRED FOR GAMESDK ACTIVITY MANAGER)
    """

    APPLICATIONS_BUILDS_READ = "applications.builds.read"
    """
    allows your app to read build data for a user's applications
    """

    APPLICATIONS_BUILDS_UPLOAD = "applications.builds.upload"
    """
    allows your app to upload/update builds for a user's applications - requires Discord approval
    """

    APPLICATIONS_COMMANDS = "applications.commands"
    """
    allows your app to use commands in a guild
    """

    APPLICATIONS_COMMANDS_PERMISSIONS_UPDATE = "applications.commands.permissions.update"
    """
    allows your app to update permissions for its commands in a guild a user has permissions to
    """

    APPLICATIONS_ENTITLEMENTS = "applications.entitlements"
    """
    allows your app to read entitlements for a user's applications
    """

    APPLICATIONS_STORE_UPDATE = "applications.store.update"
    """
    allows your app to read and update store data (SKUs, store listings, achievements, etc.) for a user's applications
    """

    BOT = "bot"
    """
    for oauth2 bots, this puts the bot in the user's selected guild by default
    """

    CONNECTIONS = "connections"
    """
    allows /users/@me/connections to return linked third-party accounts
    """

    DM_CHANNELS_READ = "dm_channels.read"
    """
    allows your app to see information about the user's DMs and group DMs - requires Discord approval
    """

    EMAIL = "email"
    """
    enables /users/@me to return an email
    """

    GDM_JOIN = "gdm.join"
    """
    allows your app to join users to a group dm
    """

    GUILDS = "guilds"
    """
    allows /users/@me/guilds to return basic information about all of a user's guilds
    """

    GUILDS_JOIN = "guilds.join"
    """
    allows /guilds/{guild.id}/members/{user.id} to be used for joining users to a guild
    """

    GUILDS_MEMBERS_READ = "guilds.members.read"
    """
    allows /users/@me/guilds/{guild.id}/member to return a user's member information in a guild
    """

    IDENTIFY = "identify"
    """
    allows /users/@me without email
    """

    MESSAGES_READ = "messages.read"
    """
    for local rpc server api access, this allows you to read messages from all client channels (otherwise restricted to channels/guilds your app creates)
    """

    OPENID = "openid"
    """
    for OpenID Connect, this allows your app to receive user id and basic profile information
    """

    RELATIONSHIPS_READ = "relationships.read"
    """
    allows your app to know a user's friends and implicit relationships - requires Discord approval
    """

    ROLE_CONNECTIONS_WRITE = "role_connections.write"
    """
    allows your app to update a user's connection and metadata for the app
    """

    RPC = "rpc"
    """
    for local rpc server access, this allows you to control a user's local Discord client - requires Discord approval
    """

    RPC_ACTIVITIES_WRITE = "rpc.activities.write"
    """
    for local rpc server access, this allows you to update a user's activity - requires Discord approval
    """

    RPC_NOTIFICATIONS_READ = "rpc.notifications.read"
    """
    for local rpc server access, this allows you to receive notifications pushed out to the user - requires Discord approval
    """

    RPC_SCREENSHARE_READ = "rpc.screenshare.read"
    """
    for local rpc server access, this allows you to read a user's screenshare status- requires Discord approval
    """

    RPC_SCREENSHARE_WRITE = "rpc.screenshare.write"
    """
    for local rpc server access, this allows you to update a user's screenshare settings- requires Discord approval
    """

    RPC_VIDEO_READ = "rpc.video.read"
    """
    for local rpc server access, this allows you to read a user's video status - requires Discord approval
    """

    RPC_VIDEO_WRITE = "rpc.video.write"
    """
    for local rpc server access, this allows you to update a user's video settings - requires Discord approval
    """

    RPC_VOICE_READ = "rpc.voice.read"
    """
    for local rpc server access, this allows you to read a user's voice settings and listen for voice events - requires Discord approval
    """

    RPC_VOICE_WRITE = "rpc.voice.write"
    """
    for local rpc server access, this allows you to update a user's voice settings - requires Discord approval
    """

    VOICE = "voice"
    """
    allows your app to connect to voice on user's behalf and see all the voice members - requires Discord approval
    """

    WEBHOOK_INCOMING = "webhook.incoming"
    """
    this generates a webhook that is returned in the oauth token response for authorization code grants
    """

    def visit(
        self,
        activities_invites_write: typing.Callable[[], T_Result],
        activities_read: typing.Callable[[], T_Result],
        activities_write: typing.Callable[[], T_Result],
        applications_builds_read: typing.Callable[[], T_Result],
        applications_builds_upload: typing.Callable[[], T_Result],
        applications_commands: typing.Callable[[], T_Result],
        applications_commands_permissions_update: typing.Callable[[], T_Result],
        applications_entitlements: typing.Callable[[], T_Result],
        applications_store_update: typing.Callable[[], T_Result],
        bot: typing.Callable[[], T_Result],
        connections: typing.Callable[[], T_Result],
        dm_channels_read: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        gdm_join: typing.Callable[[], T_Result],
        guilds: typing.Callable[[], T_Result],
        guilds_join: typing.Callable[[], T_Result],
        guilds_members_read: typing.Callable[[], T_Result],
        identify: typing.Callable[[], T_Result],
        messages_read: typing.Callable[[], T_Result],
        openid: typing.Callable[[], T_Result],
        relationships_read: typing.Callable[[], T_Result],
        role_connections_write: typing.Callable[[], T_Result],
        rpc: typing.Callable[[], T_Result],
        rpc_activities_write: typing.Callable[[], T_Result],
        rpc_notifications_read: typing.Callable[[], T_Result],
        rpc_screenshare_read: typing.Callable[[], T_Result],
        rpc_screenshare_write: typing.Callable[[], T_Result],
        rpc_video_read: typing.Callable[[], T_Result],
        rpc_video_write: typing.Callable[[], T_Result],
        rpc_voice_read: typing.Callable[[], T_Result],
        rpc_voice_write: typing.Callable[[], T_Result],
        voice: typing.Callable[[], T_Result],
        webhook_incoming: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ACTIVITIES_INVITES_WRITE:
            return activities_invites_write()
        if self is OauthScope.ACTIVITIES_READ:
            return activities_read()
        if self is OauthScope.ACTIVITIES_WRITE:
            return activities_write()
        if self is OauthScope.APPLICATIONS_BUILDS_READ:
            return applications_builds_read()
        if self is OauthScope.APPLICATIONS_BUILDS_UPLOAD:
            return applications_builds_upload()
        if self is OauthScope.APPLICATIONS_COMMANDS:
            return applications_commands()
        if self is OauthScope.APPLICATIONS_COMMANDS_PERMISSIONS_UPDATE:
            return applications_commands_permissions_update()
        if self is OauthScope.APPLICATIONS_ENTITLEMENTS:
            return applications_entitlements()
        if self is OauthScope.APPLICATIONS_STORE_UPDATE:
            return applications_store_update()
        if self is OauthScope.BOT:
            return bot()
        if self is OauthScope.CONNECTIONS:
            return connections()
        if self is OauthScope.DM_CHANNELS_READ:
            return dm_channels_read()
        if self is OauthScope.EMAIL:
            return email()
        if self is OauthScope.GDM_JOIN:
            return gdm_join()
        if self is OauthScope.GUILDS:
            return guilds()
        if self is OauthScope.GUILDS_JOIN:
            return guilds_join()
        if self is OauthScope.GUILDS_MEMBERS_READ:
            return guilds_members_read()
        if self is OauthScope.IDENTIFY:
            return identify()
        if self is OauthScope.MESSAGES_READ:
            return messages_read()
        if self is OauthScope.OPENID:
            return openid()
        if self is OauthScope.RELATIONSHIPS_READ:
            return relationships_read()
        if self is OauthScope.ROLE_CONNECTIONS_WRITE:
            return role_connections_write()
        if self is OauthScope.RPC:
            return rpc()
        if self is OauthScope.RPC_ACTIVITIES_WRITE:
            return rpc_activities_write()
        if self is OauthScope.RPC_NOTIFICATIONS_READ:
            return rpc_notifications_read()
        if self is OauthScope.RPC_SCREENSHARE_READ:
            return rpc_screenshare_read()
        if self is OauthScope.RPC_SCREENSHARE_WRITE:
            return rpc_screenshare_write()
        if self is OauthScope.RPC_VIDEO_READ:
            return rpc_video_read()
        if self is OauthScope.RPC_VIDEO_WRITE:
            return rpc_video_write()
        if self is OauthScope.RPC_VOICE_READ:
            return rpc_voice_read()
        if self is OauthScope.RPC_VOICE_WRITE:
            return rpc_voice_write()
        if self is OauthScope.VOICE:
            return voice()
        if self is OauthScope.WEBHOOK_INCOMING:
            return webhook_incoming()
