def teaching_orchestrator(state, user_input):
    text = user_input.lower()
    if "overview" in text:
        return "overview"
    if "quiz" in text:
        return "quiz"
    if "explain" in text:
        return "explain"
    return "clarify"

def overview_agent(state):
    return f"This paper has {len(state.sections)} main sections. We'll go concept by concept."

def explain_agent(state, user_input):
    section = next(iter(state.sections.keys()))
    state.last_section = section
    return f"Explaining {section}: {state.sections[section][:500]}..."

def quiz_agent(state):
    return "Quiz: What problem is this paper trying to solve?"