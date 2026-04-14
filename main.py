def display_student_info(data):
    print("--- Student Record ---")
    print(f"Name: {data['name']}")
    print(f"Year Level: {data['year']}")
    print(f"Section: {data['section'][0]} - {data['section'][1]}")
    print(f"Skills: {', '.join(data['skills'])}")
    print("----------------------")

student = {
    "name": "Norberto Ayat III",
    "year": 3,
    "skills": ["Python", "Git", "SQL", "Linux"],
    "section": ("CPE106L", "A")
}

if __name__ == "__main__":
    display_student_info(student)