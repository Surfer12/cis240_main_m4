# =========================================
# File: educational_components.py
# Description:
#   Educational visualizations and interactive
#   learning components for binary number systems.
# =========================================

from typing import List, Tuple, Dict
from ..core.number_conversion import Colors

def show_concept_map(topic: str = "binary") -> None:
    """Display a concept map for binary number system topics."""
    topics = {
        "binary": {
            "title": "Binary Number Systems",
            "concepts": [
                ("Number Representation", ["Unsigned", "Signed (Two's Complement)", "Fixed-point", "Floating-point"]),
                ("Basic Operations", ["Addition", "Subtraction", "Multiplication", "Division"]),
                ("Digital Logic", ["Gates", "Adders", "Multiplexers"]),
                ("Applications", ["Memory Addressing", "Data Storage", "ALU Operations"])
            ]
        },
        "arithmetic": {
            "title": "Binary Arithmetic",
            "concepts": [
                ("Addition", ["Half Adder", "Full Adder", "Ripple Carry", "Carry Look-ahead"]),
                ("Subtraction", ["Two's Complement", "Borrow Chain", "Add Negative"]),
                ("Multiplication", ["Partial Products", "Booth's Algorithm", "Shift-and-Add"]),
                ("Division", ["Restoring", "Non-restoring", "SRT Division"])
            ]
        }
    }
    
    if topic not in topics:
        print(f"Topic '{topic}' not found. Available topics: {', '.join(topics.keys())}")
        return
    
    topic_data = topics[topic]
    
    # Display concept map
    print(f"\n=== {topic_data['title']} Concept Map ===\n")
    print("┌" + "─" * 60 + "┐")
    print(f"│{topic_data['title']:^60}│")
    print("└" + "─" * 60 + "┘")
    
    for concept, subtopics in topic_data["concepts"]:
        print(f"\n{Colors.BOLD}{concept}{Colors.ENDC}")
        print("├─" + "─" * 40)
        for subtopic in subtopics:
            print(f"│  • {subtopic}")

def show_learning_path(current_level: str = "beginner") -> None:
    """Display a recommended learning path based on current level."""
    levels = {
        "beginner": {
            "current_topics": [
                "Binary counting (0s and 1s)",
                "Basic number conversion (decimal ↔ binary)",
                "Simple addition (no carry)"
            ],
            "next_topics": [
                "Carry in addition",
                "Binary subtraction",
                "Fixed-width numbers"
            ],
            "prerequisites": []
        },
        "intermediate": {
            "current_topics": [
                "Two's complement representation",
                "Multiplication algorithms",
                "Basic circuit components"
            ],
            "next_topics": [
                "Division algorithms",
                "Floating-point representation",
                "ALU design concepts"
            ],
            "prerequisites": ["beginner"]
        },
        "advanced": {
            "current_topics": [
                "Optimized arithmetic circuits",
                "IEEE-754 implementation",
                "Error detection/correction"
            ],
            "next_topics": [
                "Custom number formats",
                "Hardware optimization",
                "Advanced ALU features"
            ],
            "prerequisites": ["beginner", "intermediate"]
        }
    }
    
    if current_level not in levels:
        print(f"Level '{current_level}' not found. Available levels: {', '.join(levels.keys())}")
        return
    
    level_data = levels[current_level]
    
    print(f"\n=== Learning Path ({current_level.title()} Level) ===\n")
    
    if level_data["prerequisites"]:
        print(f"{Colors.YELLOW}Prerequisites:{Colors.ENDC}")
        for prereq in level_data["prerequisites"]:
            print(f"• Complete {prereq.title()} level")
        print()
    
    print(f"{Colors.GREEN}Current Topics:{Colors.ENDC}")
    for topic in level_data["current_topics"]:
        print(f"• {topic}")
    
    print(f"\n{Colors.BLUE}Next Topics:{Colors.ENDC}")
    for topic in level_data["next_topics"]:
        print(f"• {topic}")

def show_practice_problem(topic: str = "addition", difficulty: str = "easy") -> None:
    """Generate and display a practice problem with solution steps."""
    problems = {
        "addition": {
            "easy": {
                "description": "Add two 4-bit binary numbers",
                "problem": ("1010", "0011"),  # 10 + 3
                "solution_steps": [
                    "1. Align numbers right-justified",
                    "2. Add bits column by column",
                    "3. Propagate carry when sum ≥ 2"
                ]
            },
            "medium": {
                "description": "Add two 8-bit numbers with multiple carries",
                "problem": ("11011011", "00110101"),  # 219 + 53
                "solution_steps": [
                    "1. Identify potential carry positions",
                    "2. Track carry chain propagation",
                    "3. Verify final carry out"
                ]
            }
        },
        "subtraction": {
            "easy": {
                "description": "Subtract using two's complement",
                "problem": ("1000", "0011"),  # 8 - 3
                "solution_steps": [
                    "1. Convert subtrahend to two's complement",
                    "2. Add the numbers",
                    "3. Check for borrow propagation"
                ]
            }
        }
    }
    
    if topic not in problems or difficulty not in problems[topic]:
        print(f"Problem not found for topic '{topic}' and difficulty '{difficulty}'")
        return
    
    problem_data = problems[topic][difficulty]
    
    print(f"\n=== Practice Problem ({difficulty.title()} {topic.title()}) ===\n")
    print(f"Task: {problem_data['description']}")
    
    if isinstance(problem_data["problem"], tuple):
        a, b = problem_data["problem"]
        print(f"\nProblem:")
        print(f"  {a}")
        print(f"  {b}")
    else:
        print(f"\nProblem: {problem_data['problem']}")
    
    input("Press Enter to see solution steps...")
    
    print("\nSolution Steps:")
    for i, step in enumerate(problem_data["solution_steps"], 1):
        print(f"{i}. {step}")

