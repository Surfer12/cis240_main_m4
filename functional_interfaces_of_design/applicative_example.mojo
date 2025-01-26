# Example of using Applicatives to parallelize data fetching
from mojo.applicative import Applicative

# Define a sample data structure
struct SensorData:
    var heart_rate: Int
    var activity_level: String

# Function to fetch heart rate data
fn fetch_heart_rate() -> Int:
    # Simulate fetching heart rate data
    return 75

# Function to fetch activity level data
fn fetch_activity_level() -> String:
    # Simulate fetching activity level data
    return "high"

# Combine data using Applicative
let sensor_data = Applicative[SensorData](heart_rate=fetch_heart_rate(), activity_level=fetch_activity_level())
print(sensor_data)
