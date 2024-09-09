import tkinter as tk
from tkinter import ttk
import webbrowser

# Global variables for survey selection, questions, and current state
questions = []
current_question = 0
selected_survey = ""


# Function to open external links
def open_link(url):
    webbrowser.open_new(url)


# Function to start the selected survey
def start_survey(survey_name):
    global selected_survey
    global current_question
    global question_label
    global next_button
    global answer_vars
    global radio_buttons

    selected_survey = survey_name
    current_question = 0  # Start from the first question
    load_survey_questions(survey_name)

    # Clear the window and setup the survey question UI
    for widget in window.winfo_children():
        widget.destroy()

    # Question label
    question_label = tk.Label(window, text="", font=("Helvetica", 18), bg=theme['bg'], fg=theme['fg'], wraplength=550,
                              justify="left")
    question_label.pack(pady=20)

    # Radio button options for answers
    answer_vars = [tk.IntVar(value=1) for _ in range(10)]
    radio_buttons = []
    for i in range(5):
        rb = tk.Radiobutton(window, text=str(i + 1), variable=answer_vars[0], value=i + 1, font=("Helvetica", 14),
                            bg=theme['bg'], fg=theme['fg'], selectcolor=theme['radio_select_bg'], relief="flat")
        rb.pack(anchor="w", padx=20)
        radio_buttons.append(rb)

    # Button to go to the next question
    next_button = tk.Button(window, text="Next", command=next_question, font=("Helvetica", 14), bg=theme['button_bg'],
                            fg=theme['button_fg'], relief="flat", cursor="hand2")
    next_button.pack(pady=20)

    next_question()  # Load the first question


# Load questions for each survey
def load_survey_questions(survey_name):
    global questions
    if survey_name == "Current Survey":
        questions = [
            "Does your boss criticize you in front of your colleagues?",
            "Does your boss ignore or exclude you from meetings or work-related discussions?",
            "Does your boss spread rumors or talk negatively about you behind your back?",
            "Does your boss withhold important information that affects your job performance?",
            "Does your boss give you unmanageable workloads or set unreasonable deadlines?",
            "Does your boss undermine your work or take credit for your accomplishments?",
            "Does your boss threaten or intimidate you in any way?",
            "Does your boss frequently raise their voice or use aggressive language?",
            "Do you feel anxious or stressed when interacting with your boss?",
            "Do you avoid talking to your boss or feel fearful of doing so?"
        ]
    elif survey_name == "NAQ-R":
        questions = [
            "Have you been humiliated or ridiculed in connection with your work?",
            "Have you been ignored, excluded, or socially isolated?",
            "Has anyone at work withheld information affecting your performance?",
            "Have you been subjected to persistent criticism of your work?",
            "Have you been shouted at or targeted with anger?",
            "Have you experienced any unwelcome sexual advances?",
            "Have you been given tasks below your competence level?",
            "Have you been threatened with violence at work?",
            "Have you experienced physical abuse at work?",
            "Have you faced threats regarding your employment?"
        ]
    elif survey_name == "LIPT":
        questions = [
            "Has someone systematically ignored or excluded you?",
            "Have you been ridiculed or mocked in your workplace?",
            "Have your work efforts been constantly criticized?",
            "Has someone spread false rumors about you?",
            "Have you been assigned meaningless tasks as punishment?",
            "Have you been denied communication opportunities at work?",
            "Have you faced verbal or written threats in your workplace?",
            "Have you experienced malicious reporting on your work?",
            "Have you faced long periods of isolation or exclusion?",
            "Have you been forced to work under severe time pressure?"
        ]


# Function to calculate the score and display results
def calculate_score():
    answers = [var.get() for var in answer_vars]
    score = sum(answers)

    if score >= 35:
        result = "Your boss's behavior indicates significant bullying. Immediate intervention may be necessary."
    elif 25 <= score < 35:
        result = "Your boss's behavior suggests bullying tendencies. Consider seeking advice or assistance."
    elif 15 <= score < 25:
        result = "There may be some negative behaviors, but they are not strongly indicative of bullying."
    else:
        result = "Your boss's behavior does not strongly indicate bullying."

    show_results_screen(score, result)


