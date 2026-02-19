def generate_curriculum(course_name, level, duration_weeks):

    objectives = [
        f"Understand fundamentals of {course_name}",
        f"Apply {course_name} concepts in real-world scenarios",
        f"Analyze problems using {course_name} techniques"
    ]

    modules = []
    for week in range(1, duration_weeks + 1):
        modules.append({
            "week": week,
            "topic": f"{course_name} - Module {week}",
            "learning_outcome": f"Students will understand key concepts of week {week}"
        })

    assessments = [
        "Weekly Quiz",
        "Mid-term Examination",
        "Final Project"
    ]

    return {
        "course_name": course_name,
        "level": level,
        "duration_weeks": duration_weeks,
        "objectives": objectives,
        "modules": modules,
        "assessments": assessments
    }
