# 💻 Laptop Recommendation Expert System


An intelligent expert system that recommends laptops based on user requirements using rule-based artificial intelligence. Built with Python's `experta` library and featuring a modern GUI powered by `customtkinter`.

Developed for CM3321 Logic Programming and Artificial Cognitive Systems module at UoM IT

## 🌟 Features

- **Rule-Based AI Engine**: 12 intelligent rules that match user requirements to optimal laptop categories
- **Interactive GUI**: Clean, modern dark-themed interface with step-by-step questions
- **Smart Recommendations**: Considers multiple factors including:
  - Primary use case (gaming, creative work, school, general use)
  - Budget constraints
  - Portability requirements
  - Battery life needs
  - Special features (touchscreen, durability, numeric keypad)
  - Operating system preferences
- **Specific Model Suggestions**: Provides actual laptop models for each recommendation
- **Priority-Based Logic**: Uses salience to prioritize critical requirements

## 🏗️ Architecture

### Components

1. **`knowledge_base.py`**: The expert system engine
   - Contains the `LaptopKnowledgeEngine` class
   - Defines 12 rules for different user scenarios
   - Implements forward-chaining inference

2. **`ui.py`**: The graphical user interface
   - Built with `customtkinter` for modern aesthetics
   - 6-question wizard for gathering user requirements
   - Results display with recommendations and reasoning

3. **`main.py`**: Application entry point
   - Bridges the UI and expert system
   - Handles fact declaration and inference execution

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone or download the project**:
   ```bash
   cd expert_system/Codebase
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install experta customtkinter
   ```

## 📖 Usage

### Running the Application

```bash
python main.py
```

### How It Works

1. **Launch the application**: The GUI opens with the first question
2. **Answer 6 questions**:
   - What is your primary use?
   - What is your budget range?
   - How portable does it need to be?
   - How important is battery life?
   - Which features are important?
   - Operating system preference?
3. **Get your recommendation**: Click "Get Recommendation" to see:
   - Recommended laptop category
   - Detailed reasoning
   - Specific laptop models to consider
4. **Start over**: Click "Start Over" to try different criteria

## 🧠 Expert System Logic

### Rule Categories

The system implements 12 rules covering various scenarios:

| Priority | Rule | Conditions | Recommendation |
|----------|------|------------|----------------|
| High (10) | Gaming Enthusiast | Gaming + High Budget | Gaming Laptop |
| High (10) | Student Note-Taker | School + Touchscreen | 2-in-1 Convertible |
| High (10) | macOS User | macOS preference | MacBook (Ultrabook) |
| Normal | Student Commuter | School + Daily portability + Critical battery | Ultrabook |
| Normal | Creative Professional | Creative + Unlimited budget | Professional Workstation |
| Normal | Premium General | General + High-end budget | Ultrabook |
| Medium (5) | Business Durability | Durability feature | Professional Workstation |
| Normal | Economy Budget | Budget < $600 | Budget All-Rounder |
| Normal | Desk-Bound User | Stays on desk | Budget All-Rounder |
| Low (-1) | Default Fallback | No specific match | Budget All-Rounder |

### Laptop Categories

- **Ultrabook**: Thin, light, premium laptops with excellent battery life
- **Gaming Laptop**: High-performance laptops with dedicated graphics
- **2-in-1 Convertible**: Versatile laptops with touchscreen and flexible form factors
- **Budget All-Rounder**: Affordable, general-purpose laptops
- **Professional Workstation**: Enterprise-grade laptops built for reliability

### How Rules Fire

1. User responses are converted to `Fact` objects
2. The expert system evaluates all rules against current facts
3. Rules with matching conditions fire (highest salience first)
4. A recommendation fact is declared with category, reason, and models
5. The first recommendation is extracted and displayed

## 📁 Project Structure

```
expert_system/
├── Codebase/
│   ├── knowledge_base.py    # Expert system rules and logic
│   ├── ui.py                # GUI implementation
│   ├── main.py              # Application entry point
│   ├── requirements.txt     # Python dependencies
│   ├── pyproject.toml       # Project configuration
│   └── README.md            # This file
└── Video Demo/              # Demo materials
```

## 🛠️ Technical Details

### Technologies Used

- **experta**: Python expert system library (CLIPS-like)
- **customtkinter**: Modern, customizable tkinter widgets
- **Python 3.x**: Core programming language

### Key Design Patterns

- **Rule-Based System**: Declarative rules for transparent decision-making
- **Forward Chaining**: Fact-driven inference from user input to recommendation
- **Salience-Based Priority**: Critical requirements evaluated first
- **MVC Pattern**: Separation of expert system logic, UI, and application control

## 🎯 Example Scenarios

### Scenario 1: Budget-Conscious Student
- **Inputs**: School use, Economy budget, Daily portability
- **Recommendation**: Budget All-Rounder or Ultrabook
- **Models**: Acer Aspire 5, Lenovo IdeaPad 3, HP Pavilion 15

### Scenario 2: Gaming Enthusiast
- **Inputs**: Gaming, High-end budget
- **Recommendation**: Gaming Laptop
- **Models**: ASUS ROG Zephyrus G14, MSI Raider GE78, Alienware m16

### Scenario 3: Creative Professional
- **Inputs**: Creative work, Unlimited budget
- **Recommendation**: Professional Workstation
- **Models**: Apple MacBook Pro 16, Dell XPS 15, HP ZBook Studio G10

## 🔧 Customization

### Adding New Rules

Edit `knowledge_base.py` and add a new method decorated with `@Rule`:

```python
@Rule(
    Fact(your_condition="value"),
    salience=5  # Set priority
)
def your_new_rule(self):
    self.declare(Fact(
        recommendation="Category",
        reason="Your reasoning",
        models="Model1, Model2, Model3"
    ))
```

### Modifying Questions

Edit `ui.py` and update the relevant `create_question_X()` method to change options or add new questions.

## 📝 License

This project is created for educational purposes.

## 👥 Authors

Built as a demonstration of expert systems and rule-based AI.

## 🤝 Contributing

Feel free to fork this project and enhance it with:
- Additional rules for edge cases
- More laptop categories
- Price range updates
- New feature considerations
- Improved UI/UX

## 📞 Support

For questions or issues, please refer to the code documentation or modify the rules to suit your specific needs.

---

**Note**: This README is generated with Claude Sonnet 4 for the expression of the project details.