# Function to display the results screen
def show_results_screen(score, result):
    for widget in window.winfo_children():
        widget.destroy()

    result_label = tk.Label(window, text="Assessment Result", font=("Helvetica", 28, "bold"), bg=theme['bg'],
                            fg=theme['fg'])
    result_label.pack(pady=20)

    score_label = tk.Label(window, text=f"Your total score: {score}", font=("Helvetica", 18), bg=theme['bg'],
                           fg=theme['fg'])
    score_label.pack(pady=10)

    result_text = tk.Label(window, text=result, font=("Helvetica", 16), wraplength=550, bg=theme['bg'], fg=theme['fg'])
    result_text.pack(pady=10)

    # Provide actionable resources
    resources_label = tk.Label(window, text="Take Action Against Workplace Bullying", font=("Helvetica", 22, "bold"),
                               bg=theme['bg'], fg=theme['fg'])
    resources_label.pack(pady=20)

    steps_label = tk.Label(window, text="Actionable Steps for Employers:", font=("Helvetica", 18, "bold"),
                           bg=theme['bg'], fg=theme['fg'])
    steps_label.pack(pady=10)

    steps = [
        "1. Establish a clear anti-bullying policy.",
        "2. Offer confidential reporting options for employees.",
        "3. Train management on handling workplace conflicts.",
        "4. Conduct regular workplace assessments.",
        "5. Implement mediation and conflict resolution strategies.",
    ]
    for step in steps:
        step_label = tk.Label(window, text=step, font=("Helvetica", 14), bg=theme['bg'], fg=theme['fg'], wraplength=550,
                              justify="left")
        step_label.pack(anchor="w", padx=20, pady=2)

    exit_button = tk.Button(window, text="Exit", command=window.quit, font=("Helvetica", 14), bg=theme['button_bg'],
                            fg=theme['button_fg'], relief="flat", cursor="hand2")
    exit_button.pack(pady=20)


# Function to display the next question
def next_question():
    global current_question
    if current_question < len(questions):
        question_label.config(text=questions[current_question])
        for i in range(5):
            radio_buttons[i].config(variable=answer_vars[current_question])
        current_question += 1
    else:
        calculate_score()


# Function to toggle between light and dark mode
def toggle_theme():
    global theme
    theme = dark_theme if theme == light_theme else light_theme
    update_theme()


# Function to apply the current theme
def update_theme():
    window.config(bg=theme['bg'])
    toggle_button.config(bg=theme['button_bg'], fg=theme['button_fg'])
    for rb in radio_buttons:
        rb.config(bg=theme['bg'], fg=theme['fg'], selectcolor=theme['radio_select_bg'])


# Function to display the survey selection page
def show_survey_selection():
    for widget in window.winfo_children():
        widget.destroy()

    selection_label = tk.Label(window, text="Choose a Workplace Bullying Survey", font=("Helvetica", 24, "bold"),
                               bg=theme['bg'], fg=theme['fg'])
    selection_label.pack(pady=20)

    surveys = [
        ("Current Survey", "Focuses on your boss's negative behaviors."),
        ("NAQ-R", "Measures exposure to bullying."),
        ("LIPT", "Focuses on psychological harassment.")
    ]

    for name, description in surveys:
        survey_button = tk.Button(window, text=f"{name}", command=lambda name=name: start_survey(name),
                                  font=("Helvetica", 14), bg=theme['button_bg'], fg=theme['button_fg'], relief="flat",
                                  cursor="hand2")
        survey_button.pack(pady=10)

        desc_label = tk.Label(window, text=description, font=("Helvetica", 12), bg=theme['bg'], fg=theme['fg'])
        desc_label.pack(pady=5)


# Create the main window
window = tk.Tk()
window.title("Boss Bullying Assessment")
window.geometry("600x700")

# Light and dark theme definitions
light_theme = {
    'bg': '#F0F0F0',
    'fg': '#000000',
    'button_bg': '#4CAF50',
    'button_fg': '#FFFFFF',
    'radio_select_bg': '#D0D0D0'
}
dark_theme = {
    'bg': '#333333',
    'fg': '#FFFFFF',
    'button_bg': '#555555',
    'button_fg': '#FFFFFF',
    'radio_select_bg': '#666666'
}
theme = light_theme

# Toggle theme button
toggle_button = tk.Button(window, text="Toggle Dark Mode", command=toggle_theme, font=("Helvetica", 14),
                          bg=theme['button_bg'], fg=theme['button_fg'], relief="flat", cursor="hand2")
toggle_button.pack(pady=10)

# Start the app with the survey selection page
show_survey_selection()

# Start the main event loop
window.mainloop()
