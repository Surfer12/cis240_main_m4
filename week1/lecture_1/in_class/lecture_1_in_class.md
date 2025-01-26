Start of document [text](lect-1-v2.md)
## Representing Information with Voltage
### Notes from Professor's In-class Lecture
"A wire in a computer system serves as the fundamental conduit for transmitting information. This information is encoded in binary form, using two 
distinct voltage levels. Traditionally, these levels have been 0 volts (0v) and 5 volts (5v)."

The interpretation of these voltage levels as logical states is crucial for digital computation. Let's break down the common interpretation:

*   **0 volts (0v):** This level is universally interpreted as **LOGIC 0**, representing the logical state **FALSE**. In conceptual terms, this can be visualized as the system being in an "off" or "low" state.
*   **5 volts (5v) or lower (e.g., 3.3v, 1.8v):** This level is interpreted as **LOGIC 1**, representing the logical state **TRUE**. Conceptually, this corresponds to the system being in an "on" or "high" state.
The interpretation of these voltage levels as logical states is crucial for digital computation. Let's break down the common interpretation:
### Voltage Levels and Logic Levels

The interpretation of these voltage levels as logical states is fundamental to digital computation. Let's examine the standard interpretation:

*   **Low Voltage (Typically 0v):** This level is generally interpreted as **LOGIC 0**, representing the logical state **FALSE**. We can think of this as the system being in an "off" or "low" state.
*   **High Voltage (e.g., 5v, 3.3v, 1.8v):** This level is typically interpreted as **LOGIC 1**, representing the logical state **TRUE**. This corresponds to the system being in an "on" or "high" state.

It's important to note that the exact voltage levels and their corresponding logical interpretations are not arbitrary. Computer designers carefully define them, considering the specific logic family used in the system's circuitry. Different logic families, like Transistor-Transistor Logic (TTL) and Complementary Metal-Oxide-Semiconductor (CMOS), have distinct voltage thresholds and characteristics.

For instance, in classic TTL, a voltage between 0v and 0.8v might be considered LOGIC 0, while a voltage between 2v and 5v might be considered LOGIC 1. In CMOS, the thresholds can differ, and the voltage representing LOGIC 1 could be much lower than 5v.

### Abstraction: From Voltage to Binary

Despite these variations, the core principle remains the same: two distinct voltage ranges are used to represent the binary digits 0 and 1. This is a crucial abstraction. We move from the physical world of varying voltages to the logical world of binary representation, where information is represented by a sequence of 0s and 1s.

### The Bit: The Fundamental Unit of Information

Each wire or memory cell in a computer that can maintain one of these two distinct voltage states is called a **bit**. The bit is the fundamental, indivisible unit of information in digital systems. It represents a binary digit, which can be either 0 or 1.

Therefore, the basic concept of a wire carrying either a low voltage (like 0v) or a high voltage (like 5v, 3.3v, or 1.8v) forms the foundation of how digital information is represented in a computer. These voltage states, interpreted as sequences of LOGIC 0s and LOGIC 1s, are the basis of data storage, processing, and communication in the digital world.

### Beyond Voltage: Other Physical Representations of a Bit

While we've focused on voltage, it's worth noting that a bit can be physically represented in various ways. Fundamentally, a bit represents a choice between two states. These states can be represented by:

*   Different voltage levels on a wire (as discussed)
*   The presence or absence of an electrical charge in a memory cell
*   The direction of magnetization on a magnetic disk
*   The reflection or absorption of light on an optical disc
