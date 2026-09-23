class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0

        for item in self.ledger:
            total += item["amount"]

        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def __str__(self):
        title = self.name.center(30, "*")

        output = title + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):

    # Calculate total spending
    total_spending = 0
    spending = []

    for category in categories:
        category_spending = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spending += -item["amount"]

        spending.append(category_spending)
        total_spending += category_spending

    # Calculate percentages (rounded down to nearest 10)
    percentages = []

    for amount in spending:
        if total_spending == 0:
            percentage = 0
        else:
            percentage = int(amount * 100 // total_spending)

        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Start chart
    chart = "Percentage spent by category\n"

    # Vertical percentage bars
    for level in range(100, -1, -10):

        chart += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find longest category name
    max_length = 0

    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)

    # Category names verticallyy
    for i in range(max_length):

        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip("\n")