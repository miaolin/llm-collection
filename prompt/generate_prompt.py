import openai
import json
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ROOT_PATH)


class PromptOptimizer:
    def __init__(self, api_key: str = None):
        """Initialize the prompt optimizer with OpenAI API key."""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        # Initialize OpenAI client with new API
        self.client = openai.OpenAI(api_key=self.api_key)
        
        # Load the guideline prompt
        self.guideline_prompt = self._load_guideline_prompt()
    
    def _load_guideline_prompt(self) -> str:
        """Load the guideline prompt from the markdown file."""
        try:
            with open(os.path.join(ROOT_PATH, "prompt", "guideline_prompt.MD"), "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError("guideline_prompt.MD not found in prompt/ directory")
    
    def optimize_prompt(self, 
                       user_input: str, 
                       task_type: str = "coding",
                       complexity: str = "basic",
                       target_platform: str = "gpt-4") -> Dict:
        """
        Optimize a prompt using the 4-D methodology.
        
        Args:
            user_input: The original user prompt/request
            task_type: Type of task (coding, creative, technical, educational, complex)
            complexity: Level of optimization (basic, detail)
            target_platform: Target AI platform (gpt-4, claude, gemini, etc.)
        
        Returns:
            Dictionary containing optimized prompt and metadata
        """
        
        # Construct the optimization request
        optimization_request = f"""
{self.guideline_prompt}

## TASK TO OPTIMIZE:
User Input: {user_input}
Task Type: {task_type}
Complexity Level: {complexity}
Target Platform: {target_platform}

Please apply the 4-D methodology to optimize this prompt for {task_type} tasks on {target_platform}.

Follow the {complexity.upper()} MODE guidelines and provide the response in the appropriate format.
"""
        
        try:
            # Call GPT-4 to optimize the prompt using new API
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI prompt optimization specialist following the Lyra methodology."},
                    {"role": "user", "content": optimization_request}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            optimized_content = response.choices[0].message.content
            
            return {
                "original_input": user_input,
                "task_type": task_type,
                "complexity": complexity,
                "target_platform": target_platform,
                "optimized_prompt": optimized_content,
                "model_used": "gpt-4",
                "tokens_used": response.usage.total_tokens
            }
            
        except Exception as e:
            return {
                "error": f"Failed to optimize prompt: {str(e)}",
                "original_input": user_input
            }
    
    def generate_coding_prompt(self, 
                              coding_task: str,
                              programming_language: str = "Python",
                              framework: str = None,
                              requirements: List[str] = None) -> Dict:
        """
        Generate an optimized prompt specifically for coding tasks.
        
        Args:
            coding_task: Description of the coding task
            programming_language: Target programming language
            framework: Optional framework to use
            requirements: List of specific requirements
        
        Returns:
            Dictionary containing optimized coding prompt
        """
        
        # Construct coding-specific input
        coding_input = f"""
Coding Task: {coding_task}
Programming Language: {programming_language}
"""
        
        if framework:
            coding_input += f"Framework: {framework}\n"
        
        if requirements:
            coding_input += f"Requirements: {', '.join(requirements)}\n"
        
        return self.optimize_prompt(
            user_input=coding_input,
            task_type="technical",
            complexity="detail",
            target_platform="gpt-4"
        )

def main():
    """Main function to demonstrate the prompt optimizer."""
    
    # Example usage
    try:
        optimizer = PromptOptimizer()
        
        # Example 1: Basic coding task
        print("=== Example 1: Basic Coding Task ===")
        result1 = optimizer.generate_coding_prompt(
            coding_task="Create a function to calculate fibonacci numbers",
            programming_language="Python"
        )
        print(json.dumps(result1, indent=2))
        print("\n" + "="*50 + "\n")
        
        # Example 2: Complex coding task
        print("=== Example 2: Complex Coding Task ===")
        result2 = optimizer.generate_coding_prompt(
            coding_task="Build a REST API with authentication and database integration",
            programming_language="Python",
            framework="FastAPI",
            requirements=["JWT authentication", "PostgreSQL database", "User management", "API documentation"]
        )
        print(json.dumps(result2, indent=2))
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure to set your OPENAI_API_KEY environment variable.")

if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    main()
