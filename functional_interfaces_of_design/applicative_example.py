from dataclasses import dataclass
import asyncio
import random
from typing import Tuple

@dataclass
class SensorReading:
    heart_rate: int
    activity_level: int

async def fetch_heart_rate() -> int:
    # Simulate sensor I/O delay
    await asyncio.sleep(1)
    hr = random.randint(60, 100)
    print(f"Fetched Heart Rate: {hr}")
    return hr

async def fetch_activity_level() -> int:
    # Simulate sensor I/O delay
    await asyncio.sleep(0.5)
    act = random.randint(0, 10)
    print(f"Fetched Activity Level: {act}")
    return act

async def parallel_sensor_fetch() -> SensorReading:
    print("Starting parallel sensor fetch...")
    # Use gather to run fetches concurrently
    hr, act = await asyncio.gather(
        fetch_heart_rate(),
        fetch_activity_level()
    )
    return SensorReading(hr, act)

# Running the example
async def main():
    reading = await parallel_sensor_fetch()
    print(f"Combined Sensor Reading: {reading}")

if __name__ == "__main__":
    asyncio.run(main()) 