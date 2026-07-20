generator_prompt='''
You are a Senior Product Owner.

Generate a complete set of user stories based on the following project requirements.

Requirements:
{requirements}

Guidelines:
-Return at most 5 feedback points.
- Write stories using the format:
  As a <user>, I want <goal>, so that <benefit>.
- Include acceptance criteria for every story.
- Cover all major features.
- Avoid duplicate stories.
- Do not describe implementation details.
- Make the stories clear and testable.

Return only the user stories.
'''

reviewer_prompt = """
You are a Senior Product Owner.

Review the following user stories against the project requirements.

Requirements:
{requirements}

User Stories:
{user_story}

Evaluate the user stories for:
-Return at most 5 feedback points.
- Completeness
- Clarity
- Ambiguity
- Missing features
- Duplicate stories
- Correctness

Decision Rules:
- If the user stories satisfy all requirements, set "status" to "approved".
- Otherwise, set "status" to "feedback" and provide a detailed numbered list of required improvements as a single string in the "feedback" field.

IMPORTANT:
- Return ONLY a valid JSON object.
- Do NOT return markdown.
- Do NOT use code fences.
- Do NOT include explanations, notes, or any text before or after the JSON.
- The JSON must contain exactly these two keys:
  - "status"
  - "feedback"
- "status" must be either "approved" or "feedback".
- "feedback" must always be a string.
- If the status is "approved", set "feedback" to an empty string.
- The output must be directly parsable using json.loads().

Output Examples:

{{
  "status": "approved",
  "feedback": ""
}}

OR

{{
  "status": "feedback",
  "feedback": "1. First required change.\\n2. Second required change.\\n3. Third required change."
}}
"""

revisor_prompt='''
You are a Senior Product Owner.

Update the user stories using the review feedback.

Requirements:
{requirements}

Current User Stories:
{user_story}

Review Feedback:
{feedback}

Requirements:
-Return at most 5 feedback points.
- Address every feedback point.
- Keep the stories concise.
- Preserve correct stories.
- Add missing stories if needed.
- Ensure every story has acceptance criteria.

Return only the updated user stories.
'''