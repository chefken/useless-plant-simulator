import tkinter as tk
import random

# --- VirtualPlant Class ---
class VirtualPlant:
    def __init__(self, name):
        self.name = name
        self.species = random.choice(["Fern", "Cactus", "Sunflower", "Bamboo"])
        self.health = 100
        self.age = 0

    def water(self):
        change = random.choice([10, -5, 0])
        self.health += change
        return change

    def sunlight(self):
        change = random.choice([10, -10, 0])
        self.health += change
        return change

    def fertilize(self):
        change = random.choice([15, -10, 5])
        self.health += change
        return change

    def pass_time(self):
        self.age += 1
        self.health -= random.randint(1, 5)

# --- GUI Application ---
class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Useless Virtual Plant Simulator 🌱")
        self.plant = None

        # Entry UI
        self.name_label = tk.Label(root, text="Enter Plant Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        # Status area
        self.status = tk.Label(root, text="", justify="left", font=("Courier", 10))
        self.status.pack(pady=10)

        # Action buttons
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()
        self.water_button = tk.Button(self.buttons_frame, text="Water", command=self.water)
        self.sun_button = tk.Button(self.buttons_frame, text="Sunlight", command=self.sunlight)
        self.fert_button = tk.Button(self.buttons_frame, text="Fertilize", command=self.fertilize)
        self.nothing_button = tk.Button(self.buttons_frame, text="Do Nothing", command=self.do_nothing)

        for b in [self.water_button, self.sun_button, self.fert_button, self.nothing_button]:
            b.config(state=tk.DISABLED)
            b.pack(side=tk.LEFT, padx=5)

    def start_game(self):
        name = self.name_entry.get().strip() or "Ken Sony"
        self.plant = VirtualPlant(name)

        # Hide input fields
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        # Enable buttons
        for b in [self.water_button, self.sun_button, self.fert_button, self.nothing_button]:
            b.config(state=tk.NORMAL)

        self.update_status("Your plant journey begins...\n")

    def update_status(self, action_text=""):
        if self.plant.health <= 0:
            self.status.config(text=f"\n💀 {self.plant.name} has died...\n{action_text}")
            for b in [self.water_button, self.sun_button, self.fert_button, self.nothing_button]:
                b.config(state=tk.DISABLED)
            return

        random_text = random.choice([
            "It looks at you with mild disappointment.",
            "It seems to be plotting something.",
            "It somehow made a weird noise.",
            "It has no idea what it's doing.",
            "You feel judged."
        ])

        status_text = (
            f"🌱 {self.plant.name} ({self.plant.species})\n"
            f"Health: {self.plant.health}\n"
            f"Age: {self.plant.age} days\n"
            f"Photosynthesis: {random.randint(0, 999)}%\n"
            f"Soil Confidence: {random.choice(['Low', 'High', 'Suspicious'])}\n\n"
            f"{action_text}{random_text}"
        )
        self.status.config(text=status_text)

    def water(self):
        effect = self.plant.water()
        text = self.effect_message("watered", effect)
        self.next_turn(text)

    def sunlight(self):
        effect = self.plant.sunlight()
        text = self.effect_message("gave sunlight to", effect)
        self.next_turn(text)

    def fertilize(self):
        effect = self.plant.fertilize()
        text = self.effect_message("fertilized", effect)
        self.next_turn(text)

    def do_nothing(self):
        text = "You stare at the plant awkwardly...\n"
        self.next_turn(text)

    def next_turn(self, action_text):
        self.plant.pass_time()
        self.update_status(action_text)

    def effect_message(self, action, effect):
        base = f"\nYou {action} {self.plant.name}...\n"
        if effect < 0:
            return base + "It hated that. Why would you do that?\n"
        elif effect == 0:
            return base + "Nothing happened. Of course.\n"
        else:
            return base + "It seems happier... for now.\n"

# --- Run the Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PlantApp(root)
    root.mainloop()