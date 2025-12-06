# Simple Soccer Shot & Goal Tracker for 10 Games

games = 10
shots_list = []
goals_list = []

print("Soccer Stats Tracker (10 Games)")
print("-------------------------------")

for game in range(1, games + 1):
    print(f"\nGame {game}")
    shots = int(input("  Enter number of shots: "))
    goals = int(input("  Enter number of goals: "))

    shots_list.append(shots)
    goals_list.append(goals)

print("\n===== SUMMARY =====")

total_shots = sum(shots_list)
total_goals = sum(goals_list)

print(f"Total Shots: {total_shots}")
print(f"Total Goals: {total_goals}")

if total_shots > 0:
    shooting_percentage = (total_goals / total_shots) * 100
    print(f"Shooting Percentage: {shooting_percentage:.2f}%")
else:
    print("Shooting Percentage: N/A (no shots taken)")

print("\nThanks for using the Soccer Stats Tracker!")
