LANGUAGES = [
    "Python", "JavaScript", "TypeScript", "Java", "C++", "C",
    "Go", "Rust", "Swift", "Kotlin", "Ruby", "PHP",
    "SQL", "Bash", "HTML/CSS", "R", "Dart", "Scala",
]

MODEL = "models/gemini-2.5-flash"

MAX_TOKENS = 2048

SYSTEM_PROMPT = (
    "You are an expert programmer. Generate clean, well-commented, "
    "production-ready code. Return only the code block with no extra explanation "
    "unless the user explicitly asks for it."
)