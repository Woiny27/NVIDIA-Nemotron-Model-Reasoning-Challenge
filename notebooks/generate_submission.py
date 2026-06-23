"""
NVIDIA Nemotron Model Reasoning Challenge - Submission Generation Script

This script processes model outputs and generates a properly formatted submission.csv
with three columns: id, reasoning, and answer.

Usage:
    - Import this module in your Colab notebook
    - Call generate_submission() with your test dataset and model outputs
"""

import pandas as pd
import numpy as np


def generate_submission(test_df, raw_outputs, question_col=None, output_path="submission.csv"):
    """
    Generate a properly formatted submission.csv from model outputs.
    
    Args:
        test_df (pd.DataFrame): Test dataset containing 'id' and question column
        raw_outputs (list): List of raw model outputs (strings)
        question_col (str, optional): Name of the question column. 
                                     If None, auto-detects from column names.
        output_path (str): Path where submission.csv will be saved
        
    Returns:
        pd.DataFrame: Submission dataframe with columns ["id", "reasoning", "answer"]
    """
    
    # Auto-detect question column if not provided
    if question_col is None:
        question_cols = [c for c in test_df.columns if "question" in c.lower() or "prompt" in c.lower()]
        if not question_cols:
            raise ValueError("Could not find question/prompt column in test_df. Specify 'question_col' parameter.")
        question_col = question_cols[0]
    
    reasonings = []
    answers = []
    
    # ==========================================
    # 1. PARSE MODEL OUTPUTS
    # ==========================================
    for output in raw_outputs:
        # Split the output to separate reasoning from final answer
        if "Answer:" in output:
            parts = output.split("Answer:")
            # Everything before "Answer:" is the reasoning process
            reasoning_text = parts[0].replace(
                "You are a reasoning assistant. Solve the problem carefully and give a concise answer.", 
                ""
            ).strip()
            answer_text = parts[1].strip()
        else:
            # If no "Answer:" marker, treat entire output as answer
            reasoning_text = "Analysis completed."
            answer_text = output.strip()
        
        reasonings.append(reasoning_text)
        answers.append(answer_text)
    
    # ==========================================
    # 2. ORGANIZE INTO THE EXACT REQUIRED FORMAT
    # ==========================================
    submission = pd.DataFrame({
        "id": test_df["id"].values,
        "reasoning": reasonings,
        "answer": answers
    })
    
    # Save to specified path
    submission.to_csv(output_path, index=False)
    
    # ==========================================
    # 3. INTEGRITY & FORMAT VALIDATION
    # ==========================================
    print("---- Final Submission Sample Check ----")
    print(submission.head(3))
    print(f"\nTotal Rows: {submission.shape[0]}")
    print(f"Output saved to: {output_path}")
    
    # Validate format
    assert list(submission.columns) == ["id", "reasoning", "answer"], \
        f"Column names do not match template! Got {list(submission.columns)}"
    
    print("\n[SUCCESS] submission.csv matches the exact 3-column format layout!")
    print(f"Columns: {list(submission.columns)}")
    
    return submission


if __name__ == "__main__":
    print("Submission generation module loaded. Use generate_submission() in your notebook.")
