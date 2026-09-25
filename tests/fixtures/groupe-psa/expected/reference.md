# Reference
## Capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_vehicles_capabilities</a>(...) -> VehicleCapabilities</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns vehicle'scharacteristics & capabilities
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.capabilities.get_vehicles_capabilities(
    vin="VF3ABCDE0FG123456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vin:** `str` — Results will only be related to this Vehicle Identification Number.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Locale is used for rendering text according to language and country for. It should match the  REGEX \w(-\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]` — Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Fleet
<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleets</a>(...) -> Fleets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Fleets owned by a partner.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet</a>(...) -> Fleet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Fleet's information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_status_list</a>(...) -> StatusList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest vehicles status for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_status_list(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_mantenance_list</a>(...) -> MaintenanceList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest vehicles maintenance list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_mantenance_list(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_alert_list</a>(...) -> Alerts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the vehicles alerts list for a given fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_alert_list(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_alert_by_id</a>(...) -> Alert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific alert message for a given fleet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_alert_by_id(
    fid="fid",
    aid="aid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**aid:** `str` — id of the alert.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_trips</a>(...) -> Trips</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method returns a list of all Trips. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_trips(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**distance:** `typing.Optional[Range]` 

Trip distance  validity interval. It allows to  define the min or max duration of a trip.  
**Unit = Km** and format : float (only one digit after the decimal point is aceepted for the interval bounds).
  
*Example:*

          * 1-150: Trip with distance between 1 Km and 150 km .
  
          * 0.1-: Trip with distance  greater than 100 m.
  
  default: 0-  
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[Range]` 

Trip duration validity interval. It allows to  define the min or max duration of a trip. **Unit = sec**
  
*Example:*
  
          * 10-3600: Trip with duration between 10 sec and 1 hour.
  
          * 20-: Trip with duration greater than 20 sec.
  
  default: 0-
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]]` 

Allow to filter for Trips with defined states. Those states can be compound of : _Nominal,Unstarted, DataLacking, Unfinished_. 

Default: All states are allowed.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_fleet_trip_collisions</a>(...) -> Collisions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of Collisions that occured on vehicles' fleet. HyperLink (HAL) resolutions of resources within the returned collection are associate to vehicle. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_fleet_trip_collisions(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fleet.<a href="src/fern/fleet/client.py">get_collisions_by_id</a>(...) -> Collision</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Collision that matches the fleet id and the Collision cid. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fleet.get_collisions_by_id(
    fid="fid",
    cid="cid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**cid:** `str` — Results will only contain the Collision related to this Collision ID.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicles
<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicles_by_device</a>(...) -> Vehicles</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Vehicles associated with the Fleet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicles_by_device(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Locale is used for rendering text according to language and country for. It should match the  REGEX \w(-\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[typing.Union[VehiclesExtensionTypeItem, typing.Sequence[VehiclesExtensionTypeItem]]]` — Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.
    
</dd>
</dl>

<dl>
<dd>

**vin_prefix:** `typing.Optional[str]` — Allows filtering on VINs that start with the same prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_byid</a>(...) -> Vehicle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns detailed information about a Vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_byid(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Locale is used for rendering text according to language and country for. It should match the  REGEX \w(-\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]` — Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_car_last_position</a>(...) -> Position</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest GPS Position of the Vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_car_last_position(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_collision</a>(...) -> Collisions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of Collisions that occurred for a given vehicle (id) during the timestamp ranges and bounded by an index range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_collision(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_collision_by_id</a>(...) -> Collision</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Collision that matches the vehicle id and the Collision cid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_collision_by_id(
    fid="fid",
    vid="vid",
    cid="cid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**cid:** `str` — Results will only contain the Collision related to this Collision ID.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_maintenance</a>(...) -> Maintenance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest Maintenance information for a Vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_maintenance(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_fleet_vehicle_status</a>(...) -> Status</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest vehicle status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_fleet_vehicle_status(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_alerts</a>(...) -> Alerts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest alert messages for a Vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_alerts(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_fleet_vehicle_alerts_by_id</a>(...) -> Alert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific alert messages for a Vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_fleet_vehicle_alerts_by_id(
    fid="fid",
    vid="vid",
    aid="aid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**aid:** `str` — id of the alert.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_telemetry</a>(...) -> Telemetries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest Telemetry messages that occurred during a selective timestamp-ranges and bounded by an index range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_telemetry(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]]` 

Results will only contain Telemetry messages of this kind. You can add more than one message type. By default, if no type is selected then all telemetries will be taken ```(the number of elements in this array must be between 1 and 17)```.
 * _Disclaimer_:   ```vehicle.lighting``` is deprecated
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]]` — Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_alarms</a>(...) -> Alarms</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a (filtered) list of alarm for a Vehicle.
*Note:* Timestamp filtering concerns the creation date for status or trigger. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_alarms(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[AlarmTypeEnumItem, typing.Sequence[AlarmTypeEnumItem]]]` — Results will only contain Alarm messages of this type.  If no filtering type is selected then all alarms will be taken .
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_alarms_by_id</a>(...) -> AlarmDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific alarm for a vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_alarms_by_id(
    fid="fid",
    vid="vid",
    aid="aid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**aid:** `str` — id of the alarm.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_stolen_history</a>(...) -> StolenCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns  list of stolen state for a vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_stolen_history(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_stolen_by_id</a>(...) -> Stolen</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific stolen context for a vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_stolen_by_id(
    fid="fid",
    vid="vid",
    sid="sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — id of the stolen state.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/fern/vehicles/client.py">get_vehicle_stolen_id_position</a>(...) -> WayPoints</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns position information about a specific stolen context for a vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vehicles.get_vehicle_stolen_id_position(
    fid="fid",
    vid="vid",
    sid="sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — id of the stolen state.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitors
<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">get_fleet_monitors</a>(...) -> Monitors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of subscribed Monitors of the fleet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.get_fleet_monitors(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">create_fleet_vehicle_monitor</a>(...) -> MonitorRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

>Create a Monitor for all Vehicles of the fleet. This is a kind of vehicle monitor that generates an event following the transition state of one of the (monitored) data  of the vehicles. As for example the fuel level, the moving out of a defined geographical area. 

>When the trigger occurs, the built event expressed as a JSON object will be sent over the subscribed callback.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MonitorCallbackSubscribe, CallbackSubscribeCallback, Webhook, Attribute, AttributeType, MonitorParameterTriggerParam, MonitorTrigger
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.create_fleet_vehicle_monitor(
    fid="fid",
    label="label",
    subscribe_param=MonitorCallbackSubscribe(
        callback=CallbackSubscribeCallback(
            webhook=Webhook(
                target="https://my.post.callback",
                name="My_Webhook",
                attributes=[
                    Attribute(
                        type=AttributeType.HEADER,
                        key="X-Vehicle_Id",
                        value="$vin",
                    )
                ],
            ),
        ),
    ),
    trigger_param=MonitorParameterTriggerParam(
        triggers=[
            MonitorTrigger(
                name="name",
            )
        ],
        bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**request:** `MonitorParameter` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">get_fleet_monitors_status_by_id</a>(...) -> Monitor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a specific Monitor for a given fleet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.get_fleet_monitors_status_by_id(
    fid="fid",
    mid="mid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**mid:** `str` — id of the monitor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">update_fleet_vehicle_monitor</a>(...) -> MonitorRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing ```Monitor``` that has been posted (and accepted previously) for this fleet. The monitor object (body) provided should be complete because the aggregation is not supported for the update of the ```monitor```. You can first retrieve this object using the ```GET /monitor/{mid}``` API, then modify it and finally publish it (via this ```PUT API```).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MonitorCallbackSubscribe, CallbackSubscribeCallback, Webhook, Attribute, AttributeType, MonitorParameterTriggerParam, MonitorTrigger
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.update_fleet_vehicle_monitor(
    fid="fid",
    mid="mid",
    label="label",
    subscribe_param=MonitorCallbackSubscribe(
        callback=CallbackSubscribeCallback(
            webhook=Webhook(
                target="https://my.post.callback",
                name="My_Webhook",
                attributes=[
                    Attribute(
                        type=AttributeType.HEADER,
                        key="X-Vehicle_Id",
                        value="$vin",
                    )
                ],
            ),
        ),
    ),
    trigger_param=MonitorParameterTriggerParam(
        triggers=[
            MonitorTrigger(
                name="name",
            )
        ],
        bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**mid:** `str` — id of the monitor.
    
</dd>
</dl>

<dl>
<dd>

**request:** `MonitorParameter` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">delete_fleet_monitor</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop (disable) an existing Monitor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.delete_fleet_monitor(
    fid="fid",
    mid="mid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**mid:** `str` — id of the monitor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/fern/monitors/client.py">set_fleet_vehicle_monitor_status</a>(...) -> MonitorRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set monitor status. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.monitors import MonitorStatusSetterStatus

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitors.set_fleet_vehicle_monitor_status(
    fid="fid",
    mid="mid",
    status=MonitorStatusSetterStatus.RUNNING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**mid:** `str` — id of the monitor.
    
</dd>
</dl>

<dl>
<dd>

**status:** `MonitorStatusSetterStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trips
<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_trips_by_vehicle</a>(...) -> Trips</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method returns a list of all Trips that a given Vehicle has taken. This will NOT include Trips that have not yet been completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_trips_by_vehicle(
    fid="fid",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**distance:** `typing.Optional[Range]` 

Trip distance  validity interval. It allows to  define the min or max duration of a trip.  
**Unit = Km** and format : float (only one digit after the decimal point is aceepted for the interval bounds).
  
*Example:*

          * 1-150: Trip with distance between 1 Km and 150 km .
  
          * 0.1-: Trip with distance  greater than 100 m.
  
  default: 0-  
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[Range]` 

Trip duration validity interval. It allows to  define the min or max duration of a trip. **Unit = sec**
  
*Example:*
  
          * 10-3600: Trip with duration between 10 sec and 1 hour.
  
          * 20-: Trip with duration greater than 20 sec.
  
  default: 0-
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[TripStateEnum, typing.Sequence[TripStateEnum]]]` 

Allow to filter for Trips with defined states. Those states can be compound of : _Nominal,Unstarted, DataLacking, Unfinished_. 

Default: All states are allowed.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_fleet_trip_by_vehicle</a>(...) -> Trip</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method returns the Trip that matches the Trip id (tid) a given Vehicle (id) has taken.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_fleet_trip_by_vehicle(
    fid="fid",
    vid="vid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_trip_collisions_by_trip_and_vehicle</a>(...) -> Collisions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of Collisions of a vehicle that occurred during a trip and bounded (optional) by a timestamp ranges and an index range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_trip_collisions_by_trip_and_vehicle(
    fid="fid",
    vid="vid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_fleet_trip_alert_by_vehicle</a>(...) -> Alerts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the alert message list for a given vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_fleet_trip_alert_by_vehicle(
    fid="fid",
    vid="vid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_fleet_trip_alert_by_vehicle_by_id</a>(...) -> Alert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the alert message list for a given vehicle that occure during a trip.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_fleet_trip_alert_by_vehicle_by_id(
    fid="fid",
    vid="vid",
    tid="tid",
    aid="aid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**aid:** `str` — id of the alert.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_path_for_trip</a>(...) -> WayPoints</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gives the Vehicle's wayPoints for a specified Trip.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_path_for_trip(
    fid="fid",
    vid="vid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**tolerance:** `typing.Optional[float]` — Tolerance factor is expressed in length km unit and is used to simplify path by reducing the total number of points by is using Douglas-Peucker algorithm to find a similar curve with fewer points (find more info here: [Ramer_Douglas_Peucker_algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm#Algorithm) ).
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trips.<a href="src/fern/trips/client.py">get_telemetry_for_trip_by_vehicle</a>(...) -> Telemetries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the set of Telemetry values that occurred for a given vehicle (id) and a speific Trip (tid) during the timestamp ranges and bounded by an index range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.trips.get_telemetry_for_trip_by_vehicle(
    fid="fid",
    vid="vid",
    tid="tid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**tid:** `str` — The ID {tid} of Trip
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[DataProfile]` 

Results will contain a relative view of the data depending on the selected profile. Indeed, ```endUser``` will expose only the data available to the end-user as if there were no intermediaries between him and the vehicle (case of B-2-B-2-C). If not specified, this parameter will be set to```fleet```value (deault value).

 * _Disclaimer_:  Since the```fleet```profile has a larger data scope, selecting```endUser```profile will potentially result in not found status depending on its granted rights and privacy level. 
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Array of  **"timestamp"** ranges. Results will contain results whose
timestamps are included in those date-time ranges (see **timestamp**
data  model).**"timestamp"** items should be expressed as in
'[RFC3339](https://www.ietf.org/rfc/rfc3339.txt)'. Each element of the array 
expresses a time range (with the pattern ```\w?/\w?``` or ```R\d?/w/w(/w)?```) 
which is the period between two or more times. The range can be expressed by tw
o times Points (start and end *Timestamp*s), by a start
*Timestamp* Point and a *Duration* or as a repeating interval. All of them  should be expressed using the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) and the interval format
is based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)
- 'T1/T2' interval time from low limit T1 to hight T2
- 'T1/D' interval time from low limit T1 with duration = D ( T2=T1+D)
- 'T/' endless range, known start Timestamp but no end Timestamp. The current time  will be used as the high time limit.
- '/T' startless range, known end date but no start date. No lower limit will be used to retrieve results.
- Rn/T/D/[d]  repeat the interval of D **n** times starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H
- R/T/D/[d] unbounded number of repetitions starting at T using **d** (extension of the standard and not mandatory) as range duration. The default (duration) value of d is 24 H.
- T is a timestamp and D is a duration  as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).
  - 2018-01-01T09:00:00+01:00/2018-01-01T12:00:00+01:00* known low and hight limits.
  - *2018-01-03T12:00:00+01:00/P3Y6M4DT12H30M5S*  known low limit, hight limit = start + duration.
  - *2018-01-03T12:00:00+01:00/*  known low limit, hight limit = current time.
  - *R5/2018-01-03T12:00:00Z/P6H/P2H* repeate duration 6H wiht interval period of 2H for 5 times starting at 2018-01-03T12:00:00Z.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page for high frequency data upload. When not set, at most 60 results will be returned.  The range for this parameter is [1...2000]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[TelemetryEnumItem, typing.Sequence[TelemetryEnumItem]]]` 

Results will only contain Telemetry messages of this kind. You can add more than one message type. By default, if no type is selected then all telemetries will be taken ```(the number of elements in this array must be between 1 and 17)```.
 * _Disclaimer_:   ```vehicle.lighting``` is deprecated
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[typing.Union[TelemetryExtensionTypeItem, typing.Sequence[TelemetryExtensionTypeItem]]]` — Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 2)```.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Remote
<details><summary><code>client.remote.<a href="src/fern/remote/client.py">get_fleet_remotes</a>(...) -> RemoteCallbacks</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of subscribed remote callback of the fleet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.get_fleet_remotes(
    fid="fid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[RemoteType, typing.Sequence[RemoteType]]]` — Results will contain only the Remote-Callbacks of these types. _If not specified then the whole callbacks are retrieved_.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">set_fleet_vehicle_remote</a>(...) -> CallbackRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new reusable callback. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RemoteType
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.set_fleet_vehicle_remote(
    fid="fid",
    remote_types=[
        RemoteType.THERMAL_PRECONDITIONING,
        RemoteType.THERMAL_PRECONDITIONING
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RemoteCallbackSubscribe` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">get_fleet_remoteby_id</a>(...) -> RemoteCallback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a subscribed remote callback of the fleet by subscribe ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.get_fleet_remoteby_id(
    fid="fid",
    cbid="cbid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">set_fleet_vehicle_remote_by_id</a>(...) -> CallbackRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Update an existing ```Callback``` that has been posted (and accepted previously) for this fleet. The callback object (body) provided should be complete (aggregation is not supported for the update). This object can be retrieved  using the ```GET /fleets/{fid}/remote/callbacks/{cbid}``` API then modify it and finally publish it (via this ```PUT API```) 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RemoteType
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.set_fleet_vehicle_remote_by_id(
    fid="fid",
    cbid="cbid",
    remote_types=[
        RemoteType.THERMAL_PRECONDITIONING,
        RemoteType.THERMAL_PRECONDITIONING
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RemoteCallbackSubscribe` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">delete_fleet_remote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an existing callback if and only if there is no pending remote attached to it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.delete_fleet_remote(
    fid="fid",
    cbid="cbid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">set_flee_remote_callback_status</a>(...) -> CallbackRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the remote callback status.```Paused``` means that the callback will not post any event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.remote import RemoteCallbacksStatusSetterStatus

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.set_flee_remote_callback_status(
    fid="fid",
    cbid="cbid",
    status=RemoteCallbacksStatusSetterStatus.RUNNING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `RemoteCallbacksStatusSetterStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">get_remote_requests_for_vhl</a>(...) -> RemoteActions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of action remote requested for vehicle.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.get_remote_requests_for_vhl(
    fid="fid",
    vid="vid",
    cbid="cbid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**index_range:** `typing.Optional[IndexRange]` 

Results indexes will be included in this range (see **indexRange** model).
  
  default: 0-

  example: 0-, 0-5
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">send_remote_to_vhl</a>(...) -> RemotePostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new asynchrone vehicle remote action and request it. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.send_remote_to_vhl(
    fid="fid",
    vid="vid",
    cbid="cbid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Remote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote.<a href="src/fern/remote/client.py">get_remote_request_for_vhl_by_id</a>(...) -> RemoteAction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the remote action requested for vehicle by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.remote.get_remote_request_for_vhl_by_id(
    fid="fid",
    vid="vid",
    cbid="cbid",
    rid="rid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fid:** `str` — Resource is related to this fleet ID only.
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Resource is related to this Vehicle ID only.
    
</dd>
</dl>

<dl>
<dd>

**cbid:** `str` — The remote callback ID.
    
</dd>
</dl>

<dl>
<dd>

**rid:** `str` — The remote action ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

