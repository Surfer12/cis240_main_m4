# Example of using Lenses to update nested data structures
from mojo.lens import Lens

# Define a sample data structure
struct UserState:
    var heart_rate: Int
    var activity_level: String

# Create a Lens for the heart_rate field
let heart_rate_lens = Lens[UserState, Int](getter=lambda state: state.heart_rate, setter=lambda state, value: UserState(state.heart_rate = value, activity_level = state.activity_level))

# Function to update heart rate using the Lens
fn update_heart_rate(state: UserState, new_rate: Int) -> UserState:
    return heart_rate_lens.set(state, new_rate)

# Example usage
let initial_state = UserState(heart_rate=72, activity_level="moderate")
let updated_state = update_heart_rate(initial_state, 80)
print(updated_state)
