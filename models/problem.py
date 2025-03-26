class Problem:
    """Represents a problem with an appliance."""
    def __init__(self, description, appliance):
        self.description = description
        self.appliance = appliance

    def __repr__(self):
        return f"Problem: {self.description} (Appliance: {self.appliance.name})"
