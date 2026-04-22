class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)
    def get_grade(self, index):
        body = self.scores[index]
        if 90 <= body <= 100:
            return "A"
        elif 80 <= body < 90:
            return "B"
        elif 75 <= body < 80:
            return "C"
        elif 60 <= body < 75:
            return "D"
        elif 50 <= body < 60:
            return "E"
        else:
            return "F"

    def find(self, value):
        results = []
        for i in range(len(self.scores)):
            if self.scores[i] == value:
                results.append(i)
        return results

    def get_sorted(self):
        scores = self.scores.copy()
        for i in range(len(scores) - 1):
            swapped = False
            for j in range(0, (len(scores) - 1 - i)):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
                    swapped = True
            if not swapped:
                break
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů:", results.count())
    print("\nVýsledky studentů:")
    for i in range(results.count()):
        print(f"Student {i}: {results.scores[i]} points – {results.get_grade(i)}")
    print("\nIndexy studentů se 100 body:", results.find(100))
    print("\nSeřazené výsledky:", results.get_sorted())



if __name__ == "__main__":
    main()
'''print(results.count())  # 9
print(results.get_by_index(2))  # 91
print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
print(results.get_grade(2))  # A (91 bodů)
print(results.get_grade(6))  # A (100 bodů)
print(results.get_grade(7))  # F (38 bodů)
print(results.find(100))  # [6]
print(results.find(50))   # [4]
print(results.find(77))   # []'''
