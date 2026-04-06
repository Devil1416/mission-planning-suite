"""Waypoint and route primitives for mission planning."""
from dataclasses import dataclass
from typing import Optional
import math

@dataclass
class Waypoint:
    lat: float          # degrees
    lon: float          # degrees
    alt: float          # metres ASL
    label: Optional[str] = None

def haversine(wp1: Waypoint, wp2: Waypoint) -> float:
    """Great-circle distance in metres between two waypoints."""
    R = 6_371_000
    phi1, phi2 = math.radians(wp1.lat), math.radians(wp2.lat)
    dphi = math.radians(wp2.lat - wp1.lat)
    dlam = math.radians(wp2.lon - wp1.lon)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2
    return 2 * R * math.asin(math.sqrt(a))

def total_route_distance(waypoints: list[Waypoint]) -> float:
    """Sum of haversine distances along an ordered route."""
    return sum(haversine(waypoints[i], waypoints[i+1])
               for i in range(len(waypoints)-1))
