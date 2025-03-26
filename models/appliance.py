class Appliance:
    """Represents an appliance."""
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"{self.category}: {self.name}"
