import tkinter as tk
from tkinter import messagebox

def suggest_career():
    skills = skills_entry.get().lower()
    interests = interests_entry.get().lower()
    
    suggestions = []
    
    if "python" in skills or "data" in interests:
        suggestions.append("Data Scientist - Skills: Python, SQL, Machine Learning")
    if "javascript" in skills or "web" in interests:
        suggestions.append("Front-end Developer - Skills: JavaScript, React, CSS")
    if "cloud" in skills or "devops" in interests:
        suggestions.append("Cloud Engineer - Skills: AWS, Azure, Docker")
    if "security" in skills or "hacking" in interests:
        suggestions.append("Cybersecurity Analyst - Skills: Network Security, Ethical Hacking")
    
    if suggestions:
        result = "\n".join(suggestions)
    else:
        result = "No clear path found. Try specifying more skills or interests."
    
    messagebox.showinfo("Career Suggestions", result)

# GUI Setup
root = tk.Tk()
root.title("Tech Career Path Finder")
root.geometry("400x300")

tk.Label(root, text="Enter your tech skills (comma-separated):").pack(pady=5)
skills_entry = tk.Entry(root, width=50)
skills_entry.pack(pady=5)

tk.Label(root, text="Enter your interests (comma-separated):").pack(pady=5)
interests_entry = tk.Entry(root, width=50)
interests_entry.pack(pady=5)

tk.Button(root, text="Find Career Path", command=suggest_career).pack(pady=20)

root.mainloop()
