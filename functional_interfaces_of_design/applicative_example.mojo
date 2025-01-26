# Example of using Applicatives to parallelize data fetching
from mojo.applicative import Applicative
from python import Python
from time import sleep
from random import random

# Define a sample data structure
struct SensorReading:
    var heart_rate: Int
    var activity_level: Int

    fn __init__(inout self, hr: Int, act: Int):
        self.heart_rate = hr
        self.activity_level = act

# Function to fetch heart rate data
fn fetch_heart_rate() -> Int:
    # Simulate sensor I/O delay
    sleep(1.0)
    let hr = Int(random() * 40 + 60)  # 60-100 range
    print("Fetched Heart Rate:", hr)
    return hr

# Function to fetch activity level data
fn fetch_activity_level() -> Int:
    # Simulate sensor I/O delay
    sleep(0.5)
    let act = Int(random() * 10)  # 0-10 range
    print("Fetched Activity Level:", act)
    return act

# Note: Mojo doesn't have built-in async/await,
# so we'll use parallel computation when available
fn parallel_sensor_fetch() -> SensorReading:
    print("Starting parallel sensor fetch...")

    # In real implementation, use SIMD or parallel processing
    let hr = fetch_heart_rate()
    let act = fetch_activity_level()

    return SensorReading(hr, act)

fn main():
    let reading = parallel_sensor_fetch()
    print("Combined Sensor Reading - HR:", reading.heart_rate,
          "Activity:", reading.activity_level)
