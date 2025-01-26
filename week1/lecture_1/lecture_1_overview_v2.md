## Representing Information with Voltage
### Notes from Professor's In-class Lecture
"A wire in a computer system serves as the fundamental conduit for transmitting information. This information is encoded in binary form, using two 
distinct voltage levels. Traditionally, these levels have been 0 volts (0v) and 5 volts (5v)."

The interpretation of these voltage levels as logical states is crucial for digital computation. Let's break down the common interpretation:

*   **0 volts (0v):** This level is universally interpreted as **LOGIC 0**, representing the logical state **FALSE**. In conceptual terms, this can be visualized as the system being in an "off" or "low" state.
*   **5 volts (5v) or lower (e.g., 3.3v, 1.8v):** This level is interpreted as **LOGIC 1**, representing the logical state **TRUE**. Conceptually, this corresponds to the system being in an "on" or "high" state.

It's paramount to understand that the precise voltage levels and their corresponding logical interpretations are not arbitrary. They are meticulously defined by the computer's designer, taking into account the specific logic family employed in the system's circuitry. Different logic families, such as Transistor-Transistor Logic (TTL) and Complementary Metal-Oxide-Semiconductor (CMOS), have their own unique voltage thresholds and characteristics.

I should expand on these points, clarify the phrasing, and provide more context for a lecture setting.

Here's a possible expansion plan:
- Clarify the voltage levels and their relation to logic levels.
- Explain the "off, on, low, high" terminology and standardize it.
- Briefly mention different logic families (though maybe too detailed for an intro lecture).
- Emphasize the bit as the fundamental unit of information.
- Explain the abstraction from physical voltage to logical 0 and 1.
- Connect this to the concept of binary representation discussed in the surrounding lecture notes

For example, in classic TTL, a voltage between 0v and 0.8v might be considered LOGIC 0, while a voltage between 2v and 5v might be considered LOGIC 1. In CMOS, the thresholds might be different, and the voltage representing LOGIC 1 could be significantly lower than 5v.

Despite these variations, the underlying principle remains steadfast: two distinct voltage ranges are employed to represent the binary digits 0 and 1.

Each individual wire or memory cell within the computer's intricate architecture that can maintain one of these two distinct voltage states is referred to as a **bit**. The bit stands as the fundamental, indivisible unit of information in digital systems. It embodies a binary digit, which can exist in one of two possible states: 0 or 1.

Thus, the seemingly elementary concept of a wire carrying either 0v or a higher voltage (like 5v, 3.3v, or 1.8v) forms the very bedrock upon which all digital information is represented within a computer. These voltage states, interpreted as sequences of LOGIC 0s and LOGIC 1s, are the foundation of data storage, processing, and communication in the digital realm.

A bit (binary digit) is one of the two values that can be stored in a computer. The physical representation of a bit can vary, but it fundamentally represents a choice between two states. These states can be represented by different voltage levels on a wire, the presence or absence of an electrical charge in a memory cell, the direction of magnetization on a magnetic disk, or the reflection or absorption of light on an optical disc.

In each case, the underlying principle is the same: two distinct physical states are used to represent the two possible values of a bit.
