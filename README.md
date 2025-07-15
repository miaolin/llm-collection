# LLM Prompt Optimizer

A Python tool that uses GPT-4 to optimize prompts for coding tasks using the Lyra 4-D methodology.

## Features

- **4-D Methodology**: Implements Deconstruct, Diagnose, Develop, and Deliver approach
- **Coding-Specific Optimization**: Tailored for technical and programming tasks
- **Multi-Platform Support**: Optimized for GPT-4, Claude, Gemini, and other AI platforms
- **Flexible Complexity**: Basic and detailed optimization modes
- **Framework Integration**: Support for specific programming frameworks and requirements

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd llm-collection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### Basic Usage

```python
from prompt.generate_prompt import PromptOptimizer

# Initialize the optimizer
optimizer = PromptOptimizer()

# Optimize a basic coding prompt
result = optimizer.generate_coding_prompt(
    coding_task="Create a function to calculate fibonacci numbers",
    programming_language="Python"
)

print(result['optimized_prompt'])
```

### Advanced Usage

```python
# Complex coding task with framework and requirements
result = optimizer.generate_coding_prompt(
    coding_task="Build a REST API with authentication",
    programming_language="Python",
    framework="FastAPI",
    requirements=[
        "JWT authentication",
        "PostgreSQL database", 
        "User management",
        "API documentation"
    ]
)
```

### Custom Optimization

```python
# Custom prompt optimization
result = optimizer.optimize_prompt(
    user_input="Help me debug this Python code that's not working",
    task_type="technical",
    complexity="detail",
    target_platform="gpt-4"
)
```

## Examples

Run the example script to see the optimizer in action:

```bash
python example_usage.py
```

Or run the main script:

```bash
python prompt/generate_prompt.py
```

## How It Works

The prompt optimizer uses the Lyra 4-D methodology:

1. **DECONSTRUCT**: Extracts core intent, key entities, and context
2. **DIAGNOSE**: Audits for clarity gaps and ambiguity
3. **DEVELOP**: Selects optimal techniques based on task type
4. **DELIVER**: Constructs the optimized prompt

### Task Types Supported

- **Creative**: Multi-perspective + tone emphasis
- **Technical**: Constraint-based + precision focus  
- **Educational**: Few-shot examples + clear structure
- **Complex**: Chain-of-thought + systematic frameworks

### Complexity Modes

- **Basic Mode**: Quick fixes, core techniques only
- **Detail Mode**: Comprehensive optimization with clarifying questions

## File Structure

```
llm-collection/
├── prompt/
│   ├── generate_prompt.py      # Main optimizer class
│   └── guildeline_prompt.MD    # Lyra methodology guidelines
├── example_usage.py            # Usage examples
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## API Reference

### PromptOptimizer Class

#### `__init__(api_key=None)`
Initialize the optimizer with OpenAI API key.

#### `optimize_prompt(user_input, task_type="coding", complexity="basic", target_platform="gpt-4")`
Optimize any prompt using the 4-D methodology.

**Parameters:**
- `user_input` (str): The original user prompt
- `task_type` (str): Type of task (coding, creative, technical, educational, complex)
- `complexity` (str): Optimization level (basic, detail)
- `target_platform` (str): Target AI platform

**Returns:** Dictionary with optimized prompt and metadata

#### `generate_coding_prompt(coding_task, programming_language="Python", framework=None, requirements=None)`
Generate optimized prompts specifically for coding tasks.

**Parameters:**
- `coding_task` (str): Description of the coding task
- `programming_language` (str): Target programming language
- `framework` (str, optional): Framework to use
- `requirements` (list, optional): List of specific requirements

**Returns:** Dictionary with optimized coding prompt

## Error Handling

The optimizer includes comprehensive error handling:

- API key validation
- File loading errors
- API call failures
- Network connectivity issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.


