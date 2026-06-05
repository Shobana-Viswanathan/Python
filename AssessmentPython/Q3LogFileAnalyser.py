import re
try:
    file = open("server_log.txt", "r")
    lines = file.readlines()
    total_lines = len(lines)
    total_words = 0
    total_chars = 0
    total_vowels = 0
    levels = {"INFO": 0,"WARNING": 0,"ERROR": 0,"CRITICAL": 0}
    alerts = []
    for line in lines:
        total_words += len(line.split())
        total_chars += len(line)
        for ch in line.lower():
            if ch in "aeiou":
                total_vowels += 1
        match = re.search(r"\[(INFO|WARNING|ERROR|CRITICAL)\]", line)
        if match:
            levels[match.group(1)] += 1
        if "ERROR" in line or "CRITICAL" in line:
            alerts.append(line.strip())

    report = open("log_report.txt", "w")
    report.write("Total Lines : " + str(total_lines) + "\n")
    report.write("Total Words : " + str(total_words) + "\n")
    report.write("Total Chars : " + str(total_chars) + "\n")
    report.write("Total Vowels : " + str(total_vowels) + "\n\n")
    for level, count in levels.items():
        report.write(level + " : " + str(count) + "\n")
    report.write("\nALERTS\n")
    for alert in alerts:
        report.write(alert + "\n")
    report.close()

except FileNotFoundError:
    print("File not found")

finally:
    print("Program Finished")