def show_interactive_tutorial(topic: str = "binary_basics") -> None:
    """Display an interactive tutorial with explanations and examples."""
    tutorials = {
        "binary_basics": {
            "title": "Binary Number Basics",
            "sections": [
                {
                    "name": "What is Binary?",
                    "content": [
                        "Binary is a base-2 number system using only 0s and 1s.",
                        "Each position represents a power of 2:",
                        "... 8s(2³) 4s(2²) 2s(2¹) 1s(2⁰)"
                    ]
                },
                {
                    "name": "Converting to Decimal",
                    "content": [
                        "To convert binary to decimal:",
                        "1. Identify position values",
                        "2. Multiply each 1 by its position value",
                        "3. Sum all values"
                    ],
                    "example": {
                        "binary": "1101",
                        "steps": [
                            "1 × 2³ = 8",
                            "1 × 2² = 4",
                            "0 × 2¹ = 0",
                            "1 × 2⁰ = 1",
                            "8 + 4 + 0 + 1 = 13"
                        ]
                    }
                }
            ]
        }
    }
    
    if topic not in tutorials:
        print(f"Tutorial '{topic}' not found. Available tutorials: {', '.join(tutorials.keys())}")
        return
    
    tutorial = tutorials[topic]
    
    print(f"\n=== {tutorial['title']} ===\n")
    
    for section in tutorial["sections"]:
        print(f"{Colors.BOLD}{section['name']}{Colors.ENDC}")
        print("─" * len(section["name"]))
        
        for line in section["content"]:
            print(line)
        
        if "example" in section:
            print(f"\n{Colors.GREEN}Example:{Colors.ENDC}")
            print(f"Binary number: {section['example']['binary']}")
            print("\nSolution:")
            for step in section['example']['steps']:
                print(f"  {step}")
        
        input("\nPress Enter to continue...")
        print("\n" + "─" * 40 + "\n")

def show_skill_assessment() -> Dict[str, str]:
    """Conduct a skill assessment and return recommended topics."""
    questions = [
        {
            "text": "Can you convert decimal numbers to binary?",
            "options": ["Not yet", "Basic conversions", "Including fractional parts", "Advanced/All cases"],
            "weight": "number_representation"
        },
        {
            "text": "How comfortable are you with binary arithmetic?",
            "options": ["Not started", "Addition only", "Add/Subtract", "All operations"],
            "weight": "arithmetic"
        },
        {
            "text": "Understanding of two's complement?",
            "options": ["What's that?", "Basic concept", "Can perform conversions", "Expert"],
            "weight": "signed_numbers"
        },
        {
            "text": "Experience with digital logic?",
            "options": ["None", "Basic gates", "Adder circuits", "Complex circuits"],
            "weight": "circuits"
        }
    ]
    
    scores = {
        "number_representation": 0,
        "arithmetic": 0,
        "signed_numbers": 0,
        "circuits": 0
    }
    
    print("\n=== Skill Assessment ===\n")
    print("Answer these questions to get personalized learning recommendations:\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['text']}")
        for j, opt in enumerate(q['options']):
            print(f"   {j + 1}. {opt}")
        
        while True:
            try:
                choice = int(input("\nYour choice (1-4): "))
                if 1 <= choice <= 4:
                    scores[q['weight']] = choice
                    break
                print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number")
    
    # Generate recommendations
    recommendations = {}
    
    for topic, score in scores.items():
        if score <= 2:
            recommendations[topic] = "beginner"
        elif score == 3:
            recommendations[topic] = "intermediate"
        else:
            recommendations[topic] = "advanced"
    
    print("\n=== Assessment Results ===\n")
    for topic, level in recommendations.items():
        print(f"{topic.replace('_', ' ').title()}: {level.title()} level")
    
    return recommendations

def main():
    """Main menu for educational components."""
    while True:
        print("\n=== Educational Tools ===")
        print("1. Show Concept Map")
        print("2. View Learning Path")
        print("3. Practice Problems")
        print("4. Interactive Tutorial")
        print("5. Skill Assessment")
        print("6. Return to Main Menu")
        
        choice = input("\nEnter choice (1-6): ")
        
        if choice == "1":
            topic = input("Enter topic (binary/arithmetic): ").lower()
            show_concept_map(topic)
        elif choice == "2":
            level = input("Enter current level (beginner/intermediate/advanced): ").lower()
            show_learning_path(level)
        elif choice == "3":
            topic = input("Enter topic (addition/subtraction): ").lower()
            difficulty = input("Enter difficulty (easy/medium): ").lower()
            show_practice_problem(topic, difficulty)
        elif choice == "4":
            show_interactive_tutorial()
        elif choice == "5":
            show_skill_assessment()
        elif choice == "6":
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 