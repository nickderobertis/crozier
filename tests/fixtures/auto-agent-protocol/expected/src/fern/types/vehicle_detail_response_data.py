

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vehicle_detail_response_data_condition import VehicleDetailResponseDataCondition
from .vehicle_status import VehicleStatus


class VehicleDetailResponseData(UniversalBaseModel):
    condition: typing.Optional[VehicleDetailResponseDataCondition] = pydantic.Field(default=None)
    """
    Combined condition enum spanning both sale-condition and trade-in-condition vocabularies. For inventory listings and vehicle_of_interest use one of `new` | `used` | `cpo` (Certified Pre-Owned). For trade_in use one of `excellent` | `good` | `fair` | `poor`. The using schema enforces the correct subset by context.
    """

    vin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Vehicle Identification Number (17 chars, ISO 3779). Optional on trade-ins; recommended on inventory listings of used vehicles.
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    Model year (e.g. 2024).
    """

    make: typing.Optional[str] = pydantic.Field(default=None)
    """
    Vehicle make / manufacturer brand (e.g. 'Honda', 'BMW', 'Ford').
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Vehicle model name (e.g. 'CR-V', '3 Series', 'F-150').
    """

    trim: typing.Optional[str] = pydantic.Field(default=None)
    """
    Trim level (e.g. 'EX-L', 'M Sport', 'Lariat').
    """

    status: typing.Optional[VehicleStatus] = pydantic.Field(default=None)
    """
    Inventory availability. v1.0 supports exactly three values: `available` (in stock now), `intransit` (allocated / en route to the dealership), `pending` (deal in progress). A vehicle in any other state is OUT OF STOCK and MUST NOT appear in inventory feeds — dealers omit it and buyer agents ignore any item missing or carrying an unknown status. Required on inventory listings; omitted on vehicle_of_interest and trade_in.
    """

    rooftop: typing.Optional[str] = pydantic.Field(default=None)
    """
    Which dealership location/rooftop holds this vehicle, identified by the rooftop's `name` from dealer.information. Nullable; single-rooftop dealers MAY leave it null.
    """

    msrp: typing.Optional[int] = pydantic.Field(default=None)
    """
    Manufacturer's Suggested Retail Price (sticker price), whole US dollars. Inventory context.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    FTC-emphasized FINAL out-the-door price after all incentives, mandatory fees, and required add-ons, in whole US dollars. Per FTC enforcement (CARS Rule), this field MUST reflect the total amount the buyer would pay; advertising a 'price' that excludes required fees or omits required add-ons is a violation. Inventory context.
    """

    list_price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Dealer's advertised list price; the base price BEFORE incentives, taxes, or fees, in whole US dollars. Inventory context.
    """

    offered_price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Regional price equal to list_price plus applicable taxes for the buyer's `zip`, in whole US dollars, when the dealer enables desking. Present only if a `zip` is supplied AND the dealer supports regional pricing. Inventory context.
    """

    zip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Buyer ZIP code used to compute regional pricing fields (`offered_price`). US ZIP, 5 digits or ZIP+4. Optional; when absent, regional pricing fields MUST be omitted.
    """

    stock: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dealer's stock number for this unit. Inventory and vehicle_of_interest contexts.
    """

    dealer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stable identifier of the dealer that owns this listing. Inventory context.
    """

    vehicle_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dealer-internal identifier when the vehicle is not yet VIN-decoded (e.g. an in-transit unit).
    """

    mileage: typing.Optional[int] = pydantic.Field(default=None)
    """
    Odometer reading in miles. Required for trade-ins; typical on used inventory.
    """

    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    Body style as text (e.g. 'sedan', 'suv', 'truck', 'coupe', 'hatchback', 'wagon', 'minivan', 'convertible').
    """

    transmission: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transmission type as text (e.g. 'automatic', 'manual', '8-speed automatic', 'cvt').
    """

    driveline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Drivetrain layout (e.g. 'fwd', 'rwd', 'awd', '4wd').
    """

    engine: typing.Optional[str] = pydantic.Field(default=None)
    """
    Engine description (e.g. '2.0L Turbo I4', '3.5L V6 Hybrid').
    """

    fuel: typing.Optional[str] = pydantic.Field(default=None)
    """
    Fuel type (e.g. 'gas', 'diesel', 'hybrid', 'phev', 'bev').
    """

    city_mpg: typing.Optional[int] = pydantic.Field(default=None)
    """
    EPA city fuel-economy estimate in miles per gallon. Omit for fully electric vehicles (use `electric_range_mi`).
    """

    highway_mpg: typing.Optional[int] = pydantic.Field(default=None)
    """
    EPA highway fuel-economy estimate in miles per gallon. Omit for fully electric vehicles (use `electric_range_mi`).
    """

    electric_range_mi: typing.Optional[float] = pydantic.Field(default=None)
    """
    Estimated electric range in miles, for BEV and PHEV vehicles.
    """

    exterior_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text exterior color name.
    """

    interior_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text interior color or upholstery name.
    """

    features: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Notable equipment and options as free-text strings (e.g. 'Adaptive Cruise Control', 'Apple CarPlay', 'Heated Front Seats'). v1.0 uses one flat list and does not separate option packages, factory equipment, or installed accessories.
    """

    photos: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Public URLs of vehicle photos, ordered by relevance.
    """

    vdp_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Public Vehicle Detail Page (VDP) URL on the dealer's website.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description / dealer marketing copy.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dealer notes (e.g. 'recently arrived', 'service history available').
    """

    inventory_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date (RFC 3339 full-date, e.g. '2026-04-21') the vehicle first appeared in the dealership's inventory.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO 8601 / RFC 3339 timestamp (with timezone offset) of the last update to this vehicle's availability, price, or status (e.g. '2026-04-30T08:42:00Z'). Buyer agents treat this as the freshness signal for availability claims.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
