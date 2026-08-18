def format_report(func):
    def wrapper(self):
        report = func(self)
        return f"\n{'=' * 40}\n{report}\n{'=' * 40}"
    return wrapper


class Report:
    templates = {
        "simple": "Simple Report",
        "detailed": "Detailed Report"
    }

    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name, "Default Report")

    @format_report
    def generate(self):
        return f"Title: {self.title}\nContent: {self.content}\nTemplate: {self.template}"

    def __str__(self):
        return f"{self.title} - {self.template}"


title = input("Enter report title: ")
content = input("Enter report content: ")

print("1. Simple")
print("2. Detailed")

choice = int(input("Choose template: "))

if choice == 1:
    template = Report.get_template("simple")
elif choice == 2:
    template = Report.get_template("detailed")
else:
    template = Report.get_template("default")

report = Report(title, content, template)

print("\nReport Object:")
print(report)

print("\nGenerated Report:")
print(report.generate())
