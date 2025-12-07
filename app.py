from flask import Flask, render_template, request

app = Flask(__name__)

# Store data in memory
shots_list = []
goals_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    
    if request.method == "POST":
        shots = int(request.form.get("shots"))
        goals = int(request.form.get("goals"))
        
        shots_list.append(shots)
        goals_list.append(goals)
        
        message = "Game stats added!"

    total_shots = sum(shots_list)
    total_goals = sum(goals_list)
    shooting_percentage = (total_goals / total_shots * 100) if total_shots > 0 else 0

    return render_template(
        "index.html",
        shots_list=shots_list,
        goals_list=goals_list,
        total_shots=total_shots,
        total_goals=total_goals,
        shooting_percentage=round(shooting_percentage, 2),
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
