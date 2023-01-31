import tkinter as tk
import random
import os
from PIL import Image, ImageTk
import codecs


class TarotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tarot Reader")

        self.card_images = {}
        self.card_names = {}
        self.card_meanings = {}
        self.cards = []

        # Load all tarot cards into memory
        with codecs.open(os.path.join(os.path.dirname(__file__), "tarot_deck.txt"), "r", "utf-8") as f:
            for line in f:
                card, name, meaning, image = line.strip().split("|")
                self.card_names[card] = name
                self.card_meanings[card] = meaning
                self.card_images[card] = ImageTk.PhotoImage(
                    Image.open(os.path.join(os.path.dirname(__file__), "TarotImages", image)))
                self.cards.append(card)

        # Create widgets
        self.label_card_name = tk.Label(self.master, text="")
        self.label_card_name.pack()

        self.label_card_meaning = tk.Label(self.master, text="")
        self.label_card_meaning.pack()

        self.card_image_label = tk.Label(self.master, image="")
        self.card_image_label.pack()

        self.draw_button = tk.Button(
            self.master, text="Draw Card", command=self.on_draw_card)
        self.draw_button.pack()

        self.reset_button = tk.Button(
            self.master, text="Reset Deck", command=self.reset_deck)
        self.reset_button.pack()

    def on_draw_card(self):
        if not self.cards:
            self.label_card_name.config(
                text="Please reset the deck to draw more cards.")
            self.label_card_meaning.config(text="")
            self.card_image_label.config(image="")
            return
        card = random.choice(self.cards)
        self.cards.remove(card)

        self.label_card_name.config(text=self.card_names[card])
        self.label_card_meaning.config(text=self.card_meanings[card])
        self.card_image_label.config(image=self.card_images[card])

    def reset_deck(self):
        self.cards = list(self.card_names.keys())
        self.label_card_name.config(text="")
        self.label_card_meaning.config(text="")
        self.card_image_label.config(image="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
