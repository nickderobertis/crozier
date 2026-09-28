

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfilesNetwork(enum.StrEnum):
    """
    The network the profile exists on
    """

    ABOUTME = "aboutme"
    ANGELLIST = "angellist"
    BEHANCE = "behance"
    CRUNCHBASE = "crunchbase"
    DRIBBBLE = "dribbble"
    ELLO = "ello"
    FACEBOOK = "facebook"
    FLICKR = "flickr"
    FOURSQUARE = "foursquare"
    GITHUB = "github"
    GITLAB = "gitlab"
    GOOGLE = "google"
    GRAVATAR = "gravatar"
    INDEED = "indeed"
    INSTAGRAM = "instagram"
    KLOUT = "klout"
    LINKEDIN = "linkedin"
    LINKEDIN_SALES_NAVIGATOR = "linkedin_sales_navigator"
    MEDIUM = "medium"
    MEETUP = "meetup"
    MYSPACE = "myspace"
    PINTEREST = "pinterest"
    QUORA = "quora"
    REDDIT = "reddit"
    SOUNDCLOUD = "soundcloud"
    STACKOVERFLOW = "stackoverflow"
    TWITTER = "twitter"
    VIMEO = "vimeo"
    WORDPRESS = "wordpress"
    XING = "xing"
    YOUTUBE = "youtube"

    def visit(
        self,
        aboutme: typing.Callable[[], T_Result],
        angellist: typing.Callable[[], T_Result],
        behance: typing.Callable[[], T_Result],
        crunchbase: typing.Callable[[], T_Result],
        dribbble: typing.Callable[[], T_Result],
        ello: typing.Callable[[], T_Result],
        facebook: typing.Callable[[], T_Result],
        flickr: typing.Callable[[], T_Result],
        foursquare: typing.Callable[[], T_Result],
        github: typing.Callable[[], T_Result],
        gitlab: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
        gravatar: typing.Callable[[], T_Result],
        indeed: typing.Callable[[], T_Result],
        instagram: typing.Callable[[], T_Result],
        klout: typing.Callable[[], T_Result],
        linkedin: typing.Callable[[], T_Result],
        linkedin_sales_navigator: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        meetup: typing.Callable[[], T_Result],
        myspace: typing.Callable[[], T_Result],
        pinterest: typing.Callable[[], T_Result],
        quora: typing.Callable[[], T_Result],
        reddit: typing.Callable[[], T_Result],
        soundcloud: typing.Callable[[], T_Result],
        stackoverflow: typing.Callable[[], T_Result],
        twitter: typing.Callable[[], T_Result],
        vimeo: typing.Callable[[], T_Result],
        wordpress: typing.Callable[[], T_Result],
        xing: typing.Callable[[], T_Result],
        youtube: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProfilesNetwork.ABOUTME:
            return aboutme()
        if self is ProfilesNetwork.ANGELLIST:
            return angellist()
        if self is ProfilesNetwork.BEHANCE:
            return behance()
        if self is ProfilesNetwork.CRUNCHBASE:
            return crunchbase()
        if self is ProfilesNetwork.DRIBBBLE:
            return dribbble()
        if self is ProfilesNetwork.ELLO:
            return ello()
        if self is ProfilesNetwork.FACEBOOK:
            return facebook()
        if self is ProfilesNetwork.FLICKR:
            return flickr()
        if self is ProfilesNetwork.FOURSQUARE:
            return foursquare()
        if self is ProfilesNetwork.GITHUB:
            return github()
        if self is ProfilesNetwork.GITLAB:
            return gitlab()
        if self is ProfilesNetwork.GOOGLE:
            return google()
        if self is ProfilesNetwork.GRAVATAR:
            return gravatar()
        if self is ProfilesNetwork.INDEED:
            return indeed()
        if self is ProfilesNetwork.INSTAGRAM:
            return instagram()
        if self is ProfilesNetwork.KLOUT:
            return klout()
        if self is ProfilesNetwork.LINKEDIN:
            return linkedin()
        if self is ProfilesNetwork.LINKEDIN_SALES_NAVIGATOR:
            return linkedin_sales_navigator()
        if self is ProfilesNetwork.MEDIUM:
            return medium()
        if self is ProfilesNetwork.MEETUP:
            return meetup()
        if self is ProfilesNetwork.MYSPACE:
            return myspace()
        if self is ProfilesNetwork.PINTEREST:
            return pinterest()
        if self is ProfilesNetwork.QUORA:
            return quora()
        if self is ProfilesNetwork.REDDIT:
            return reddit()
        if self is ProfilesNetwork.SOUNDCLOUD:
            return soundcloud()
        if self is ProfilesNetwork.STACKOVERFLOW:
            return stackoverflow()
        if self is ProfilesNetwork.TWITTER:
            return twitter()
        if self is ProfilesNetwork.VIMEO:
            return vimeo()
        if self is ProfilesNetwork.WORDPRESS:
            return wordpress()
        if self is ProfilesNetwork.XING:
            return xing()
        if self is ProfilesNetwork.YOUTUBE:
            return youtube()
