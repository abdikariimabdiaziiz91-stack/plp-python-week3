scores = [72, 45, 90, 61, 38]
pass_count = 0
fail_count = 0
total_score = 0

for score in scores:
    total_score += score
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(f"Score: {score} - Grade: {grade}")
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

average = total_score / len(scores)
print(f"\nNumber passed: {pass_count}")
print(f"Number failed: {fail_count}")

cat << 'EOF' > bug_hunt.py
count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

print("Sum of 1 to 5 is: " + str(total))
